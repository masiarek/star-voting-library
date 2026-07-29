# The website build — searchable pages from the same Markdown

The whole repo publishes as a **searchable website** at **<https://masiarek.github.io/star-voting-library/>** — every teaching page, glossary entry, and generated per-election page, with instant full-text search (the search box is the reason the site exists; GitHub's own rendering never gives readers one).

There is **no separate docs source**. The site is built from the repo root itself ([`mkdocs.yml`](https://github.com/masiarek/star-voting-library/blob/master/mkdocs.yml) + the `mkdocs-same-dir` plugin), so the same Markdown that GitHub renders is what the site serves — nothing is copied, nothing can drift. Non-Markdown files (`.yaml` sources, `_tabulated` `.txt` mirrors, images) are carried through unchanged, so "run this file" links keep working.

## How it deploys

[`.github/workflows/docs.yml`](https://github.com/masiarek/star-voting-library/blob/master/.github/workflows/docs.yml) builds the site on every push to `master` and deploys it to GitHub Pages. **One-time setup** (repo admin): *Settings → Pages → Build and deployment → Source: **GitHub Actions***. After that it's fully automatic.

## Local preview

```sh
uvx --with mkdocs-same-dir --with "mkdocs-material>=9.5" --with mkdocs-redirects mkdocs serve
```

(or `mkdocs build`, which writes the static site into `site/` — gitignored, never commit it). No project dependency is involved; `uvx` runs the doc tools in their own isolated environment.

## The conventions that make it work

- **Every content folder has a `README.md`** (the existing house rule). MkDocs turns each one into that folder's `index.html`, which is what makes the repo's *folder-style* links (`../center_squeeze_bv2137/`) resolve on the website too.
- **Plain `.html` URLs** (`use_directory_urls: false`). The repo's cross-links were authored for GitHub's file-relative rendering; pretty directory URLs would shift every page one level deeper and 404 the folder-style links. Don't flip this back without fixing hundreds of links.
- **The homepage** is [`index.md`](../../index.md): a **site-only graphical hero** (big headline, CTA buttons, the official EVC ballot image — attributed, styled by the `.star-hero` rules in `site_extra.css`), followed by everything below `readme.md`'s own text hero, inlined at build time via the snippet-**section** markers inside `readme.md` (`<!-- --8<-- [start:below-hero] -->` … `[end:below-hero]`). GitHub ignores `index.md` and renders `readme.md` whole; MkDocs doesn't recognize the lowercase `readme.md` as an index. One source for the shared body, two front doors — **don't delete the invisible comment markers in `readme.md`**, the homepage include depends on them.
- **The homepage's "New to STAR?" card row** is a `<div class="star-path" markdown="1">` in `readme.md`, styled by `site_extra.css` (a 2×2 card grid on the site). On GitHub the class is ignored and it degrades to a plain stacked list — that's intentional; keep any future hero markup dual-renderable the same way.
- **Hidden from the sidebar, still built** (`not_in_nav` in `mkdocs.yml`): `CLAUDE.md`, `THIRD_PARTY_LICENSES.md`, and `readme.md` (its content is already the homepage). Links to them keep working; they just no longer appear in the left nav ahead of the teaching content.
- **Excluded from the site**: dot-dirs, `site/`, `AGENTS.md` (agent-facing duplicate of `CLAUDE.md`), `_demo_dropbox/` staging, and generated ballot printouts — see `exclude_docs` in `mkdocs.yml`.

## Known nits (accepted for v1)

- **Anchor slugs differ from GitHub's** for headings with `&`/em-dashes (GitHub's `#properties--criteria` style). Those links land at the top of the correct page instead of the exact section — about 30 across the repo.
- **Search index is ~6 MB** (≈700 pages). Fine over gzip; if it ever feels slow, the generated `*_pages` could be excluded from indexing (not from the site).
- **~1,200 `unrecognized relative link` INFO lines — benign, don't "fix" them.** These are *folder* links (666 written `…/dir/`, 546 as bare `…/dir`) rather than file links, so MkDocs declines to rewrite them and leaves them as-is, suggesting `…/dir/README.md` instead. **They are not broken.** GitHub Pages serves a directory URL from its `index.html` (and 301s the no-slash form to the slash form), and GitHub's own file view resolves a folder link to that folder's README — which is exactly why the repo writes them this way, since links must work in *both* places. Spot-checked live 2026-07-29: 12 of 12 sampled across both forms returned HTTP 200, and `check_repo_hygiene.py` passes them too. Rewriting 1,200 links to `README.md` form would be a very large diff for no user-visible gain, so the house answer is: **leave them, and filter these lines out when reading build output** (`mkdocs build 2>&1 | grep -v "unrecognized relative link"`). The messages are INFO, not WARNING — the build stays warning-free.
- **The build is warning-free** as of 2026-07-29. It used to emit 5 warnings for `img/REPLACE_*.png` — uncaptured screenshot placeholders on the Ranked Robin case pages — which rendered as broken images on the site; those shots are now captured (`05_Ranked_Robin/*/img/<bvid>_*.png`). If `REPLACE_*` warnings reappear, they mean the same thing: a page references a screenshot nobody took yet. Placeholders that are **commented out** (as on `teaching_runoff_reversal.md` and the two `STAR_reporting` pages) don't warn and don't break the site — they're inert until someone captures the image.

## The rename (2026-07-16)

This repo was renamed from `masiarek/YAML` to `masiarek/star-voting-library` on 2026-07-16, *before* the first Pages deploy — so the site URL was born correct and no stale Pages links exist. All `github.com/masiarek/YAML/...` deep links (in Google Docs, Slack, the Substack posts) keep working via GitHub's automatic redirects. Two standing rules: **never create a new repo named `YAML`** under this account (it would sever those redirects), and if the repo is ever renamed again, update `site_url` / `repo_url` / `repo_name` in `mkdocs.yml` — the Pages URL moves on rename and old Pages URLs do **not** redirect.
