#!/usr/bin/env python3
"""Filter Hugo's output: KaTeX prints "No character metrics for 'X'" every time a symbol without font
metrics (planet symbols ♂ ☾ ♃ …) is rendered. They still render (browser fallback font), so the lines
are hidden and only counted; the summary is printed at the end. Everything else passes through."""
import collections
import re
import sys

counts = collections.Counter()
pat = re.compile(r"No character metrics for '(.+?)'")
for line in sys.stdin:
    m = pat.search(line)
    if m:
        counts[m.group(1)] += 1
        continue
    sys.stdout.write(line)
    sys.stdout.flush()
if counts:
    print('KaTeX: symbols without font metrics (rendered with a fallback font): ' +
          ', '.join('%s %dx' % (k, v) for k, v in counts.most_common()) +
          '  (total %d)' % sum(counts.values()))
