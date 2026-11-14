# Issues found in the Overleaf projects

Found while building the archive (state of the sources from November 2026). The pipeline works around all of them,
but they should be fixed in Overleaf. Per-problem issues (missing solutions, figures, references, duplicates) are
also listed live in the last column of the [overview page](https://jajopi.github.io/AOSK-public-archive/prehlad/).

## AO 2024
- `\loadAllPriklady` lists folders with Java (texosquery) and cuts off a fixed 105/106 characters
  (`\drblyWarning`) – the JVM warning printed only on Overleaf. It breaks everywhere else;
  `tools/build_pdfs.py` patches it in its scratch copy.
- Per-round solution documents do not compile cleanly (1–6 errors each; Overleaf hides them).
- DK ZŠ P1 Gnómon: the text mentions a figure that is not in the source.
- 7 overfull lines in the yearbook.

## AO 2025
- RK SŠ D1 Rýchlostná dátovka: `\ref{tab:tabulka-1}` points to a missing label (shows "??").
- RK ZŠ P1 „Originálny názov“: placeholder title; the text mentions a figure that is not in the source.
- DK ZŠ Hviezdny Mesiac: `\(` inside a formula.
- CK SŠ D2 Vzdialená galaxia (`52-Farebna-mapa`): web links written with `\hyperlink` (an internal anchor) instead of
  `\href`, so they do not work in the PDF (the import converts them).
- DK SŠ D1 Vera Rubin links the Science article through `sci-hub.se` (kept as is, by decision).
- Per-round solution documents fail to compile (2–11 errors each, no PDF).
- 7 overfull lines in the yearbook.

## AO 2026
- CK solutions: 15 errors ("Not in outer par mode").
- 14 overfull lines in the yearbook.

## ZAO (collection 2007–2023)
- Statement and solution titles differ in 7 files (they are paired by title); one title has `A0` instead of `AO`.
- Two problems have no „úloha N“ in the title; 114 problems have no name at all (shown as „Úloha N“ – the
  sources contain no names for them, not even in the solution titles).
- 2016 DK SŠ Ú2 „Tepelné rozšírenie spektrálnej čiary“ is titled „AO 2022“ and has no solution.
- 2009 DK SŠ Ú7 „Galileiho dedičstvo“ has no solution.
- The text mentions a figure that is not in the source: 2007 CK SŠ Ú4, 2008 CK SŠ Ú4, 2014 DK SŠ Ú1,
  2020 CK SŠ Ú4, 2021 CK SŠ Ú2.
- 2011 CK SŠ Ú4: `$` inside a formula.
- 15 unresolved references in the compiled PDF (probably statement↔solution links broken by the title mismatches).

## All projects
- Links without a scheme (`\url{www.aosk.eu/…}`) and an e-mail written as `\url{zbierka@aosk.sk}`
  (the import fixes them).
