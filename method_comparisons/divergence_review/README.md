# Divergence review — the generated cross-method ledger

**Everything in this folder except this README is generated** — `build_divergence_index.py` re-tabulates the curated single-winner STAR library under RCV-IRV, Ranked Robin, and Approval on every commit (wired into the pre-commit hook) and rewrites the ledger. Don't hand-edit; edit the source elections instead.

- **[INDEX.md](INDEX.md)** — the ledger: every election where at least one method disagrees with STAR, with winners per method.
- `divergence.csv` — the same table, machine-readable.
- `cases/` — one generated teaching page per divergent election.
