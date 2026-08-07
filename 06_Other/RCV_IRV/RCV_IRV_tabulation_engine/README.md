# RCV / IRV Tabulation Engine

A single-winner **Instant-Runoff Voting (IRV)** tabulator that reads the same YAML election format as the STAR engine. It wraps the vendored [`pyrankvote`](https://github.com/jontingvold/pyrankvote) library (MIT, see `pyrankvote/LICENSE.txt`); `tabulate` is vendored alongside as its only dependency, so the folder is self-contained.

## Usage

```bash
python rcv_irv_tabulation.py example_tennessee.yaml
```

Any STAR-style YAML works, since ballots are read as scores and converted to ranks on the fly.

## Score → rank conversion

IRV needs *ranked* ballots, but the YAML stores *scores* (0..5). Each ballot is converted with these rules:

- **Higher score = higher preference.**
- **Score 0** (or a blank/marker cell) means **unranked** — the candidate is left off that ballot. The ballot exhausts rather than transferring to a zero-scored candidate (matches STAR's "0 = no support" semantics).
- **Equal non-zero scores** are a **tie**. IRV requires a strict order, so ties are broken deterministically by candidate column order (left-to-right in the ballot header). This is a documented simplification — equal-rank IRV is not represented.

A ballot scored entirely 0 counts as a blank/exhausted vote.

## Known limitation — elimination ties

When two or more candidates are tied for fewest first choices, somebody still has to be cut, and whichever one you cut changes every round after it. This engine inherits pyrankvote's answer, which has **two rungs worth telling apart**:

1. **The ladder.** `_cmp_candidate_vote_counts` (in `pyrankvote/helpers.py`) breaks the tie on **most second choices**, then thirds, then fourths. This is a real, ballot-based tiebreak — structurally the same shape as the STAR engine's *pairwise → five-star → lot* ladder — and while it has information to work with the result is fully determined by the ballots.
2. **The coin.** Once the ladder runs out of ranks (`x >= number_of_candidates`) it falls to `random.choice`. `rcv_irv_tabulation.py` calls `random.seed(0)` so this reproduces run to run.

**What the seed does not buy.** `sorted()` feeds the comparator pairs in an order set by the input list, and that list is built in order of each candidate's **first appearance across the ballot rows**. So the seed pins the *sequence* of coin flips, not the *candidate* each flip lands on. Where the ladder dies — every candidate tied at every rank — **the winner is the first row's first choice, and re-ordering the identical ballots elects somebody else.** That is an *anonymity* failure: who cast which ballot is the one thing a voting rule is supposed to provably ignore.

Demonstrated on a perfect 3-cycle. Same three ballots, six row orderings, three different winners:

```text title="Abridged for the lesson — not verbatim engine output"
Amy>Bruno>Clara · Bruno>Clara>Amy · Clara>Amy>Bruno   →  Amy
Amy>Bruno>Clara · Clara>Amy>Bruno · Bruno>Clara>Amy   →  Amy
Bruno>Clara>Amy · Amy>Bruno>Clara · Clara>Amy>Bruno   →  Bruno
Bruno>Clara>Amy · Clara>Amy>Bruno · Amy>Bruno>Clara   →  Bruno
Clara>Amy>Bruno · Amy>Bruno>Clara · Bruno>Clara>Amy   →  Clara
Clara>Amy>Bruno · Bruno>Clara>Amy · Amy>Bruno>Clara   →  Clara
```

Change one ballot so second choices separate the candidates (Amy 2, Bruno 1, Clara 0) and all six orderings elect Amy — the ladder does its job and the row order stops mattering.

**Practical impact is small; the disclosure gap is the real issue.** An exact tie at *every* rank needs a perfectly symmetric profile, which among real ballots is astronomically rare. What the report never says is which kind of winner you are looking at — one the ballots chose, or one the file order chose. Pinned by `tests/test_rcv_irv_tie_order_sensitivity.py` so a future pyrankvote bump or a home-grown tie rule shows up as a test change rather than a silent one.

Background and the alternatives (batch elimination, Parallel Universe Tiebreaking, a published lot order): [Batch elimination — what happens when the batch is *everyone*](../../../07_Concepts/topics/ties/batch_elimination.md) · [Parallel Universe Tiebreaking](../../../07_Concepts/topics/ties/parallel_universe_tiebreaking.md).

## Status

Minimal first pass: correct round-by-round elimination and winner, using pyrankvote's built-in result table. Colorized banners, `_tabulated` output files, and `--save` parity with the STAR engine can be added later.
