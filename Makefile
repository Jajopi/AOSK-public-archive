# Incremental local pipeline (also used by `docker compose up`). Requirements: see README.md.
#
#   make preview   import + yearbook PDFs (if sources/ changed) → site + search (if site/ changed) → serve
#   make content   only the import: sources/ → site/content
#   make pdfs      compile the yearbooks (+ ZAO collection) from sources/ into site/static/pdf
#   make site      only the site build into site/public (+ search index)
#   make serve     live-reloading Hugo server (no search)
#   make rebuild   forget what was built and run `make preview` from scratch
#
# Changes are detected by fingerprints (paths, sizes and modification times) stored in .cache/stamps.

HUGO     ?= hugo
PAGEFIND ?= pagefind
JOBS     ?= 4
PORT     ?= 8080
BASEURL  ?= http://localhost:$(PORT)/
SKIP_PDF ?= 0
STAMPS   := .cache/stamps
SHELL    := /bin/bash
.SHELLFLAGS := -o pipefail -c

# fingerprint of all regular files under the given paths
FP = find $(1) -type f ! -path '*/__pycache__/*' ! -path 'site/public/*' ! -path 'site/resources/*' \
       ! -name '.hugo_build.lock' -printf '%p %T@ %s\n' 2>/dev/null | sort | md5sum | cut -c1-32
HAVE_SOURCES = [ -n "$$(find sources -mindepth 1 -maxdepth 1 ! -name '.*' 2>/dev/null)" ]

.PHONY: preview content pdfs site serve rebuild clean FORCE

preview:
	@# import and yearbook PDFs are independent → run them in parallel (output kept per step)
	@$(MAKE) --no-print-directory -j2 --output-sync=target $(STAMPS)/site
	@echo "== serving http://localhost:$(PORT)/  (Ctrl+C to stop)"
	python3 -m http.server --directory site/public --bind 0.0.0.0 $(PORT)

content: $(STAMPS)/content
pdfs: $(STAMPS)/pdfs
site: $(STAMPS)/site

# --- import ------------------------------------------------------------------------------------
$(STAMPS)/sources.fp: FORCE
	@mkdir -p $(STAMPS)
	@fp="$$($(call FP,sources tools))"; echo "$$fp" | cmp -s - $@ || echo "$$fp" > $@

$(STAMPS)/content: $(STAMPS)/sources.fp
	@if ! $(HAVE_SOURCES); then echo "== sources/ is empty – keeping the committed site/content"; \
	else echo "== import sources/ → site/content"; python3 tools/build.py --jobs $(JOBS); fi
	@touch $@

# --- yearbook PDFs (LaTeX, slow: only when sources/ or the PDF script changed) -----------------
$(STAMPS)/pdfsrc.fp: FORCE
	@mkdir -p $(STAMPS)
	@fp="$$($(call FP,sources tools/build_pdfs.py))"; echo "$$fp" | cmp -s - $@ || echo "$$fp" > $@

$(STAMPS)/pdfs: $(STAMPS)/pdfsrc.fp
	@if [ "$(SKIP_PDF)" = 1 ]; then echo "== yearbook PDFs skipped (SKIP_PDF=1)"; \
	elif ! $(HAVE_SOURCES); then echo "== sources/ is empty – keeping the committed PDFs"; touch $@; \
	else echo "== yearbook PDFs (LaTeX)"; python3 tools/build_pdfs.py && touch $@; fi

# --- site, search ------------------------------------------------------------------------------
$(STAMPS)/site.fp: $(STAMPS)/content $(STAMPS)/pdfs FORCE
	@fp="$$($(call FP,site)) $(BASEURL)"; echo "$$fp" | cmp -s - $@ || echo "$$fp" > $@

$(STAMPS)/site: $(STAMPS)/site.fp
	@echo "== hugo"
	rm -rf site/public
	$(HUGO) --source site --minify --baseURL "$(BASEURL)" 2>&1 | python3 tools/hugo_log.py
	@echo "== search index"
	$(PAGEFIND) --site site/public
	@touch $@

# --- other -------------------------------------------------------------------------------------
serve:
	$(HUGO) server --source site --bind 0.0.0.0 --port 1313 --baseURL http://localhost:1313/ --poll 700ms 2>&1 | python3 tools/hugo_log.py

rebuild:
	rm -rf $(STAMPS)
	$(MAKE) preview

clean:
	rm -rf site/public site/resources .cache
