#!/usr/bin/env python3
"""Import every source in sources/ and (re)generate site/content/ for Hugo.

Usage:  python3 tools/build.py [--only 2026] [--jobs 4]

Each directory (or .zip) in sources/ is one Overleaf project export. The layout is detected
automatically (see tools/aosk/layouts.py). Generated files are overwritten on every run.
"""
import argparse
import json
import re
import shutil
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aosk import layouts, siunitx, transform  # noqa: E402
from aosk.figures import FigureHandler  # noqa: E402
from aosk.layouts import ROUND_NAMES, TYPE_NAMES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / 'sources'
CACHE = REPO / '.cache'
CONTENT = REPO / 'site' / 'content'
DATA = REPO / 'site' / 'data'
TAGS_FILE = REPO / 'tools' / 'tags.yaml'
ROUND_ORDER = {'DK': 0, 'RK': 1, 'CK': 2}
CAT_ORDER = {'ZŠ': 0, 'SŠ': 1}
TYPE_ORDER = {'teoria': 0, 'datovka': 1, 'prakticka': 2}
UNCATEGORIZED = 'Nezaradené'   # tag of problems without any topic (see tools/tags.yaml)


def find_sources():
    """Yield (name, path, year) for every source project; zip files are unpacked into .cache/sources."""
    seen = set()
    for p in sorted(SOURCES.iterdir()):
        if p.name.startswith('.'):
            continue
        if p.suffix.lower() == '.zip':
            if (SOURCES / p.stem).is_dir():
                continue  # an unpacked copy exists and wins
            dest = CACHE / 'sources' / p.stem
            stamp = dest / '.unpacked-from'
            if not stamp.exists() or stamp.read_text() != str(p.stat().st_mtime):
                shutil.rmtree(dest, ignore_errors=True)
                dest.mkdir(parents=True)
                with zipfile.ZipFile(p) as z:
                    z.extractall(dest)
                stamp.write_text(str(p.stat().st_mtime))
            p = dest
        if p.is_dir() and p.name not in seen:
            seen.add(p.name)
            m = re.search(r'(\d{4})', p.name)
            yield p.name, p, int(m.group(1)) if m else None


def yaml_dump(d):
    return yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000)


def write_page(path: Path, front: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('---\n' + yaml_dump(front) + '---\n\n' + body, encoding='utf-8')


def convert_text(tex, units, warn_prefix, report, figs=None):
    """Convert a free text (introduction, constants) without figures."""
    ctx = transform.Ctx(units, figs or (lambda k, a: None), warn_prefix)
    s = transform.convert_block(tex, ctx)
    md = transform.finish_block(s, ctx)
    report.extend('%s: %s' % (warn_prefix, w) for w in ctx.warnings)
    return md


def document_body(tex: str) -> str:
    m = re.search(r'\\begin\{document\}(.*)\\end\{document\}', tex, re.S)
    return m.group(1) if m else tex


def mark_inverted(md: str, names) -> str:
    """Give line drawings the class "invert" (inverted by CSS on the dark site, not in print)."""
    for n in names:
        md = md.replace('<img src="%s"' % n, '<img class="invert" src="%s"' % n)
        md = re.sub(r'!\[([^\]]*)\]\(%s\)(\{[^}]*\})?' % re.escape(n), '<img class="invert" src="%s" alt="obrázok">' % n, md)
    return md


def process_problem(p, src, units, tags, report):
    pid = '%d/%s' % (p.year, p.slug)
    bundle = CONTENT / str(p.year) / p.slug
    shutil.rmtree(bundle, ignore_errors=True)
    warnings = []
    figs = FigureHandler(src.root, p.base_dirs, bundle, CACHE / 'figures', src.tikz_preamble, warnings.append)
    ctx = transform.Ctx(units, figs, pid)
    a = transform.convert_block(p.statement, ctx)
    b = transform.convert_block(p.solution, ctx) if p.solution.strip() else ''
    stmt, sol = transform.finish_block(a, ctx), transform.finish_block(b, ctx)
    stmt, sol = mark_inverted(stmt, figs.invert), mark_inverted(sol, figs.invert)
    comment = convert_text(p.comment, units, pid, warnings) if p.comment else ''
    warnings += ctx.warnings
    extra = tags.get(pid, [])
    front = {
        'title': p.title,
        'year': p.year,
        'round': p.round,
        'roundName': ROUND_NAMES[p.round],
        'category': p.category,
        'type': p.type,
        'typeName': TYPE_NAMES[p.type],
        'label': p.label,
        'weight': (CAT_ORDER[p.category] * 3000 + ROUND_ORDER[p.round] * 1000 + TYPE_ORDER[p.type] * 100 + p.order),
        'points': p.points or None,
        'authors': p.authors,
        'hasSolution': bool(sol.strip()),
        'source': '%s:%s' % (src.name, p.src),
        'years': [str(p.year)],
        'rounds': [ROUND_NAMES[p.round]],
        'categories': [p.category],
        'types': [TYPE_NAMES[p.type]],
        'topics': sorted(set(p.topics + extra)) or [UNCATEGORIZED],
    }
    if p.collection:
        front['collection'] = p.collection
    if warnings:
        front['warnings'] = warnings
    body = ['## Zadanie\n', stmt]
    if sol.strip():
        body += ['<details class="solution">\n<summary>Riešenie</summary>\n', sol, '</details>\n']
    else:
        body += ['<p class="missing">Riešenie tejto úlohy sa nezachovalo.</p>\n']
    if comment.strip():
        body += ['## Komentár autora\n', comment]
    write_page(bundle / 'index.md', {k: v for k, v in front.items() if v not in (None, [], '')}, '\n'.join(body))
    report.extend('%s: %s' % (pid, w) for w in warnings)
    # private fields for the overview page (not written into the page)
    front['_slug'] = p.slug
    front['_sig'] = signature(p.statement)
    text = stmt + sol
    front['_figref'] = bool(re.search(r'\bobr(\.|ázk|ázok)', text, re.I)) and '<img' not in text and '![' not in text
    return front


def signature(tex: str) -> str:
    """Normalised start of a statement – equal signatures = the same problem used twice."""
    t = re.sub(r'\\[A-Za-z]+|[^\w]|\d', '', tex.lower())
    return t[:250] if len(t) > 80 else ''


def problem_issues(f):
    out = []
    w = ' '.join(f.get('warnings', []))
    if not f['hasSolution']:
        out.append('bez riešenia')
    if 'image' in w:
        out.append('chýba obrázok alebo sa nepodarilo skonvertovať')
    if f['_figref']:
        out.append('text spomína obrázok, ktorý v zdroji nie je')
    if 'unknown reference' in w:
        out.append('odkaz na neexistujúci obrázok/rovnicu/tabuľku (??)')
    if 'pandoc failed' in w:
        out.append('text sa nepodarilo skonvertovať')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', help='process only sources whose name contains this')
    ap.add_argument('--jobs', type=int, default=4)
    args = ap.parse_args()

    tags = {k: v for k, v in (yaml.safe_load(TAGS_FILE.read_text()) or {}).items()} if TAGS_FILE.exists() else {}
    tags = tags.get('problems', {}) or {}
    years, report, summary = {}, [], {}
    for name, root, year in find_sources():
        if args.only and args.only not in name:
            continue
        L = layouts.detect(root)
        if not L:
            print('! %s: unknown project layout, skipping' % name)
            continue
        src = L.load(root, year)
        units = siunitx.UnitTable(siunitx.parse_si_units(src.units_text))
        report.extend('%s: %s' % (name, n) for n in src.notes)
        # unique slugs inside a year
        seen = {}
        for p in src.problems:
            base, k = p.slug, 1
            while (p.year, p.slug) in seen:
                k += 1
                p.title_suffix = k
                p.label = p.label + chr(96 + k) if k == 2 else p.label[:-1] + chr(96 + k)
            seen[(p.year, p.slug)] = 1
        for y in sorted({p.year for p in src.problems}):
            shutil.rmtree(CONTENT / str(y), ignore_errors=True)
        print('%s: %s, %d problems' % (name, type(L).__name__, len(src.problems)))
        with ThreadPoolExecutor(args.jobs) as ex:
            fronts = list(ex.map(lambda p: process_problem(p, src, units, tags, report), src.problems))
        for p, f in zip(src.problems, fronts):
            years.setdefault(p.year, {'sources': set(), 'problems': []})
            years[p.year]['sources'].add(name)
            years[p.year]['problems'].append(f)
        # texts: introduction + constants
        for key, tex in src.intro.items():
            if tex.strip():
                summary.setdefault('intro', {})[str(key)] = convert_text(document_body(tex), units, '%s intro' % name, report)
        for cat, tex in src.constants.items():
            if tex.strip():
                cdir = CACHE / 'const' / ('%s-%s' % (name, cat or 'all'))
                shutil.rmtree(cdir, ignore_errors=True)
                figs = FigureHandler(src.root, [src.root], cdir, CACHE / 'figures', src.tikz_preamble, report.append)
                md = convert_text(document_body(tex), units, '%s constants' % name, report, figs)
                md = mark_inverted(md, figs.invert)
                summary.setdefault('constants', {})['%s|%s' % (name, cat)] = md
        summary.setdefault('sources', {})[name] = {'layout': type(L).__name__, 'years': sorted({p.year for p in src.problems})}

    if not years:
        print('no sources found in sources/ – nothing changed')
        return
    write_year_pages(years, summary)
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / 'report.json').write_text(json.dumps(sorted(set(report)), ensure_ascii=False, indent=1))
    print('done: %d years, %d problems, %d warnings (site/data/report.json)' %
          (len(years), sum(len(v['problems']) for v in years.values()), len(set(report))))


def write_year_pages(years, summary):
    consts = summary.get('constants', {})
    intro = summary.get('intro', {})
    written = set()
    for y, info in sorted(years.items()):
        srcs = sorted(info['sources'])
        body = ''
        if str(y) in intro:
            body += '## Úvod ročenky\n\n' + intro[str(y)]
        write_page(CONTENT / str(y) / '_index.md',
                   {'title': 'Astronomická olympiáda %d' % y, 'year': y, 'weight': -y,
                    'sources': srcs,
                    'collection': 'ZAO' if srcs == ['ZAO'] else None}, body)
        # constants: per source; year pages link the matching one
        for key, md in consts.items():
            name, cat = key.split('|')
            if name in srcs:
                slug = 'constants' + ('-' + {'SŠ': 'ss', 'ZŠ': 'zs'}[cat] if cat else '')
                cdir = CACHE / 'const' / ('%s-%s' % (name, cat or 'all'))
                if name == 'ZAO':
                    path = CONTENT / 'constants' / 'collection' / 'index.md'
                    if path in written:      # one page for all ZAO years
                        continue
                    written.add(path)
                    write_page(path, {'title': 'Zoznam konštánt (Zbierka úloh AO 2007–2023)'}, md)
                else:
                    path = CONTENT / str(y) / slug / 'index.md'
                    write_page(path,
                               {'title': 'Zoznam konštánt %s %d' % (cat, y) if cat else 'Zoznam konštánt %d' % y,
                                'year': y, 'build': {'list': 'never'}}, md)
                if cdir.is_dir():
                    for f in cdir.iterdir():
                        shutil.copyfile(f, path.parent / f.name)
    for k, v in summary.get('intro', {}).items():
        if k == 'ZAO':
            write_page(CONTENT / 'collection.md', {'title': 'Zbierka úloh AO 2007–2023 – úvod'}, v)
    # problems with the same statement elsewhere (one problem for both categories, or reused in a later year):
    # a notice on those problem pages only (data/duplicates.json, layouts/_partials/problem-meta.html)
    by_sig = {}
    for info in years.values():
        for f in info['problems']:
            if f['_sig']:
                by_sig.setdefault(f['_sig'], []).append(f)
    dups = {}
    for group in by_sig.values():
        for f in group:
            others = [{'year': d['year'], 'round': d['round'], 'roundName': d['roundName'], 'category': d['category'],
                       'label': d['label'], 'title': d['title'], 'url': '%d/%s/' % (d['year'], d['_slug'])}
                      for d in group if d is not f]
            if others:
                dups['%d/%s' % (f['year'], f['_slug'])] = others
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / 'duplicates.json').write_text(json.dumps(dups, ensure_ascii=False, indent=1, sort_keys=True))
    # overview of what exists / is missing
    rows = []
    for y, info in sorted(years.items()):
        cells, issues = {}, []
        for f in sorted(info['problems'], key=lambda f: f['weight']):
            c = cells.setdefault((f['round'], f['category']), [0, 0, 0])
            c[0] += 1
            c[1] += 0 if f['hasSolution'] else 1
            c[2] += 1 if any('image' in w for w in f.get('warnings', [])) else 0
            found = problem_issues(f)
            if found:
                issues.append({'title': f['title'], 'where': '%s %s %s' % (f['round'], f['category'], f['label']),
                               'url': '%d/%s/' % (f['year'], f['_slug']), 'issues': found})
        rows.append({'year': y, 'sources': sorted(info['sources']),
                     'cells': {'%s %s' % k: v for k, v in cells.items()}, 'issues': issues})
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / 'overview.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
