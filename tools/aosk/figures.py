"""Figures: find source files, convert them for the web (cached), copy into the page bundle.

* .png/.jpg — copied; large ones are shrunk with ImageMagick (`magick`).
* .pdf      — vector PDFs → SVG (pdftocairo); PDFs with embedded raster images → PNG.
* TikZ      — \\includestandalone files and inline tikzpicture environments are compiled with
               pdflatex (from the year root, like Overleaf) and converted to SVG.
"""
import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

EXTS = ['', '.pdf', '.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG', '.svg', '.eps']
MAX_PX = 1600          # longest side of raster images
JPEG_QUALITY = 85
BIG_BYTES = 400_000    # rasters larger than this get resized/recompressed


def sha(*parts) -> str:
    h = hashlib.sha1()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode())
    return h.hexdigest()[:16]


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


class FigureHandler:
    def __init__(self, source_root: Path, base_dirs, out_dir: Path, cache: Path, tikz_preamble: str, log):
        self.root, self.base_dirs, self.out, self.cache = source_root, base_dirs, out_dir, cache
        self.tikz_preamble, self.log = tikz_preamble, log
        self.used = {}
        self.invert = set()   # output names of line drawings (dark lines on white/transparent) → CSS inversion
        cache.mkdir(parents=True, exist_ok=True)

    def __call__(self, kind: str, arg: str):
        try:
            if kind == 'graphics':
                src = self.find(arg)
                return self.emit(self.convert(src), src.stem) if src else None
            if kind == 'standalone':
                src = self.find(arg, ['.tex', ''])
                return self.emit(self.compile_tex(src.read_bytes(), standalone_file=src), src.stem) if src else None
            if kind == 'tikz':
                doc = ('\\documentclass[tikz,border=2pt]{standalone}\n%s\n\\begin{document}\n%s\n\\end{document}\n'
                       % (self.tikz_preamble, arg))
                return self.emit(self.compile_tex(doc.encode()), 'tikz')
        except Exception as e:  # never break the whole build because of one picture
            self.log('image %s: %s' % (arg[:60], e))
        return None

    # ------------------------------------------------------------ lookup
    def find(self, rel: str, exts=EXTS):
        rel = rel.strip().strip('"')
        for base in self.base_dirs:
            for e in exts:
                p = (base / (rel + e))
                if p.is_file():
                    return p
        name = Path(rel).name  # last resort: unique file with that name anywhere in the source
        hits = [p for e in exts for p in self.root.rglob(name + e) if p.is_file()]
        return hits[0] if len(hits) >= 1 else None

    # ------------------------------------------------------------ output
    def emit(self, converted: Path, stem: str):
        if not converted:
            return None
        stem = re.sub(r'[^A-Za-z0-9_-]+', '-', stem).strip('-') or 'obrazok'
        name = stem + converted.suffix.lower()
        n = 1
        while name in self.used and self.used[name] != converted:
            n += 1
            name = '%s-%d%s' % (stem, n, converted.suffix.lower())
        self.used[name] = converted
        self.out.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(converted, self.out / name)
        if self.is_line_art(converted):
            self.invert.add(name)
        return name

    def is_line_art(self, img: Path) -> bool:
        """Mostly white/transparent with dark lines and few mid-tones (drawings, plots, diagrams).
        Photos and dark images are left alone. Result is cached next to the converted figures."""
        key = self.cache / ('%s.lineart' % sha(img.read_bytes(), 'v2'))
        if key.exists():
            return key.read_text() == '1'
        src = str(img) + '[0]'
        tmp = None
        if img.suffix.lower() == '.svg':  # ImageMagick may lack an SVG reader; rasterize with librsvg
            tmp = self.cache / (key.stem + '-probe.png')
            run(['rsvg-convert', '-w', '200', '-o', str(tmp), str(img)])
            if not tmp.exists():
                key.write_text('0')
                return False
            src = str(tmp)
        base = ['magick', src, '-background', 'white', '-flatten', '-resize', '200x200',
                '-colorspace', 'Gray']
        try:
            white = float(run(base + ['-threshold', '85%', '-format', '%[fx:mean]', 'info:']).stdout or 0)
            dark = 1 - float(run(base + ['-threshold', '35%', '-format', '%[fx:mean]', 'info:']).stdout or 1)
        except ValueError:
            white, dark = 0, 0
        if tmp:
            tmp.unlink(missing_ok=True)
        mid = 1 - white - dark
        res = white > 0.55 and mid < 0.2
        key.write_text('1' if res else '0')
        return res

    # ------------------------------------------------------------ conversion
    def convert(self, src: Path) -> Path:
        data = src.read_bytes()
        ext = src.suffix.lower()
        key = sha(data, MAX_PX, JPEG_QUALITY, 'v3')
        if ext == '.pdf':
            return self.pdf_to_web(src, key)
        if ext in ('.png', '.jpg', '.jpeg'):
            if len(data) <= BIG_BYTES:
                return src
            out = self.cache / (key + ('.jpg' if ext != '.png' else '.png'))
            if not out.exists():
                args = ['magick', str(src), '-auto-orient', '-resize', '%dx%d>' % (MAX_PX, MAX_PX), '-strip']
                if ext == '.png':
                    run(args + [str(out)])
                    if out.exists() and out.stat().st_size > BIG_BYTES:
                        # 1) 256-colour PNG (fine for plots and drawings)
                        q = self.cache / (key + '-q.png')
                        run(['magick', str(out), '-colors', '256', 'PNG8:' + str(q)])
                        if q.exists() and q.stat().st_size <= BIG_BYTES:
                            out.unlink(); q.rename(out)
                        else:
                            q.unlink(missing_ok=True)
                            # 2) photos: JPEG on white background (pages are white)
                            jpg = self.cache / (key + '.jpg')
                            run(['magick', str(out), '-background', 'white', '-flatten', '-quality', str(JPEG_QUALITY), str(jpg)])
                            if jpg.exists() and jpg.stat().st_size < out.stat().st_size:
                                out.unlink()
                                out = jpg
                else:
                    run(args + ['-quality', str(JPEG_QUALITY), str(out)])
            if not out.exists():
                alt = self.cache / (key + '.jpg')
                return alt if alt.exists() else src
            return out
        if ext == '.svg':
            return src
        if ext == '.eps':
            out = self.cache / (key + '.svg')
            if not out.exists():
                pdf = self.cache / (key + '.pdf')
                run(['epstopdf', str(src), '--outfile=' + str(pdf)])
                return self.pdf_to_web(pdf, key)
            return out
        raise ValueError('unsupported format %s' % ext)

    def pdf_to_web(self, pdf: Path, key: str) -> Path:
        svg, png = self.cache / (key + '.svg'), self.cache / (key + '.png')
        if svg.exists():
            return svg
        if png.exists():
            return png
        lst = run(['pdfimages', '-f', '1', '-l', '1', '-list', str(pdf)]).stdout.strip().splitlines()
        if len(lst) > 2:  # contains raster images → PNG is smaller and safer than SVG with embedded bitmaps
            run(['pdftocairo', '-png', '-singlefile', '-f', '1', '-l', '1', '-r', '150', str(pdf), str(png)[:-4]])
            if png.exists() and png.stat().st_size > BIG_BYTES:
                return self.convert_png_path(png)
            return png
        r = run(['pdftocairo', '-svg', '-f', '1', '-l', '1', str(pdf), str(svg)])
        if r.returncode or not svg.exists():
            raise RuntimeError('pdftocairo: ' + r.stderr[:200])
        return svg

    def convert_png_path(self, png: Path) -> Path:
        jpg = png.with_suffix('.jpg')
        run(['magick', str(png), '-resize', '%dx%d>' % (MAX_PX, MAX_PX), '-quality', str(JPEG_QUALITY), str(jpg)])
        if jpg.exists() and jpg.stat().st_size < png.stat().st_size:
            png.unlink()
            return jpg
        return png

    def compile_tex(self, doc: bytes, standalone_file: Path = None) -> Path:
        key = sha(doc, self.tikz_preamble, 'tex-v1')
        svg = self.cache / (key + '.svg')
        if svg.exists():
            return svg
        fail = self.cache / (key + '.failed')
        if fail.exists():
            raise RuntimeError('compilation failed (cached), log: %s' % fail)
        with tempfile.TemporaryDirectory(prefix='aosk-tex-') as tmp:
            tmp = Path(tmp)
            if standalone_file is not None:
                # compile the original file from the year root so relative \input's work
                texfile, cwd = standalone_file, self.root
            else:
                texfile, cwd = tmp / 'fig.tex', self.root
                texfile.write_bytes(doc)
            env = dict(os.environ, TEXINPUTS='.:%s:%s:' % (self.root, texfile.parent))
            r = run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', str(tmp),
                     '-jobname', 'fig', str(texfile)], cwd=cwd, env=env, timeout=300)
            pdf = tmp / 'fig.pdf'
            if not pdf.exists():
                fail.write_text(r.stdout[-3000:])
                raise RuntimeError('compilation failed, log: %s' % fail)
            out = self.pdf_to_web(pdf, key)
            return out
