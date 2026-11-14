"""Low-level LaTeX string utilities: comments, argument parsing, math/text splitting."""
import re

MATH_ENVS = ('equation', 'equation*', 'align', 'align*', 'gather', 'gather*', 'multline', 'multline*',
             'eqnarray', 'eqnarray*', 'flalign', 'flalign*', 'alignat', 'alignat*', 'displaymath', 'math')


def strip_comments(s: str) -> str:
    """Remove %-comments (keeps escaped \\%). A comment also swallows the newline+indent, like TeX."""
    out = []
    for line in s.split('\n'):
        m = re.search(r'(?<!\\)(?:\\\\)*%', line)
        if m:
            out.append(line[:m.start() + len(m.group(0)) - 1] + '\x00')  # \x00 = "no newline here"
        else:
            out.append(line)
    s = '\n'.join(out)
    return re.sub(r'\x00\n[ \t]*', '', s).replace('\x00', '')


def skip_ws(s: str, i: int) -> int:
    while i < len(s) and s[i] in ' \t\n':
        i += 1
    return i


def read_group(s: str, i: int, open_='{', close='}'):
    """s[i] must be `open_` (after optional whitespace). Returns (content, index after group) or (None, i)."""
    j = skip_ws(s, i)
    if j >= len(s) or s[j] != open_:
        return None, i
    depth, k = 0, j
    while k < len(s):
        c = s[k]
        if c == '\\':
            k += 2
            continue
        if c == open_:
            depth += 1
        elif c == close:
            depth -= 1
            if depth == 0:
                return s[j + 1:k], k + 1
        elif open_ == '[' and c == '{':  # skip braces inside optional args
            _, k2 = read_group(s, k)
            k = k2
            continue
        k += 1
    return None, i


def read_token_arg(s: str, i: int):
    """Mandatory argument: braced group or a single token (\\cmd or char)."""
    g, j = read_group(s, i)
    if g is not None:
        return g, j
    j = skip_ws(s, i)
    if j < len(s) and s[j] == '\\':
        m = re.match(r'\\([A-Za-z]+|.)', s[j:])
        return m.group(0), j + len(m.group(0))
    if j < len(s):
        return s[j], j + 1
    return '', j


def replace_cmd(s: str, name: str, nargs: int, fn, opt: bool = False, star: bool = False) -> str:
    """Replace every \\name[opt]{a1}...{an} with fn(opt, a1, ..., an). fn returns replacement text."""
    pat = re.compile(r'\\' + re.escape(name) + (r'\*?' if star else '') + r'(?![A-Za-z])')
    out, pos = [], 0
    while True:
        m = pat.search(s, pos)
        if not m:
            break
        j = m.end()
        o = None
        if opt:
            o, j2 = read_group(s, j, '[', ']')
            if o is not None:
                j = j2
        args = []
        ok = True
        for _ in range(nargs):
            a, j2 = read_group(s, j)
            if a is None:
                a, j2 = read_token_arg(s, j)
                if a == '':
                    ok = False
                    break
            args.append(a)
            j = j2
        if not ok:
            out.append(s[pos:m.end()])
            pos = m.end()
            continue
        out.append(s[pos:m.start()])
        out.append(fn(o, *args))
        pos = j
    out.append(s[pos:])
    return ''.join(out)


def find_envs(s: str, names):
    """Yield (start, body_start, body_end, end, name) of top-level occurrences of the given environments."""
    pat = re.compile(r'\\(begin|end)\{([^}]+)\}')
    stack = []
    for m in pat.finditer(s):
        kind, name = m.group(1), m.group(2)
        if kind == 'begin':
            stack.append((name, m.start(), m.end()))
        else:
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][0] == name:
                    bname, bstart, bend = stack[k]
                    del stack[k:]
                    if name in names and not any(st[0] in names for st in stack):
                        yield bstart, bend, m.start(), m.end(), name
                    break


def split_math(s: str):
    """Split into [(is_math, text)], math segments include their delimiters."""
    segs, i, buf = [], 0, []
    env_pat = re.compile(r'\\begin\{(' + '|'.join(re.escape(e) for e in MATH_ENVS) + r')\}')
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            nxt = s[i + 1]
            if nxt in '([':
                close = '\\)' if nxt == '(' else '\\]'
                j = s.find(close, i + 2)
                if j >= 0:
                    segs.append((False, ''.join(buf))); buf = []
                    segs.append((True, s[i:j + 2])); i = j + 2
                    continue
            m = env_pat.match(s, i)
            if m:
                endtok = '\\end{' + m.group(1) + '}'
                j = s.find(endtok, m.end())
                if j >= 0:
                    segs.append((False, ''.join(buf))); buf = []
                    segs.append((True, s[i:j + len(endtok)])); i = j + len(endtok)
                    continue
            buf.append(s[i:i + 2]); i += 2
            continue
        if c == '$':
            dbl = s.startswith('$$', i)
            d = '$$' if dbl else '$'
            j = i + len(d)
            while True:
                j = s.find(d, j)
                if j < 0 or s[j - 1] != '\\':
                    break
                j += 1
            if j >= 0:
                segs.append((False, ''.join(buf))); buf = []
                segs.append((True, s[i:j + len(d)])); i = j + len(d)
                continue
        buf.append(c); i += 1
    segs.append((False, ''.join(buf)))
    return [x for x in segs if x[1]]


def map_text(s: str, fn) -> str:
    """Apply fn only to the non-math parts."""
    return ''.join(t if m else fn(t) for m, t in split_math(s))


def map_math(s: str, fn) -> str:
    return ''.join(fn(t) if m else t for m, t in split_math(s))


def split_rows(body: str):
    """Split an align-like body on top-level \\\\ (ignores nested environments and braces)."""
    rows, depth, envdepth, cur, i = [], 0, 0, [], 0
    while i < len(body):
        if body.startswith('\\begin{', i):
            envdepth += 1
        elif body.startswith('\\end{', i):
            envdepth -= 1
        c = body[i]
        if c == '\\' and body.startswith('\\\\', i) and depth == 0 and envdepth == 0:
            i += 2
            sp = re.match(r'\s*\[[^\]]*\]', body[i:])  # \\[2mm]
            if sp:
                i += sp.end()
            rows.append(''.join(cur)); cur = []
            continue
        if c == '\\':
            cur.append(body[i:i + 2]); i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        cur.append(c); i += 1
    rows.append(''.join(cur))
    if len(rows) > 1 and not rows[-1].strip():
        rows.pop()
    return rows
