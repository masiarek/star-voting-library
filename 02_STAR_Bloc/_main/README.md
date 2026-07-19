# 02_STAR_Bloc/_main — Bloc STAR case files

The Bloc STAR reference elections themselves live here. Each is a small, engine-verified YAML carrying `expected_winners` (auto-checked by `test_method_positive.py`). BV-backed cases also keep a frozen `_bv_export.json` (the BetterVoting export) and a two-view `.md` — the BetterVoting result beside the inline LH report.

**Naming.** `bv<NNN>_<descriptor>.yaml` ties a file to its row in the *BetterVoting – test cases* master sheet; `00_c3_b3_bloc-baseline-2-seats.yaml` is the tie-free control. `voting_method: Bloc STAR` (not the vaguer `bloc`).

**Index & status** — the BV id → scenario → tie type → issue → case table lives one level up, in the folder overview: [02_STAR_Bloc/README.md → Bloc test-case index](../README.md#the-reference-cases). That's the single source of truth; this page just makes the case folder discoverable on GitHub.

# file: README.md
