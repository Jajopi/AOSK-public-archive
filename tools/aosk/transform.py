"""Turn an extracted LaTeX block (statement/solution) into web-ready Markdown.

Order: strip comments → normalise environments → siunitx → numbering + refs → figures →
text macros → drop styling → protect math → pandoc (gfm + Lua filter) → restore math.
"""
import re
import subprocess
from pathlib import Path
from .latex import (strip_comments, replace_cmd, find_envs, split_math, map_text, map_math, split_rows,
                    read_group)
from . import siunitx

HERE = Path(__file__).resolve().parent
LUA = HERE.parent / 'filters' / 'aosk.lua'

# Astronomical symbols etc. that are math macros (see site/data/katex.yaml); wrapped into math when used in text.
TEXT_TO_MATH = ['Sun', 'Earth', 'Ea', 'Ze', 'Moon', 'Mo', 'Mars', 'Ma', 'Me', 'Ve', 'Ju', 'Sa', 'Ur', 'Ne', 'Pl',
                'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Venus', 'Mercury', 'Pluto', 'leftmoon', 'Aries',
                'Taurus', 'messier', 'ztv']

STYLE_DROP_0 = ['centering', 'raggedright', 'raggedleft', 'noindent', 'newpage', 'clearpage', 'pagebreak',
                'linebreak', 'vfill', 'hfill', 'medskip', 'bigskip', 'smallskip', 'par', 'tiny', 'scriptsize',
                'footnotesize', 'small', 'normalsize', 'large', 'Large', 'LARGE', 'huge', 'Huge', 'justifying',
                'break', 'allowbreak', 'newline', 'FloatBarrier', 'protect', 'selectfont', 'normalfont',
                'intro', 'intermezzo', 'prechod', 'finito', 'prechodDoRiesenia', 'phantomsection', 'qquad']
STYLE_DROP_1 = ['vspace', 'hspace', 'phantom', 'hphantom', 'vphantom', 'label', 'pageref', 'setlength',
                'addvspace', 'enlargethispage', 'thispagestyle', 'pagestyle', 'fontsize', 'zlomStranyZadanie',
                'zlomStranyRiesenie', 'komentarRado', 'needspace', 'captionsetup']


class Ctx:
    """Per-problem state shared by statement and solution (counters, labels, figure handler, warnings)."""

    def __init__(self, units, figure_handler, pid):
        self.units, self.figure_handler, self.pid = units, figure_handler, pid
        self.eq = self.fig = self.tab = 0
        self.labels = {}
        self.warnings = []

    def warn(self, msg):
        self.warnings.append(msg)


# ---------------------------------------------------------------- environments

def drop_definitions(s: str) -> str:
    """Remove macro definitions made inside the problem text (they may contain math, so do it first)."""
    pat = re.compile(r'\\(newcommand|renewcommand|providecommand|def|let)\*?(?![A-Za-z])')
    out, pos = [], 0
    while True:
        m = pat.search(s, pos)
        if not m:
            break
        j = m.end()
        if m.group(1) == 'let':
            mm = re.match(r'\s*\\[A-Za-z]+\s*=?\s*\\[A-Za-z]+', s[j:])
            j += mm.end() if mm else 0
        elif m.group(1) == 'def':
            mm = re.match(r'\s*\\[A-Za-z]+(#\d)*', s[j:])
            if not mm:
                out.append(s[pos:j]); pos = j; continue
            j += mm.end()
            _, j = read_group(s, j)
        else:
            _, j = read_group(s, j)                     # {\name}
            if j == m.end():                            # \newcommand\name
                mm = re.match(r'\s*\\[A-Za-z]+', s[j:]); j += mm.end() if mm else 0
            while True:                                 # [n][default]
                o, j2 = read_group(s, j, '[', ']')
                if o is None:
                    break
                j = j2
            _, j = read_group(s, j)                     # {body}
        out.append(s[pos:m.start()]); pos = j
    out.append(s[pos:])
    return ''.join(out)


def normalise_envs(s: str) -> str:
    s = re.sub(r'\\begin\{comment\}.*?\\end\{comment\}', '', s, flags=re.S)
    s = re.sub(r'\\iffalse\b.*?\\fi\b', '', s, flags=re.S)
    for a, b in (('enumerateShort', 'enumerate'), ('enumerateSemiShort', 'enumerate'), ('itemizeShort', 'itemize'),
                 ('itemizeSemiShort', 'itemize'), ('longtag', None), ('longtable', 'tabular')):
        if b is None:
            s = re.sub(r'\\(begin|end)\{' + a + r'\}', '', s)
        else:
            s = re.sub(r'\\(begin|end)\{' + a + r'\}', r'\\\1{' + b + '}', s)
    # floats with extra args → plain figure/table
    s = re.sub(r'\\begin\{(?:wrapfigure|wrapfig)\}(\[[^\]]*\])?\{[^}]*\}(\[[^\]]*\])?\{[^}]*\}', r'\\begin{figure}', s)
    s = re.sub(r'\\end\{wrapfigure\}', r'\\end{figure}', s)
    s = re.sub(r'\\begin\{wraptable\}(\[[^\]]*\])?\{[^}]*\}(\[[^\]]*\])?\{[^}]*\}', r'\\begin{table}', s)
    s = re.sub(r'\\end\{wraptable\}', r'\\end{table}', s)
    s = re.sub(r'\\(begin|end)\{(?:sidewaysfigure|AOsidewaysfigure|figure\*)\}', r'\\\1{figure}', s)
    s = re.sub(r'\\(begin|end)\{(?:sidewaystable|table\*)\}', r'\\\1{table}', s)
    # minipage with \captionof{figure|table} is a float in disguise
    def mp(m):
        body = m.group(2)
        k = re.search(r'\\captionof\{(figure|table)\}', body)
        if not k:
            return m.group(0)
        body = re.sub(r'\\captionof\{(?:figure|table)\}', lambda _: '\\caption', body)
        return '\\begin{%s}%s\\end{%s}' % (k.group(1), body, k.group(1))
    s = re.sub(r'\\begin\{minipage\}((?:\[[^\]]*\])*\{[^}]*\})(.*?)\\end\{minipage\}', mp, s, flags=re.S)
    s = re.sub(r'\\captionof\{(?:figure|table)\}', lambda _: '\\caption', s)
    # wrappers whose content we keep
    s = re.sub(r'\\begin\{(?:minipage|subfigure|subtable)\}(\[[^\]]*\])*\{[^}]*\}', '', s)
    s = re.sub(r'\\end\{(?:minipage|subfigure|subtable)\}', '', s)
    s = re.sub(r'\\begin\{multicols\}\{[^}]*\}|\\end\{multicols\}', '', s)
    s = re.sub(r'\\begin\{(?:adjustbox|tcolorbox|samepage|flushleft|flushright|taggedblock)\}(\[[^\]]*\])?(\{[^}]*\})?'
               r'|\\end\{(?:adjustbox|tcolorbox|samepage|flushleft|flushright|taggedblock)\}', '', s)
    for cmd in ('rotatebox', 'scalebox'):
        s = replace_cmd(s, cmd, 2, lambda o, a, b: b, opt=True)
    s = replace_cmd(s, 'resizebox', 3, lambda o, a, b, c: c, star=True)
    return s


# ---------------------------------------------------------------- numbering

def number_equations(s: str, ctx: Ctx) -> str:
    envs = ('equation', 'align', 'gather', 'multline', 'eqnarray', 'flalign', 'alignat',
            'equation*', 'align*', 'gather*', 'multline*', 'eqnarray*', 'flalign*', 'alignat*')
    out, pos = [], 0
    for b0, b1, e0, e1, name in find_envs(s, envs):
        body = s[b1:e0]
        starred = name.endswith('*')
        base = name.rstrip('*')
        if base == 'alignat':
            _, k = read_group(body, 0)
            body = body[k:]
        if base == 'eqnarray':
            body = '\\\\'.join(re.sub(r'&([^&]*)&', r'&\1', r) for r in split_rows(body))
        rows = split_rows(body) if base not in ('equation',) else [body]
        new_rows = []
        for r in rows:
            labels = re.findall(r'\\label\{([^}]*)\}', r)
            r = re.sub(r'\\label\{[^}]*\}', '', r)
            has_tag = re.search(r'\\tag\*?\{', r)
            if re.search(r'\\(nonumber|notag)\b', r) or starred or (base == 'multline' and r is not rows[-1]):
                r = re.sub(r'\\(nonumber|notag)\b', '', r)
                for l in labels:
                    ctx.labels[l] = '?'
            elif has_tag:
                for l in labels:
                    ctx.labels[l] = '(' + re.search(r'\\tag\*?\{([^}]*)\}', r).group(1) + ')'
            elif r.strip():
                ctx.eq += 1
                r = r.rstrip() + ' \\tag{%d}' % ctx.eq
                for l in labels:
                    ctx.labels[l] = '(%d)' % ctx.eq
            new_rows.append(r)
        if base == 'equation':
            inner = new_rows[0]
            if '\\\\' in inner and not re.search(r'\\begin\{(split|aligned|gathered|cases|array|[pbvBV]?matrix)', inner):
                inner = '\\begin{gathered}' + inner + '\\end{gathered}'
            rep = '\\[' + inner + '\\]'
        elif base == 'multline':
            tag = ''
            last = new_rows[-1]
            mt = re.search(r'\\tag\{[^}]*\}', last)
            if mt:
                tag, new_rows[-1] = mt.group(0), last.replace(mt.group(0), '')
            rep = '\\[\\begin{gathered}' + '\\\\'.join(new_rows) + '\\end{gathered}' + tag + '\\]'
        elif base == 'gather':
            rep = '\\[\\begin{gather*}' + '\\\\'.join(new_rows) + '\\end{gather*}\\]'
        else:
            rep = '\\[\\begin{align*}' + '\\\\'.join(new_rows) + '\\end{align*}\\]'
        if rep.count('\\tag') > 1 or (base == 'equation' and False):
            pass
        out.append(s[pos:b0]); out.append(rep); pos = e1
    out.append(s[pos:])
    return ''.join(out)


def number_floats(s: str, ctx: Ctx) -> str:
    out, pos = [], 0
    for b0, b1, e0, e1, name in find_envs(s, ('figure', 'table')):
        body = s[b1:e0]
        caps = []
        has_caption = re.search(r'\\caption(\[[^\]]*\])?\{', body)
        if has_caption:
            if name == 'figure':
                ctx.fig += 1; num, word = ctx.fig, 'Obrázok'
            else:
                ctx.tab += 1; num, word = ctx.tab, 'Tabuľka'
            for l in re.findall(r'\\label\{([^}]*)\}', body):
                ctx.labels[l] = str(num)

            def cap(o, c, _w=word, _n=num):
                caps.append(1)
                return '\\caption{\\textbf{%s %d%s:} %s}' % (_w, _n, '' if len(caps) == 1 else chr(96 + len(caps)), c)
            body = replace_cmd(body, 'caption', 1, cap, opt=True)
        body = re.sub(r'\\label\{[^}]*\}', '', body)
        out.append(s[pos:b0]); out.append('\\begin{%s}%s\\end{%s}' % (name, body, name)); pos = e1
    out.append(s[pos:])
    return ''.join(out)


def resolve_refs(s: str, ctx: Ctx) -> str:
    def look(o, key):
        if key in ctx.labels:
            return ctx.labels[key].strip('()') if True else ''
        ctx.warn('unknown reference \\ref{%s}' % key)
        return '??'

    def eq(o, key):
        v = ctx.labels.get(key)
        if v is None:
            ctx.warn('unknown reference \\eqref{%s}' % key)
            return '(??)'
        return v if v.startswith('(') else '(' + v + ')'
    s = replace_cmd(s, 'eqref', 1, eq)
    for c in ('ref', 'autoref', 'cref', 'Cref'):
        s = replace_cmd(s, c, 1, look, star=True)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    return s


# ---------------------------------------------------------------- figures

def handle_graphics(s: str, ctx: Ctx) -> str:
    def width_of(o):
        if not o:
            return ''
        m = re.search(r'width\s*=\s*([\d.]*)\s*\\(linewidth|textwidth|columnwidth|hsize)', o)
        if m:
            f = float(m.group(1) or 1)
            return 'width=%.2f\\linewidth' % max(.1, min(1, f))
        m = re.search(r'(?<![a-z])(width|height)\s*=\s*([\d.]+)\s*(cm|mm|pt|in)', o)
        if m:
            cm = float(m.group(2)) * {'cm': 1, 'mm': .1, 'pt': .0351, 'in': 2.54}[m.group(3)]
            if m.group(1) == 'height':   # keep the printed height (≈ same size as in the PDF)
                return 'height=%.1fcm' % max(.5, min(22, cm))
            return 'width=%.2f\\linewidth' % max(.05, min(1, cm / 16))   # 16 cm ≈ A4 text width
        return ''

    def gfx(kind):
        def f(o, path):
            new = ctx.figure_handler(kind, path.strip())
            if not new:
                ctx.warn('missing image: %s' % path)
                return '\\textit{[chýbajúci obrázok]}'
            w = width_of(o)
            return '\\aoimgdone%s{%s}' % ('[' + w + ']' if w else '', new)
        return f
    # inline tikz pictures first (they may contain \includegraphics); decorative overlays are dropped.
    # Settings defined in the text before a picture (\def, \tdplotsetmaincoords, ...) are passed along.
    defs = []
    outside, k0 = [], 0
    for b0, b1, e0, e1, name in find_envs(s, ('tikzpicture', 'circuitikz')):
        outside.append(s[k0:b0]); k0 = e1
    outside = ''.join(outside) + s[k0:]
    for m in re.finditer(r'\\def\\[A-Za-z]+\{[^{}]*\}|\\tdplotsetmaincoords\{[^}]*\}\{[^}]*\}'
                         r'|\\pgfmathsetmacro\{?\\[A-Za-z]+\}?\{[^{}]*\}|\\colorlet\{[^}]*\}\{[^}]*\}', outside):
        defs.append(m.group(0))
    for m in re.finditer(r'\\(tikzset|tikzmath)(?=\{)', outside):
        g, _ = read_group(outside, m.end())
        if g is not None:
            defs.append('\\%s{%s}' % (m.group(1), g))
    prefix = '\n'.join(defs) + '\n' if defs else ''
    out, pos = [], 0
    for b0, b1, e0, e1, name in find_envs(s, ('tikzpicture', 'circuitikz')):
        out.append(s[pos:b0])
        pos = e1
        if 'overlay' in s[b1:b1 + 200].split('\n', 1)[0]:
            continue
        new = ctx.figure_handler('tikz', prefix + s[b0:e1])
        if new:
            out.append('\\aoimgdone{%s}' % new)
        else:
            ctx.warn('image: TikZ picture could not be converted')
            out.append('\\textit{[obrázok sa nepodarilo skonvertovať]}')
    out.append(s[pos:])
    s = ''.join(out)
    s = replace_cmd(s, 'includestandalone', 1, gfx('standalone'), opt=True)
    s = replace_cmd(s, 'includegraphics', 1, gfx('graphics'), opt=True, star=True)
    out = [s]
    return ''.join(out).replace('\\aoimgdone', '\\includegraphics')


# ---------------------------------------------------------------- text macros & cleanup

def text_macros(s: str) -> str:
    body = lambda o, n: '⟦B:%s⟧' % n.strip()
    for c in ('subbody', 'subody', 'podbody'):
        s = replace_cmd(s, c, 1, body)
    for c in ('subsubbody', 'subsubody', 'podpodbody'):
        s = map_math(s, lambda m, c=c: replace_cmd(m, c, 1, lambda o, n: '\\qquad\\textit{[%s\\,b]}' % n.strip(), opt=True))
        s = replace_cmd(s, c, 1, lambda o, n: '⟦b:%s⟧' % n.strip(), opt=True)
    s = map_text(s, lambda t: replace_cmd(t, 'fbox', 1, lambda o, a: fbox(a)))
    s = replace_cmd(s, 'uv', 1, lambda o, a: '„' + a + '“')
    s = re.sub(r"''(.+?)''", '„\\1“', s, flags=re.S) if False else s
    s = replace_cmd(s, 'paragraphAO', 1, lambda o, a: '\n\n\\textbf{' + a + '}\n\n')
    s = replace_cmd(s, 'textsl', 1, lambda o, a: '\\textit{' + a + '}')
    s = replace_cmd(s, 'makecell', 1, lambda o, a: re.sub(r'\\\\(\[[^\]]*\])?', ' ', a), opt=True)
    s = replace_cmd(s, 'texorpdfstring', 2, lambda o, a, b: a)
    # links written without a scheme in the sources (www.aosk.sk, someone@aosk.sk) would become relative
    s = replace_cmd(s, 'href', 2, lambda o, u, t: '\\href{%s}{%s}' % (fix_url(u), re.sub(r'\\url\{([^}]*)\}', r'\1', t)))
    s = replace_cmd(s, 'url', 1, lambda o, u: '\\href{%s}{%s}' % (fix_url(u), o or u) if o or fix_url(u) != u
                    else '\\url{%s}' % u, opt=True)   # \url[text]{..} is a custom 2026 macro
    for c in TEXT_TO_MATH:
        s = map_text(s, lambda t, c=c: re.sub(r'\\' + c + r'(?![A-Za-z])(\{[^{}]*\})?', lambda m: '\\(\\' + c + (m.group(1) or '') + '\\)', t))
    return s


def fix_url(u: str) -> str:
    u = u.strip()
    if re.match(r'^[\w.+-]+@[\w-]+\.[\w.]+$', u):
        return 'mailto:' + u
    if re.match(r'^www\.|^[\w-]+\.(sk|eu|com|org|cz|net)(/|$)', u):
        return 'https://' + u
    return u


def fbox(a: str) -> str:
    segs = split_math(a.strip())
    if len(segs) == 1 and segs[0][0]:
        m = segs[0][1]
        inner = re.sub(r'^(\$\$?|\\\(|\\\[)|(\$\$?|\\\)|\\\])$', '', m)
        return '\\(\\boxed{' + inner + '}\\)'
    return a


def drop_style(s: str) -> str:
    def t(x):
        for c in ('setlength', 'addtolength', 'colorlet'):
            x = replace_cmd(x, c, 2, lambda o, a, b: '', opt=True, star=True)
        for c in STYLE_DROP_1:
            x = replace_cmd(x, c, 1, lambda o, a: '', opt=True, star=True)
        x = re.sub(r'\\(' + '|'.join(STYLE_DROP_0) + r')(?![A-Za-z])\s?', '', x)
        x = re.sub(r'\\\\\s*\[[^\]]*\]', r'\\\\', x)
        x = re.sub(r'\\(enspace|quad|,|;|:|!)(?![A-Za-z])', ' ', x)
        x = re.sub(r'~', '\u00a0', x)
        x = re.sub(r'\\textendash\b\s?', '–', x)
        x = re.sub(r'\\textemdash\b\s?', '—', x)
        x = x.replace('"=', '-').replace('\\-', '')
        return x
    return map_text(s, t)


# ---------------------------------------------------------------- math protection & pandoc

def protect_math(s: str):
    store = []

    def put(m):
        store.append(m)
        return 'ZZM%04dZZ' % (len(store) - 1)
    return ''.join(put(t) if m else t for m, t in split_math(s)), store


def math_to_md(m: str) -> str:
    m = m.strip()
    disp = True
    if m.startswith('$$'):
        inner = m[2:-2]
    elif m.startswith('\\['):
        inner = m[2:-2]
    elif m.startswith('\\('):
        inner, disp = m[2:-2], False
    elif m.startswith('$'):
        inner, disp = m[1:-1], False
    else:  # unnumbered env like displaymath / math left over
        mm = re.match(r'\\begin\{([^}]*)\}(.*)\\end\{\1\}$', m, re.S)
        inner = mm.group(2) if mm else m
        disp = not (mm and mm.group(1) == 'math')
    inner = re.sub(r'\\label\{[^}]*\}', '', inner)
    inner = re.sub(r'(?<!\\)\$|\\\(|\\\)', '', inner)  # math delimiters nested inside math (source typos)
    inner = inner.replace('\\fbox{', '\\boxed{')
    inner = replace_cmd(inner, 'Aboxed', 1, lambda o, a: '\\boxed{' + a.replace('&', '') + '}')
    inner = re.sub(r'\n\s*\n', '\n', inner).strip()
    if inner.endswith('\\'):
        inner += ' '
    if disp:
        return '\n\n$$\n' + inner + '\n$$\n\n'
    return '$' + inner.replace('\n', ' ') + '$'


def math_shortcode(m: str) -> str:
    md = math_to_md(m)
    if md.startswith('\n'):
        return '{{< m block >}}' + md.strip().strip('$').strip() + '{{< /m >}}'
    return '{{< m >}}' + md[1:-1] + '{{< /m >}}'


def pandoc_md(tex: str) -> str:
    r = subprocess.run(['pandoc', '-f', 'latex', '-t', 'gfm+tex_math_dollars', '--wrap=none',
                        '--lua-filter', str(LUA)], input=tex, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr.strip()[:500])
    return r.stdout


def restore(md: str, store) -> str:
    md = re.sub(r'ZZ(?=ZZM\d{4}ZZ)', 'ZZ ', md)  # $a$$b$ would be read as display math
    # math inside raw HTML blocks (tables pandoc could not write as Markdown) goes through the {{< m >}} shortcode
    def in_html(m):
        return re.sub(r'ZZM(\d{4})ZZ', lambda k: math_shortcode(store[int(k.group(1))]), m.group(0))
    md = re.sub(r'<table.*?</table>', in_html, md, flags=re.S)
    md = re.sub(r'ZZM(\d{4})ZZ', lambda m: math_to_md(store[int(m.group(1))]), md)
    md = re.sub(r'⟦B:([^⟧]*)⟧', r'<span class="body">[\1 b]</span>', md)
    md = re.sub(r'⟦b:([^⟧]*)⟧', r'<span class="subbody">[\1 b]</span>', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'


def convert_block(tex: str, ctx: Ctx, already_stripped=False) -> str:
    """Full pipeline for one block. Numbering state lives in ctx (call in reading order)."""
    if not tex or not tex.strip():
        return ''
    s = tex if already_stripped else strip_comments(tex)
    s = normalise_envs(s)
    s = siunitx.expand(s, ctx.units)
    s = replace_cmd(s, 'widefrac', 2, lambda o, a, b: '\\frac{%s}{%s}' % (a, b), opt=True)
    s = number_equations(s, ctx)
    s = number_floats(s, ctx)
    s = handle_graphics(s, ctx)
    s = drop_definitions(s)
    s = text_macros(s)
    s = drop_style(s)
    return s  # refs are resolved later, once both blocks are numbered


def finish_block(s: str, ctx: Ctx) -> str:
    if not s:
        return ''
    s = resolve_refs(s, ctx)
    s = map_math(s, lambda m: re.sub(r'\\(nonumber|notag)\b', '', m))
    body, store = protect_math(s)
    try:
        md = pandoc_md(body)
    except RuntimeError as e:
        ctx.warn('pandoc failed: %s' % e)
        return '*[Text sa nepodarilo skonvertovať.]*\n'
    return restore(md, store)
