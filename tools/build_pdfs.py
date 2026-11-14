#!/usr/bin/env python3
"""Compile the yearbook (ročenka) of every source project – and the ZAO collection – with LaTeX,
exactly as Overleaf does, into site/static/pdf/ (committed, linked from the year pages).

Usage:  python3 tools/build_pdfs.py [--only AO_2026]

* compiled in a scratch copy (.cache/latex/<project>), the sources are never touched
* parts that must not be published (results with names of students, photo gallery) are removed
* the result is compressed with Ghostscript (images downsampled to ~150 dpi)
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aosk import layouts  # noqa: E402
from build import CACHE, REPO, find_sources  # noqa: E402

OUT = REPO / 'site' / 'static' / 'pdf'
PRIVATE_PARTS = ('Výsledkové listiny', 'Výsledky', 'Fotogaléria', 'Fotogaleria')
ZAO_PDF = 'zbierka-AO-2007-2023.pdf'


def yearbook(layout, root: Path):
    """(main file relative to root, extra pdflatex args, function preparing the scratch copy)."""
    name = type(layout).__name__
    if name == 'Layout2024':
        main = next(iter(sorted(root.glob('*[Rr]ocenka*.tex')))).name

        def prep(work):
            # \loadAllPriklady lists directories with Java (texosquery) and drops the first 105/106
            # characters of its output – a JVM warning line printed only on Overleaf.
            m = work / 'macros.tex'
            m.write_text(m.read_text(encoding='utf-8').replace(
                '\\substring[q]{\\filesZoznam}{\\the\\drblyWarning}', '\\substring[q]{\\filesZoznam}{1}'), encoding='utf-8')
        return main, ['-shell-escape'], prep, [main]
    if name == 'Layout2025':
        main = '99-background/00-main.tex'      # its default target is the yearbook
        return main, [], None, ['99-background/kompilaty/0-ROCENKA/rocenka-kompilat.tex']
    if name == 'Layout2026':
        main = str(next(iter(sorted((root / 'rocenka').glob('*.tex'),
                                    key=lambda p: (not p.name.upper().startswith('.ROC'), p.name)))).relative_to(root))
        return main, [], None, [main]
    if name == 'LayoutZAO':
        return '__MAIN__.tex', [], None, ['__MAIN__.tex']
    return None


def strip_private(path: Path):
    """Remove \\part{Výsledkové listiny}, \\part{Fotogaléria}, … up to the next part or \\end{document}."""
    s = path.read_text(encoding='utf-8')
    parts = list(re.finditer(r'\\part\*?\{([^}]*)\}', s))
    end_doc = s.find('\\end{document}')
    cuts = []
    for i, m in enumerate(parts):
        if any(p.lower() in m.group(1).lower() for p in PRIVATE_PARTS):
            end = parts[i + 1].start() if i + 1 < len(parts) else (end_doc if end_doc >= 0 else len(s))
            cuts.append((m.start(), end))
    for a, b in reversed(cuts):
        s = s[:a] + s[b:]
    path.write_text(s, encoding='utf-8')


def compile_pdf(name, root, layout, log):
    yb = yearbook(layout, root)
    if not yb:
        log('%s: unknown project layout, skipping' % name)
        return None
    main, extra, prep, to_strip = yb
    work = CACHE / 'latex' / name
    shutil.rmtree(work, ignore_errors=True)
    shutil.copytree(root, work, symlinks=True)
    if prep:
        prep(work)
    for f in to_strip:
        strip_private(work / f)
    # Like Overleaf: pdflatex from the project root, repeated until references/TOC are stable.
    # (latexmk is not used: it crashes on some file names in the projects and leaves half-written PDFs.)
    job = 'rocenka'
    env = dict(os.environ, TEXINPUTS='.:%s:' % work)
    cmd = ['pdflatex', '-interaction=nonstopmode', '-file-line-error', '-jobname=' + job, *extra, main]
    logf = work / (job + '.log')
    for npass in range(1, 5):
        subprocess.run(cmd, cwd=work, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3600)
        text = logf.read_text(errors='replace') if logf.exists() else ''
        if npass >= 2 and not re.search(r'Rerun to get|Label\(s\) may have changed|Rerun LaTeX', text):
            break
    pdf = work / (job + '.pdf')
    errors = len(re.findall(r'^\S+:\d+: |^! ', text, re.M))
    if not pdf.exists():
        log('%s: compilation failed (see %s)' % (name, logf))
        return None
    return pdf, errors


def pages(pdf: Path) -> int:
    m = re.search(r'Pages:\s*(\d+)', subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout)
    return int(m.group(1)) if m else 0


def compress(src: Path, dst: Path):
    """Ghostscript /ebook (images ~150 dpi); the original is kept if gs fails or loses pages."""
    tmp = dst.with_suffix('.tmp.pdf')
    r = subprocess.run(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.6', '-dPDFSETTINGS=/ebook',
                        '-dNOPAUSE', '-dBATCH', '-dQUIET', '-sOutputFile=' + str(tmp), str(src)],
                       capture_output=True, text=True, errors='replace')
    if r.returncode == 0 and tmp.exists() and tmp.stat().st_size < src.stat().st_size and pages(tmp) == pages(src):
        tmp.replace(dst)
    else:
        tmp.unlink(missing_ok=True)
        shutil.copyfile(src, dst)


def build_one(name, root, year):
    """Compile one project; returns the lines to print (so parallel jobs do not interleave)."""
    layout = layouts.detect(root)
    if not layout:
        return []
    if type(layout).__name__ != 'LayoutZAO' and not year:
        return ['%s: directory name contains no year, skipping' % name]
    target = OUT / (ZAO_PDF if type(layout).__name__ == 'LayoutZAO' else 'AO-%d.pdf' % year)
    lines = ['== %s → %s' % (name, target.relative_to(REPO))]
    res = compile_pdf(name, root, layout, lines.append)
    if not res:
        return lines
    pdf, errors = res
    compress(pdf, target)
    lines.append('   %d pages, %.1f MB%s' % (pages(target), target.stat().st_size / 1e6,
                                         ', %d LaTeX errors (ignored, like on Overleaf)' % errors if errors > 0 else ''))
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only')
    ap.add_argument('--jobs', type=int, default=int(os.environ.get('PDF_JOBS', 2)),
                    help='projects compiled in parallel (each LaTeX run uses one core)')
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    todo = [s for s in find_sources() if not a.only or a.only in s[0]]
    with ThreadPoolExecutor(max(1, a.jobs)) as ex:
        for lines in ex.map(lambda s: build_one(*s), todo):
            print('\n'.join(lines), flush=True)


if __name__ == '__main__':
    main()
