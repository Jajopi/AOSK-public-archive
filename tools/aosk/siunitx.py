"""Expand siunitx (\\SI, \\si, \\num, \\ang, ...) and the AO time/angle macros into plain KaTeX-compatible math."""
import re
from .latex import read_group, replace_cmd, split_math

PREFIXES = {'quecto': 'q', 'ronto': 'r', 'yocto': 'y', 'zepto': 'z', 'atto': 'a', 'femto': 'f', 'pico': 'p',
            'nano': 'n', 'micro': '\\mu ', 'milli': 'm', 'centi': 'c', 'deci': 'd', 'deca': 'da', 'deka': 'da',
            'hecto': 'h', 'kilo': 'k', 'mega': 'M', 'giga': 'G', 'tera': 'T', 'peta': 'P', 'exa': 'E',
            'zetta': 'Z', 'yotta': 'Y', 'ronna': 'R', 'quetta': 'Q'}
UNITS = {'meter': 'm', 'metre': 'm', 'second': 's', 'kilogram': 'kg', 'gram': 'g', 'ampere': 'A', 'kelvin': 'K',
         'mole': 'mol', 'candela': 'cd', 'hertz': 'Hz', 'newton': 'N', 'pascal': 'Pa', 'joule': 'J', 'watt': 'W',
         'coulomb': 'C', 'volt': 'V', 'ohm': '\\Omega', 'tesla': 'T', 'henry': 'H', 'lumen': 'lm', 'lux': 'lx',
         'becquerel': 'Bq', 'electronvolt': 'eV', 'minute': 'min', 'hour': 'h', 'day': 'd', 'liter': 'L',
         'litre': 'L', 'tonne': 't', 'astronomicalunit': 'au', 'radian': 'rad', 'steradian': 'sr', 'bar': 'bar',
         'dalton': 'Da', 'decibel': 'dB', 'barn': 'b', 'hectare': 'ha', 'siemens': 'S', 'farad': 'F',
         'weber': 'Wb', 'gray': 'Gy', 'sievert': 'Sv', 'katal': 'kat', 'neper': 'Np', 'bel': 'B',
         # abbreviations
         'm': 'm', 's': 's', 'g': 'g', 'K': 'K', 'J': 'J', 'W': 'W', 'N': 'N', 'Pa': 'Pa', 'Hz': 'Hz', 'eV': 'eV',
         'A': 'A', 'V': 'V', 'C': 'C', 'L': 'L', 'mol': 'mol', 'kg': 'kg', 'mg': 'mg', 'ug': '\\mu g',
         'km': 'km', 'cm': 'cm', 'mm': 'mm', 'um': '\\mu m', 'nm': 'nm', 'pm': 'pm', 'fm': 'fm',
         'ms': 'ms', 'us': '\\mu s', 'ns': 'ns', 'ps': 'ps', 'kJ': 'kJ', 'MJ': 'MJ', 'kW': 'kW', 'MW': 'MW',
         'GW': 'GW', 'kHz': 'kHz', 'MHz': 'MHz', 'GHz': 'GHz', 'THz': 'THz', 'kN': 'kN', 'kPa': 'kPa',
         'MPa': 'MPa', 'keV': 'keV', 'MeV': 'MeV', 'GeV': 'GeV', 'TeV': 'TeV', 'mA': 'mA', 'kV': 'kV',
         'mL': 'mL', 'ml': 'ml', 'mV': 'mV', 'kK': 'kK', 'kelvins': 'K', 'F': 'F', 'H': 'H', 'T': 'T', 'Wb': 'Wb', 'S': 'S'}
NOSPACE = {'degree': '^{\\circ}', 'arcminute': "'", 'arcsecond': "''", 'percent': '\\,\\%',
           'degreeCelsius': '\\,^{\\circ}\\mathrm{C}', 'celsius': '\\,^{\\circ}\\mathrm{C}'}
SPECIAL = {'angstrom': '\\text{Å}', 'Angstrom': '\\text{Å}', 'micro': '\\mu'}


def fmt_num(x: str) -> str:
    """siunitx number → math, decimal comma, exponent with \\cdot 10^{..}, digit grouping for 5+ digits."""
    x = x.strip()
    if not x:
        return ''
    if '\\pm' in x:
        return ' \\pm '.join(fmt_num(p) for p in x.split('\\pm'))
    for sep in ('x', '\\times'):
        if sep in x and re.fullmatch(r'[\d\s.,eE+\-]+(?:' + re.escape(sep) + r'[\d\s.,eE+\-]+)+', x):
            return ' \\times '.join(fmt_num(p) for p in x.split(sep))
    m = re.fullmatch(r'([+\-]?)\s*([\d\s.,]*?)\s*(?:[eE]\s*([+\-]?)\s*(\d+))?', x)
    if not m:
        return x  # free-form: leave as is
    sign, mant, esign, exp = m.groups()
    mant = re.sub(r'\s+', '', mant).replace('.', ',')
    if mant:
        ip, _, fp = mant.partition(',')
        if len(ip) >= 5:
            ip = re.sub(r'(?<=\d)(?=(\d{3})+$)', '\\\\,', ip)
        mant = ip + ('{,}' + fp if _ else '')
    out = sign + mant
    if exp is not None:
        e = (esign if esign == '-' else '') + exp
        out = (out + ' \\cdot ' if mant else sign) + '10^{' + e + '}'
    return out


class UnitTable:
    def __init__(self, custom=None):
        self.custom = dict(custom or {})

    def render(self, u: str, depth=0) -> str:
        """Unit string (\\kilo\\meter\\per\\second\\squared or literal text) → math."""
        if depth > 5:
            return u
        items = []  # [prefix, symbol, power, nospace]
        pending_prefix, per, pending_pow = '', False, None
        i = 0
        literal = []

        def flush_literal():
            if literal:
                txt = ''.join(literal)
                literal.clear()
                if txt.strip():
                    items.append(['', lit_to_math(txt), None, False, True])

        while i < len(u):
            m = re.match(r'\\([A-Za-z]+)', u[i:])
            if not m:
                literal.append(u[i]); i += 1
                continue
            name = m.group(1); i += m.end()
            if name in ('per',):
                flush_literal(); per = True; continue
            if name in ('squared', 'cubed'):
                flush_literal()
                if items:
                    items[-1][2] = ('-' if items[-1][2] == '-1' else '') + ('2' if name == 'squared' else '3')
                continue
            if name == 'tothe':
                g, j = read_group(u, i); i = j
                if items:
                    items[-1][2] = g
                continue
            if name in ('square', 'cubic'):
                pending_pow = '2' if name == 'square' else '3'; continue
            if name in PREFIXES and name != 'micro' or (name == 'micro' and u[i:i + 1] == '\\'):
                flush_literal(); pending_prefix += PREFIXES[name]; continue
            sym, nosp = None, False
            if name in self.custom:
                sym = self.render(self.custom[name], depth + 1)
                sym = sym
            elif name in NOSPACE:
                sym, nosp = NOSPACE[name], True
            elif name in SPECIAL:
                sym = SPECIAL[name]
            elif name in UNITS:
                sym = '\\mathrm{' + UNITS[name] + '}' if not UNITS[name].startswith('\\') else UNITS[name]
                if UNITS[name].startswith('\\mu '):
                    sym = '\\mu\\mathrm{' + UNITS[name][4:] + '}'
            if sym is None:  # unknown macro → keep raw (e.g. \cdot, \mathit{..}, \odot)
                literal.append(m.group(0)); continue
            flush_literal()
            if pending_prefix:
                if '\\mu' in pending_prefix:
                    sym = '\\mu' + sym
                elif sym.startswith('\\mathrm{'):
                    sym = '\\mathrm{' + pending_prefix + sym[len('\\mathrm{'):]
                else:
                    sym = '\\mathrm{' + pending_prefix + '}' + sym
            power = pending_pow
            if per:
                power = '-' + (power or '1')
            items.append([pending_prefix, sym, power, nosp, False])
            pending_prefix, per, pending_pow = '', False, None
        flush_literal()
        out = ''
        for k, (_, sym, power, nosp, lit) in enumerate(items):
            piece = sym if power is None else '{' + sym + '}^{' + power + '}'
            if k and not nosp and not lit and not items[k - 1][4]:
                out += '\\,'
            out += piece
        return out

    def first_nospace(self, u: str) -> bool:
        m = re.match(r'\s*\\([A-Za-z]+)', u)
        return bool(m) and m.group(1) in NOSPACE and len(re.findall(r'\\[A-Za-z]+', u)) == 1


ACCENTS = [(r'\\acute\{\\text\{\\i\}\}', 'í'), (r"\\'\{?\\i\}?", 'í'), (r'\\acute\{(\w)\}', lambda m: m.group(1) + '\u0301'),
           (r'\\check\{(\w)\}', lambda m: m.group(1) + '\u030c'), (r'\\v\{(\w)\}', lambda m: m.group(1) + '\u030c')]


def lit_to_math(t: str) -> str:
    """Literal unit text like 'W \\cdot m^{-2}' → letters at brace depth 0 upright."""
    import unicodedata
    for pat, rep in ACCENTS:
        t = re.sub(pat, rep, t)
    t = unicodedata.normalize('NFC', t)
    out, depth, i = [], 0, 0
    while i < len(t):
        c = t[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+|.)', t[i:]); out.append(m.group(0)); i += m.end(); continue
        if c == '{': depth += 1
        elif c == '}': depth -= 1
        if depth == 0 and (c.isalpha()):
            j = i
            while j < len(t) and t[j].isalpha(): j += 1
            out.append('\\mathrm{' + t[i:j] + '}'); i = j; continue
        out.append(c); i += 1
    return ''.join(out)


def fmt_ang(a: str) -> str:
    parts = a.split(';')
    if len(parts) == 1:
        return fmt_num(parts[0]) + '^{\\circ}'
    parts += [''] * (3 - len(parts))
    out = []
    for p, sym in zip(parts, ('^{\\circ}', "'", "''")):
        if p.strip():
            out.append(fmt_num(p) + sym)
    return '\\,'.join(out)


def fmt_hms(h, m, s, units=('h', 'min', 's'), sup=True):
    out = []
    for v, u in zip((h, m, s), units):
        if v is not None and str(v).strip():
            out.append(fmt_num(v) + ('^{\\mathrm{' + u + '}}' if sup else '\\,\\mathrm{' + u + '}'))
    return ('\\,' if sup else '\\;').join(out) or ''


def expand(s: str, units: UnitTable) -> str:
    """Expand siunitx/AO macros everywhere; results in text mode get wrapped in \\( \\)."""
    def in_math(seg, math):
        w = (lambda x: x) if math else (lambda x: '\\(' + x + '\\)')

        def si_full(o, n, u):
            n2, u2 = fmt_num(n), units.render(u)
            if units.first_nospace(u) or not n2:
                return w(n2 + u2)
            return w(n2 + '\\,' + u2)
        seg = replace_cmd(seg, 'SIrange', 3, lambda o, a, b, u: w(fmt_num(a) + '\\,' + units.render(u) + ' - ' + fmt_num(b) + '\\,' + units.render(u)), opt=True)
        seg = replace_cmd(seg, 'qtyrange', 3, lambda o, a, b, u: w(fmt_num(a) + ' - ' + fmt_num(b) + '\\,' + units.render(u)), opt=True)
        seg = replace_cmd(seg, 'SIspecial', 4, lambda o, a, b, c, u: w(fmt_num(a) + '^{+' + fmt_num(b) + '}_{-' + fmt_num(c) + '}\\,' + units.render(u)))
        seg = replace_cmd(seg, 'numrange', 2, lambda o, a, b: w(fmt_num(a) + ' - ' + fmt_num(b)), opt=True)
        for name in ('SI', 'qty'):
            seg = replace_cmd(seg, name, 2, si_full, opt=True)
        for name in ('si', 'unit'):
            seg = replace_cmd(seg, name, 1, lambda o, u: w(units.render(u)), opt=True)
        seg = replace_cmd(seg, 'num', 1, lambda o, n: w(fmt_num(n)), opt=True)
        seg = replace_cmd(seg, 'ang', 1, lambda o, a: w(fmt_ang(a)), opt=True)
        seg = replace_cmd(seg, 'angleh', 3, lambda o, h, m, x: w(fmt_hms(h, m, x)))
        seg = replace_cmd(seg, 'anglem', 2, lambda o, m, x: w(fmt_hms(None, m, x)))
        seg = replace_cmd(seg, 'angles', 1, lambda o, x: w(fmt_hms(None, None, x)))
        seg = replace_cmd(seg, 'anglehh', 1, lambda o, x: w(fmt_hms(x, None, None)))
        seg = replace_cmd(seg, 'anglemm', 1, lambda o, x: w(fmt_hms(None, x, None)))
        seg = replace_cmd(seg, 'angh', 1, lambda o, a: w(fmt_hms(*(a.split(';') + ['', '', ''])[:3])))
        seg = replace_cmd(seg, 'angm', 1, lambda o, a: w(fmt_hms(None, *(a.split(';') + ['', ''])[:2])))
        seg = replace_cmd(seg, 'angs', 1, lambda o, a: w(fmt_hms(None, None, a)))
        seg = replace_cmd(seg, 'cas', 3, lambda o, h, m, x: w(fmt_hms(h, m, x, sup=False)))
        return seg
    return ''.join(in_math(t, m) for m, t in split_math(s))


def parse_si_units(text: str) -> dict:
    """Collect \\DeclareSIUnit definitions (later ones win)."""
    out = {}
    for m in re.finditer(r'\\DeclareSIUnit(?:\[[^\]]*\])?\s*\{?\\([A-Za-z]+)\}?', text):
        g, _ = read_group(text, m.end())
        if g is not None:
            out[m.group(1)] = g
    return out
