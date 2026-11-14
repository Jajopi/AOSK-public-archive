# AOSK-public-archive

Static, searchable archive of the problems and solutions of the Slovak Astronomical Olympiad
(Astronomická olympiáda, AO), generated from the Overleaf (LaTeX) projects and published on GitHub Pages.

- one page per problem: statement, solution (folded under „Riešenie“), points, author, topics
- year pages with all problems by round and category, the yearbook introduction and the list of constants
- the yearbook of each year as PDF, compiled from the Overleaf sources (2007–2023: one PDF of the ZAO collection)
- full-text search with filters (year, round, category, type, topic) – [Pagefind](https://pagefind.app/)
- overview of what is missing (`/prehlad/`)

Only problems that were published are included: for 2024 and later the list of problems is taken from the
yearbook (ročenka) of the year, for 2007–2023 from the collection book *Zbierka úloh AO* (`sources/ZAO`).

## How it works

```
sources/<project>/      Overleaf exports (NOT in git)
   │  tools/build.py    detects the layout of each project, reads the yearbook, extracts statement +
   │                    solution + metadata, converts LaTeX → Markdown (pandoc + tools/filters/aosk.lua),
   │                    figures → SVG/PNG/JPG
   ▼
   │  tools/build_pdfs.py  compiles each yearbook (ročenka) with LaTeX like Overleaf, without the results
   │                       lists and the photo gallery → site/static/pdf/AO-<year>.pdf, zbierka-AO-2007-2023.pdf
   ▼
site/content/<year>/<problem>/index.md + figures, site/static/pdf/   (generated, committed to git)
   │  GitHub Actions    hugo (math rendered by KaTeX at build time) → pagefind
   ▼
GitHub Pages
```

The LaTeX sources stay the only place where problems are edited. The archive is always regenerated
from them, so a fix made in Overleaf only needs a new export and `make content`.

## Adding a new year (or updating an existing one)

1. Download the Overleaf project (*Menu → Download → Source*) and unzip it into `sources/`, e.g.
   `sources/AO_2027/`. The directory name must contain the year. (A `.zip` placed in `sources/` also works;
   it is unpacked into `.cache/`.)
2. Make sure the project contains the yearbook (`rocenka/…ROCENKA.tex` in the 2026 layout) with all problems
   that were used – only those are published.
3. Run `make content pdfs` (≈1–5 min for the import, figures are cached in `.cache/`; a few minutes per
   yearbook PDF).
   Read the summary: warnings are written to `site/data/report.json`, problems with missing figures or
   solutions also appear on the page `/prehlad/`.
4. Check the result locally: `make preview` (or `docker compose up`), open <http://localhost:8080>.
5. Commit `site/content`, `site/data` and `site/static/pdf` and push; GitHub Actions publishes the site.

If a new year uses a **new Overleaf layout**, add an adapter class to `tools/aosk/layouts.py`
(see the existing `Layout2024`, `Layout2025`, `Layout2026`, `LayoutZAO`). If it keeps the 2026 layout
(`background/.global/` directory), nothing needs to change.

### Tags

Problems from 2007–2023 get their topic from the chapter of the ZAO collection. Other tags are added in
`tools/tags.yaml` (key = `<year>/<problem folder>`), then `make content`.

### Math macros

Math is rendered by KaTeX. When a source uses a macro KaTeX does not know, the Hugo build prints
`MATHERR <page> | <formula> | <error>`. Add the macro to `site/data/katex.yaml`
(or to `tools/aosk/siunitx.py` for siunitx units).

## Local preview with Docker

Everything (import, Hugo, PDFs, search) can run in a container, so nothing but Docker is needed:

```sh
docker compose up                      # pipeline, then http://localhost:8080
SKIP_PDF=1 docker compose up           # faster: do not recompile the yearbook PDFs
docker compose run --rm preview make rebuild   # force everything to be rebuilt
docker compose --profile dev up dev    # live reload for templates/CSS: http://localhost:1313 (no search)
docker compose run --rm content        # only the import (sources/ → site/content)
```

`docker compose up` runs `make preview`, which is incremental: the import runs only when something in
`sources/` or `tools/` changed, the yearbook PDFs only when `sources/` or `tools/build_pdfs.py` changed, and
the site and search index only when something in `site/` changed (fingerprints of file paths, sizes and modification times in `.cache/stamps/`). With nothing
changed the existing build is served immediately. Without Docker, `make preview` does the same.

The first `docker compose up` builds the image (TeX Live, ~2–3 GB, several minutes). The repository is
mounted into the container, so the generated files (`site/content`, `.cache`, `site/public`) appear in your
working copy and are owned by your user (UID/GID 1000 by default; set `UID`/`GID` if yours differ).
`JOBS=2 docker compose up` limits the number of problems converted in parallel.

## Requirements (for `make content` without Docker)

- Python 3.10+ with `pyyaml`
- pandoc ≥ 3.1
- TeX Live with the packages used by the sources (TikZ figures, yearbook PDFs): `pdflatex`, `latexmk`,
  `siunitx`, `tikz`, `pgfplots`, `tikz-3dplot`, `mathabx`, `standalone`, `texosquery`, …
  (`texlive-full`, or Arch: `texlive-meta` group); Java for `texosquery` (2024 project)
- poppler (`pdftocairo`, `pdfimages`), ImageMagick 7 (`magick`), librsvg (`rsvg-convert`), Ghostscript (`gs`)

For the site: [Hugo](https://gohugo.io/) ≥ 0.141 (standard edition) and Pagefind.

## Layout of the repository

| Path | Content |
|---|---|
| `tools/build.py` | import pipeline entry point |
| `tools/aosk/layouts.py` | one adapter per Overleaf project layout (yearbook → list of problems) |
| `tools/aosk/transform.py` | LaTeX cleanup, numbering of equations/figures, references, pandoc |
| `tools/aosk/siunitx.py` | `\SI`, `\ang`, units… → plain math |
| `tools/aosk/figures.py` | figure lookup and conversion (cache in `.cache/figures`) |
| `tools/filters/aosk.lua` | pandoc filter: (a)(b)(c) lists, figures, tables |
| `tools/build_pdfs.py` | compiles the yearbooks / ZAO collection into `site/static/pdf/` |
| `tools/hugo_log.py` | condenses KaTeX's per-symbol warnings in the Hugo output into one summary line |
| `site/` | Hugo site (`content/` generated, `pages/` hand-written, `layouts/`, `data/katex.yaml`) |

## Privacy note

Problem pages show only the authors of a problem. Reviewers (correctors), internal notes (`\poznamky`),
unused problems, results lists and the yearbook photo gallery are never imported or published.

## License

The content (problems, solutions, texts) is available under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) – see [`LICENSE`](LICENSE).
Bundled third-party files keep their own licenses: KaTeX (MIT, `site/static/katex/LICENSE`) and the Play font
(SIL OFL, `site/static/fonts/OFL.txt`).
