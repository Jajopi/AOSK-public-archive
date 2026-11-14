# Image with everything needed to import the sources and build/preview the site locally.
# Used by docker-compose.yml; the repository is bind-mounted at /work (nothing is copied in).
FROM debian:trixie-slim

ARG HUGO_VERSION=0.170.0
ARG PAGEFIND_VERSION=1.6.0
ARG PANDOC_VERSION=3.11
ENV DEBIAN_FRONTEND=noninteractive LANG=C.UTF-8

# TeX Live (TikZ figures and the yearbook PDFs are compiled like on Overleaf), image tools,
# Ghostscript (PDF compression), Java (texosquery used by the 2024 project)
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-yaml make curl ca-certificates \
      texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-science \
      texlive-pictures texlive-fonts-recommended texlive-fonts-extra texlive-lang-czechslovak \
      texlive-plain-generic texlive-extra-utils latexmk \
      poppler-utils imagemagick librsvg2-bin ghostscript default-jre-headless fonts-noto-core \
    && rm -rf /var/lib/apt/lists/*

# pandoc (pinned, Debian's is older), Hugo, Pagefind – for amd64 or arm64 (Apple Silicon, ARM Linux)
RUN arch="$(dpkg --print-architecture)" \
    && case "$arch" in amd64) pf=x86_64 ;; arm64) pf=aarch64 ;; *) echo "unsupported architecture $arch"; exit 1 ;; esac \
    && curl -fsSL -o /tmp/pandoc.deb "https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-1-${arch}.deb" \
    && dpkg -i /tmp/pandoc.deb && rm /tmp/pandoc.deb \
    && curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-${arch}.tar.gz" | tar xz -C /usr/local/bin hugo \
    && curl -fsSL "https://github.com/Pagefind/pagefind/releases/download/v${PAGEFIND_VERSION}/pagefind-v${PAGEFIND_VERSION}-${pf}-unknown-linux-musl.tar.gz" | tar xz -C /usr/local/bin pagefind \
    && (command -v magick || ln -s "$(command -v convert)" /usr/local/bin/magick)

# Run as the owner of the mounted repository, so generated files belong to the host user whatever their UID
# (with rootless Docker/Podman the repository appears owned by root, which is the host user there).
RUN printf '%s\n' '#!/bin/sh' 'set -e' 'u=$(stat -c %u /work) g=$(stat -c %g /work)' \
      'if [ "$(id -u)" = 0 ] && [ "$u" != 0 ]; then exec setpriv --reuid="$u" --regid="$g" --clear-groups "$@"; fi' \
      'exec "$@"' > /usr/local/bin/as-owner && chmod +x /usr/local/bin/as-owner

WORKDIR /work
ENTRYPOINT ["as-owner"]
CMD ["make", "preview"]
