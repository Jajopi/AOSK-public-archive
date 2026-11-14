"""Source layouts. Each adapter turns one directory in sources/ into a list of Problems + extra texts.

Which problems exist (and their order/labels) is taken from the yearbook (ročenka): it contains
exactly the problems that were used in competition rounds and published.
To support a new Overleaf layout, add an adapter class and register it in `detect()`.
"""
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from .latex import strip_comments, read_group, replace_cmd

ROUND_NAMES = {'DK': 'Domáce kolo', 'RK': 'Regionálne kolo', 'CK': 'Celoštátne kolo'}
TYPE_LETTER = {'teoria': 'T', 'datovka': 'D', 'prakticka': 'P'}
TYPE_NAMES = {'teoria': 'Teória', 'datovka': 'Dátová analýza', 'prakticka': 'Praktická úloha'}


@dataclass
class Problem:
    year: int
    round: str              # DK / RK / CK
    category: str           # ZŠ / SŠ
    type: str               # teoria / datovka / prakticka
    order: int              # 1-based order within (year, round, category, type)
    title: str
    statement: str          # raw LaTeX
    solution: str           # raw LaTeX ('' = missing)
    src: str                # path relative to the source dir (for reference)
    base_dirs: list         # dirs used to resolve relative image paths (first = year root)
    authors: list = field(default_factory=list)
    points: str = ''
    comment: str = ''
    topics: list = field(default_factory=list)
    label: str = ''         # e.g. T3; ZAO uses the original problem number
    collection: str = ''    # 'ZAO' for problems from the collection book

    @property
    def cat_ascii(self):
        return {'ZŠ': 'zs', 'SŠ': 'ss'}[self.category]

    @property
    def slug(self):
        return ('%s-%s-%s-%s' % (self.round.lower(), self.cat_ascii, slugify(self.label), slugify(self.title)))[:80].rstrip('-')


@dataclass
class Source:
    name: str
    root: Path
    problems: list
    units_text: str               # text containing \DeclareSIUnit definitions
    tikz_preamble: str            # preamble used to compile inline tikzpicture environments
    intro: dict = field(default_factory=dict)       # year -> raw LaTeX of the yearbook introduction
    constants: dict = field(default_factory=dict)   # key ('SŠ'/'ZŠ'/'') -> raw LaTeX
    notes: list = field(default_factory=list)


def slugify(s: str) -> str:
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-') or 'uloha'


def read(p: Path) -> str:
    return p.read_text(encoding='utf-8', errors='replace')


def clean_meta(s: str) -> str:
    """Metadata text (title, names) → plain text."""
    s = strip_comments(s or '')
    s = replace_cmd(s, 'texorpdfstring', 2, lambda o, a, b: b)
    s = replace_cmd(s, 'includegraphics', 1, lambda o, a: '', opt=True)
    s = s.replace('\\&', ',')
    s = s.replace('"=', '-').replace("''", '"').replace('``', '"').replace('~', ' ')
    s = replace_cmd(s, 'uv', 1, lambda o, a: '„' + a + '“')
    s = re.sub(r'\\(textit|textbf|emph|textrm|text|mathrm)\{([^{}]*)\}', r'\2', s)
    s = re.sub(r'\\[A-Za-z]+\*?', '', s)
    s = re.sub(r'[{}$]', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def names(s: str) -> list:
    s = clean_meta(s)
    if not s or s.upper() in ('MENO', 'TODO', '??', '-', 'AUTOR'):
        return []
    return [x.strip() for x in re.split(r',| a |;|&', s) if x.strip()]


def norm_type(t: str) -> str:
    t = clean_meta(t).lower()
    if t.startswith('d'):
        return 'datovka'
    if t.startswith('p'):
        return 'prakticka'
    return 'teoria'


def cmd_args(text: str, name: str, n: int):
    """Arguments of the first \\name{..}{..} (comments already stripped)."""
    m = re.search(r'\\' + name + r'(?![A-Za-z])', text)
    if not m:
        return None
    args, j = [], m.end()
    for _ in range(n):
        g, j2 = read_group(text, j)
        if g is None:
            break
        args.append(g)
        j = j2
    return args


def block_between(text, start_re, end_re):
    m = re.search(start_re, text, re.S)
    if not m:
        return ''
    e = re.search(end_re, text[m.end():], re.S)
    return text[m.end(): m.end() + e.start()] if e else text[m.end():]


# ------------------------------------------------------------------ yearbook manifest

def parse_yearbook(text: str, include_cmds, list_dir=None):
    """Return [(round, category, type, relpath)] for the problems of the 'Zadania' part, in order."""
    text = strip_comments(text)
    tok = re.compile(r'\\(part|chapter|kolo|' + '|'.join(include_cmds) + r')(\[[^\]]*\])?\{([^}]*)\}')
    in_part, rnd, cat, typ, out = False, None, None, None, []
    for m in tok.finditer(text):
        cmd, arg = m.group(1), m.group(3).strip()
        if cmd == 'part':
            if in_part:
                break
            in_part = arg.lower().startswith('zadani')
        elif not in_part:
            continue
        elif cmd == 'chapter':
            cat = 'ZŠ' if 'ZŠ' in arg else 'SŠ'
            typ = 'datovka' if 'Dátov' in arg else 'prakticka' if 'Praktick' in arg else 'teoria'
        elif cmd == 'kolo':
            rnd = arg
        elif cmd == 'loadAllPriklady' and list_dir:
            for p in list_dir(arg):
                out.append((rnd, cat, typ, p))
        else:
            out.append((rnd, cat, typ, arg if arg.endswith('.tex') else arg + '.tex'))
    return out


def number(problems):
    seen = {}
    for p in problems:
        k = (p.year, p.round, p.category, p.type)
        seen[k] = seen.get(k, 0) + 1
        p.order = seen[k]
        p.label = p.label or '%s%d' % (TYPE_LETTER[p.type], p.order)
    return problems


# ------------------------------------------------------------------ 2024 (catchfilebetweentags)

class Layout2024:
    """AO 2024: problems are single files with %<*uvod>/%<*zadanie>/%<*riesenie> tags; yearbook loads them."""

    @staticmethod
    def match(root: Path):
        return (root / 'config.tex').exists() and (root / 'macros.tex').exists()

    def load(self, root: Path, year: int) -> Source:
        yb = next(iter(sorted(root.glob('*[Rr]ocenka*.tex'))))

        def list_dir(d):
            return sorted(str(p.relative_to(root)) for p in (root / d).glob('*.tex'))
        probs = []
        for rnd, cat, typ, rel in parse_yearbook(read(yb), ['loadPrikladRocenka', 'loadAllPriklady'], list_dir):
            raw = read(root / rel)
            tag = lambda t: block_between(raw, r'%<\*' + t + '>', r'%</' + t + '>')
            meta = strip_comments(tag('uvod'))
            a = cmd_args(meta, 'AOpriklad', 3) or ['', Path(rel).stem, '']
            stmt = tag('zadanie') + '\n\n' + tag('intermezzoZ') + '\n\n' + tag('post')
            probs.append(Problem(year, rnd, cat, typ, 0, clean_meta(a[1]), stmt, tag('riesenie'), rel,
                                 [root, (root / rel).parent], authors=names(a[2]),
                                 points=clean_meta((cmd_args(meta, 'body', 1) or [''])[0])))
        consts = read(root / 'konstanty-ALL.tex') if (root / 'konstanty-ALL.tex').exists() else ''
        consts = block_between(consts, r'%<\*konstanty>', r'%</konstanty>') or consts
        return Source(str(year), root, number(probs), read(root / 'macros.tex'),
                      '\\newtoks\\kde\\kde{samostatne}\n\\input{config}\n\\input{macros}',
                      intro={year: read(root / 'rocenka-uvod.tex')} if (root / 'rocenka-uvod.tex').exists() else {},
                      constants={'': consts})


# ------------------------------------------------------------------ 2025 (subfiles)

class Layout2025:
    """AO 2025: one directory per problem with 00-zadanie.tex (metadata + statement) and 01-riesenie.tex."""

    @staticmethod
    def match(root: Path):
        return (root / '99-background' / '00-main.tex').exists()

    def load(self, root: Path, year: int) -> Source:
        bg = root / '99-background'
        yb = bg / 'kompilaty' / '0-ROCENKA' / 'rocenka-kompilat.tex'
        probs = []
        for rnd, cat, typ, rel in parse_yearbook(read(yb), ['subfile']):
            f = root / rel
            t = strip_comments(read(f))
            meta = t.split('\\zadanie', 1)[0]
            a = cmd_args(meta, 'AOpriklad', 9) or ['', f.parent.name, '', '', '', '', '', '', '']
            m = re.search(r'\\zadanie\{\\the\\kde\}(\{[^}]*\})?(.*?)\\riesenie\{\\the\\kde\}\s*\{([^}]*)\}', t, re.S)
            stmt, sol = (m.group(2), '') if m else (block_between(t, r'\\zadanie\{[^}]*\}', r'\\end\{document\}'), '')
            if m and (f.parent / m.group(3).strip()).exists():
                rt = strip_comments(read(f.parent / m.group(3).strip()))
                body = block_between(rt, r'\\begin\{document\}', r'\\end\{document\}') or rt
                body = re.sub(r'\\ifthenelse\{\\equal\{\\the\\kde\}\{riesenie\}\}\{.*?\\label\{hlavicka\}\s*\}\{\}', '', body, flags=re.S)
                sol = body
            probs.append(Problem(year, rnd, cat, typ, 0, clean_meta(a[1]), stmt, sol, rel, [root, f.parent],
                                 authors=names(a[2]),
                                 points=clean_meta((cmd_args(meta, 'body', 1) or [''])[0]),
                                 comment=komentar(meta)))
        consts = {k: read(root / f'konstanty-{s}.tex') for k, s in (('SŠ', 'SS'), ('ZŠ', 'ZS')) if (root / f'konstanty-{s}.tex').exists()}
        uvod = bg / 'kompilaty' / '0-ROCENKA' / 'rocenka-uvod.tex'
        return Source(str(year), root, number(probs), read(bg / 'important' / '02-definitions.tex'),
                      '\n'.join('\\input{99-background/important/%s}' % n for n in ('01-packages', '02-definitions', '05-macros')),
                      intro={year: read(uvod)} if uvod.exists() else {}, constants=consts)


def komentar(meta: str) -> str:
    a = cmd_args(meta, 'komentar', 1)
    c = (a or [''])[0].strip()
    return '' if not c or 'Krátky komentár autora' in c else c


# ------------------------------------------------------------------ 2026+ (standalone + taggedblock)

class Layout2026:
    """AO 2026 (and later years copying it): one file per problem, taggedblock{zadanie|intermezzo|riesenie}."""

    @staticmethod
    def match(root: Path):
        return (root / 'background' / '.global').is_dir()

    def load(self, root: Path, year: int) -> Source:
        yb = next(iter(sorted((root / 'rocenka').glob('*.tex'), key=lambda p: (not p.name.upper().startswith('.ROC'), p.name))))
        probs = []
        for rnd, cat, typ, rel in parse_yearbook(read(yb), ['input']):
            f = root / rel
            if not f.exists():
                continue
            t = strip_comments(read(f))
            if 'taggedblock' not in t:
                continue
            blk = lambda n: block_between(t, r'\\begin\{taggedblock\}\{' + n + r'\}', r'\\end\{taggedblock\}')
            meta = t.split('\\begin{taggedblock}', 1)[0]
            a = cmd_args(meta, 'AOpriklad', 9) or ['', f.stem, '', '', '', '', '', '', '']
            probs.append(Problem(year, rnd, cat, typ, 0, clean_meta(a[1]), blk('zadanie') + '\n\n' + blk('intermezzo'),
                                 blk('riesenie'), rel, [root, f.parent], authors=names(a[2]),
                                 points=clean_meta((cmd_args(meta, 'body', 1) or [''])[0]), comment=komentar(meta)))
        consts = {k: read(root / f'konstanty-{s}.tex') for k, s in (('SŠ', 'SS'), ('ZŠ', 'ZS')) if (root / f'konstanty-{s}.tex').exists()}
        uvod = root / 'rocenka' / 'uvod.tex'
        return Source(str(year), root, number(probs), read(root / 'background' / '.global' / '02-definitions.tex'),
                      '\\input{background/.main/main-05-kreslenie}',
                      intro={year: read(uvod)} if uvod.exists() else {}, constants=consts)


# ------------------------------------------------------------------ ZAO (collection book 2007–2023)

ZAO_TOPICS = {'NebMech': 'Nebeská mechanika', 'GmtrCas': 'Geometria a čas', 'Sferika': 'Sférická astronómia',
              'FotoSpek': 'Fotometria a spektroskopia', 'OptikDek': 'Optika a detektory',
              'FyzHaP': 'Fyzika hviezd a planét', 'Kozmo': 'Kozmológia', 'Rozsiahle': 'Rozsiahle príklady',
              'Dodovky': None, 'Prakticke': None}


class LayoutZAO:
    """Zbierka AO: problems grouped by topic; statements in I_Zadania, solutions in II_Riesenia (same titles)."""

    @staticmethod
    def match(root: Path):
        return (root / 'I_Zadania').is_dir() and (root / 'II_Riesenia').is_dir()

    TITLE = re.compile(r'A[O0]\s*(\d{4}),?\s*(?:úloha\s*(\d+)\s*)?(?:[-–,]\s*)?(.*)', re.S)

    def split(self, text, level):
        text = strip_comments(re.sub(r'\\begin\{comment\}.*?\\end\{comment\}', '', text, flags=re.S))
        pat = re.compile(r'\\' + level + r'(?:AutorNewline|Autor)?\{')
        parts, ms = [], list(pat.finditer(text))
        for i, m in enumerate(ms):
            title, j = read_group(text, m.end() - 1)
            author = ''
            if 'Autor' in m.group(0):
                author, j = read_group(text, j)
            end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
            body = text[j:end]
            body = re.split(r'\\section\{', body)[0]
            parts.append((title, author or '', body))
        return parts

    def key(self, title):
        m = self.TITLE.search(title)
        return (int(m.group(1)), m.group(2) or m.group(3).strip()) if m else title.strip()

    def load(self, root: Path, year=None) -> Source:
        probs, notes = [], []
        for zf in sorted((root / 'I_Zadania').glob('*/*.tex')):
            if 'main' in zf.name:
                continue
            rf = root / 'II_Riesenia' / zf.relative_to(root / 'I_Zadania')
            topic_key = zf.parent.name.split('_', 1)[1]
            topic = ZAO_TOPICS.get(topic_key)
            if topic_key == 'Dodovky':
                y = int(re.search(r'(\d{4})', zf.name).group(1))
                z = self.split(read(zf), 'section')
                r = self.split(read(rf), 'section') if rf.exists() else []
                for (title, author, body), sol in zip(z, r + [None] * len(z)):
                    name = re.sub(r'^\s*A[O0]\s*\d{4},?\s*', '', clean_meta(title))
                    probs.append(Problem(y, 'CK', 'SŠ', 'datovka', 0, name or 'Dátová analýza', body,
                                         sol[2] if sol else '', str(zf.relative_to(root)), [root, root / 'images'],
                                         collection='ZAO', label='D1'))
                continue
            m = re.match(r'\d+_(ZS|SS)_(DK|FI)', zf.stem)
            cat, rnd = ('ZŠ' if m.group(1) == 'ZS' else 'SŠ'), ('DK' if m.group(2) == 'DK' else 'CK')
            sols = {self.key(t): b for t, a, b in (self.split(read(rf), 'subsection') if rf.exists() else [])}
            for title, author, body in self.split(read(zf), 'subsection'):
                k = self.key(title)
                tm = self.TITLE.search(clean_meta(title))
                if not tm or not (tm.group(2) or tm.group(3)):
                    notes.append('ZAO: unrecognised title "%s" in %s' % (clean_meta(title), zf.name))
                    continue
                y, n, name = int(tm.group(1)), tm.group(2) or '', (tm.group(3) or '').strip()
                name = re.sub(r'^(A[O0]\s*\d{4}\s*(,\s*úloha\s*\d+)?\s*[-–,]?\s*)+', '', name).strip()
                if not n:
                    n = str(90 + sum(1 for q in probs if q.year == y and q.round == rnd and q.category == cat and q.label.startswith('Ú9')))
                typ = 'prakticka' if topic_key == 'Prakticke' else 'teoria'
                probs.append(Problem(y, rnd, cat, typ, 0, name or 'Úloha %s' % n, body, sols.get(k, ''),
                                     str(zf.relative_to(root)), [root, root / 'images'], authors=names(author),
                                     topics=[topic] if topic else [], collection='ZAO', label='Ú' + n))
        # same problem used in several categories is listed once per category; order by original number
        probs.sort(key=lambda p: (p.year, p.round, p.category, int(re.sub(r'\D', '', p.label) or 0)))
        for p in probs:
            p.order = int(re.sub(r'\D', '', p.label) or 0)
        intro = read(root / 'Uvod.tex') if (root / 'Uvod.tex').exists() else ''
        return Source('ZAO', root, probs, read(root / '_macros_.tex'), '\\providecommand{\\chaptermark}[1]{}\\providecommand{\\chapter}[1]{}\n\\input{_config_}\n\\input{_macros_}',
                      intro={'ZAO': intro}, constants={'': read(root / 'ZoznamKonstant.tex')}, notes=notes)


LAYOUTS = [LayoutZAO, Layout2025, Layout2026, Layout2024]


def detect(root: Path):
    for L in LAYOUTS:
        if L.match(root):
            return L()
    return None
