# The website build — searchable pages from the same Markdown

The whole repo publishes as a **searchable website** at **<https://masiarek.github.io/star-voting-library/>** — every teaching page, glossary entry, and generated per-election page, with instant full-text search (the search box is the reason the site exists; GitHub's own rendering never gives readers one).

There is **no separate docs source**. The site is built from the repo root itself ([`mkdocs.yml`](https://github.com/masiarek/star-voting-library/blob/master/mkdocs.yml) + the `mkdocs-same-dir` plugin), so the same Markdown that GitHub renders is what the site serves — nothing is copied, nothing can drift. Non-Markdown files (`.yaml` sources, `_tabulated` `.txt` mirrors, images) are carried through unchanged, so "run this file" links keep working.

## How it deploys

[`.github/workflows/docs.yml`](https://github.com/masiarek/star-voting-library/blob/master/.github/workflows/docs.yml) builds the site on every push to `master` and deploys it to GitHub Pages. **One-time setup** (repo admin): *Settings → Pages → Build and deployment → Source: **GitHub Actions***. After that it's fully automatic.

## Local preview

```sh
uvx --with mkdocs-same-dir --with "mkdocs-material>=9.5" mkdocs serve
```

(or `mkdocs build`, which writes the static site into `site/` — gitignored, never commit it). No project dependency is involved; `uvx` runs the doc tools in their own isolated environment.

## The conventions that make it work

- **Every content folder has a `README.md`** (the existing house rule). MkDocs turns each one into that folder's `index.html`, which is what makes the repo's *folder-style* links (`../center_squeeze_bv2137/`) resolve on the website too.
- **Plain `.html` URLs** (`use_directory_urls: false`). The repo's cross-links were authored for GitHub's file-relative rendering; pretty directory URLs would shift every page one level deeper and 404 the folder-style links. Don't flip this back without fixing hundreds of links.
- **The homepage** is [`index.md`](../../index.md), which inlines [`readme.md`](../../readme.md) at build time (snippet include). GitHub ignores `index.md`; MkDocs doesn't recognize the lowercase `readme.md` as an index. One source, two front doors.
- **Excluded from the site**: dot-dirs, `site/`, `AGENTS.md` (agent-facing duplicate of `CLAUDE.md`), `_demo_dropbox/` staging, and generated ballot printouts — see `exclude_docs` in `mkdocs.yml`.

## Known nits (accepted for v1)

- **Anchor slugs differ from GitHub's** for headings with `&`/em-dashes (GitHub's `#properties--criteria` style). Those links land at the top of the correct page instead of the exact section — about 30 across the repo.
- **Search index is ~6 MB** (≈700 pages). Fine over gzip; if it ever feels slow, the generated `*_pages` could be excluded from indexing (not from the site).
- The 5 build warnings about `img/REPLACE_*.png` are the known screenshot placeholders in the Ranked Robin cases, not site breakage.

## The rename (2026-07-16)

This repo was renamed from `masiarek/YAML` to `masiarek/star-voting-library` on 2026-07-16, *before* the first Pages deploy — so the site URL was born correct and no stale Pages links exist. All `github.com/masiarek/YAML/...` deep links (in Google Docs, Slack, the Substack posts) keep working via GitHub's automatic redirects. Two standing rules: **never create a new repo named `YAML`** under this account (it would sever those redirects), and if the repo is ever renamed again, update `site_url` / `repo_url` / `repo_name` in `mkdocs.yml` — the Pages URL moves on rename and old Pages URLs do **not** redirect.
