# BetterVoting abstain / blank / zero — issue index

A single map of the BetterVoting GitHub issues about **abstention vs. blank vs. explicit zero** (and the related "None of the Above" case), because the topic is spread across a dozen tickets and keeps getting re-discovered. Cross-referenced to the **BV Test IDs** (Google-sheet tracker) and the **library cases** that reproduce them.

Concept backbone: [Abstention vs. a zero vs. "None of the Above"](../../STAR_Voting/properties_and_limits/abstention_vs_zero_vs_nota.md).

## The core tension

A STAR ballot line can be a **score 0–5** or **blank**. Three things get conflated:

- **explicit `0`** — an active low score ("I reject this candidate"),
- **blank / `null`** — the voter didn't score that candidate (a per-candidate abstention),
- **whole-ballot abstention** — the voter expressed no preference at all.

Two policy/plumbing questions run through every ticket: **(a) what counts as an abstention?** and **(b) how is a blank stored/exported so a `0` and a `null` stay distinguishable?**

## The root policy decision — #884

**[#884 — Update abstain behavior for STAR](https://github.com/Equal-Vote/bettervoting/issues/884)** is the source of the current behavior: STAR now counts a ballot as an abstention when its marks are **all equal** (all 3s, all 0s, a mix of 0s and nulls…), not only when it's all-null. Implemented via `makeAbstentionTest(markAllEqualAsAbstention=true)` in `Tabulators/Util.ts`. **Adam dissents on the record** ("all threes is not abstain though") — this is the open disagreement most of the UI-mislabel tickets below trace back to.

## The tickets, by theme

### A. Policy — what counts as abstain
| Issue | What | Status |
|---|---|---|
| [#884](https://github.com/Equal-Vote/bettervoting/issues/884) | Count **all-equal** ballots (all 3s/0s/mixed 0-null) as abstain | Implemented; **disputed** |

### B. UI confirmation / receipt mislabels a real vote as "Abstained"
| Issue | What | BV Test ID · election |
|---|---|---|
| [#1053](https://github.com/Equal-Vote/bettervoting/issues/1053) | Full **equal-max** ballot (5,5) shown as "Abstained / No preference" | BV11 · [6xhfp8](https://bettervoting.com/6xhfp8) |
| [#1090](https://github.com/Equal-Vote/bettervoting/issues/1090) | Explicit **all-0** ("equal opposition") shown as "Abstained"; export blank/0 ambiguous. JSON is correct | BV655 · [jfrk9t](https://bettervoting.com/jfrk9t) |
| [#518](https://github.com/Equal-Vote/bettervoting/issues/518) | Confirmation doesn't show the race's method; 0/1 wording (No/Yes/Approve/Abstain) | HOA (old `dev.star.vote` `d93e92a9…`) |
| [#252](https://github.com/Equal-Vote/bettervoting/issues/252) | Ballot warning / "Abstained" message + submit-confirmation flow | Discussion (pre-launch) |
| [#627](https://github.com/Equal-Vote/bettervoting/issues/627) | Voter **can't abstain** on the *last* race | UI bug |

### C. Data export — blank vs `0` vs `null` (audit trail)
| Issue | What | BV Test ID · election |
|---|---|---|
| [#791](https://github.com/Equal-Vote/bettervoting/issues/791) | CSV download has **no clear abstain indicator** — empty cell ambiguous vs explicit 0 | BV20 · [bp7kwg](https://bettervoting.com/bp7kwg) |
| [#1090 (Bug 2)](https://github.com/Equal-Vote/bettervoting/issues/1090) | CSV blanks-for-abstentions ambiguous; wants explicit `NULL` | BV655 · [jfrk9t](https://bettervoting.com/jfrk9t) |
| [#1160](https://github.com/Equal-Vote/bettervoting/issues/1160) | **Add dual export**: "Official Count" (nulls→0) vs "Raw Audit" (keep nulls, `5,,4`) | (pet-style) — **emergent / deprioritized** |

### D. Tabulation / results semantics
| Issue | What | BV Test ID · election |
|---|---|---|
| [#894](https://github.com/Equal-Vote/bettervoting/issues/894) | Plurality "undecided" election (all abstentions) still **claims a winner**; **voter count wrong** (2 vs 3); CSV abstain/blank/zero | BV1570 · [6hv7jf](https://bettervoting.com/6hv7jf) · **closed (#952)** |
| [#1421](https://github.com/Equal-Vote/bettervoting/issues/1421) | **None of the Above** (a real `c-nota` candidate) wins → seated with no special handling | BV215 · [26khr3](https://bettervoting.com/26khr3) |

## How this library relates

- **Concept lesson:** [abstention_vs_zero_vs_nota.md](../../STAR_Voting/properties_and_limits/abstention_vs_zero_vs_nota.md) — the 0 / null / NOTA distinction, and the LH marker vocabulary (`- ~ & ? %`) BV lacks.
- **Reproduced cases:**
  - [`abstain_bugs/`](../../../01_STAR/abstain_bugs/README.md) — the #884 "all-equal = abstain" reproductions, cross-checked against LH:
    - [`bv11_6xhfp8_full_equal_support`](../../../01_STAR/abstain_bugs/bv11_6xhfp8_full_equal_support.md) → **#1053** (`5,5`×3 counted as 3 abstentions).
    - [`bv655_jfrk9t_equal_opposition`](../../../01_STAR/abstain_bugs/bv655_jfrk9t_equal_opposition.md) → **#1090** (explicit `0,0` labeled "Abstained").
    - [`bv1570_6hv7jf_undecided_plurality`](../../../01_STAR/abstain_bugs/bv1570_6hv7jf_undecided_plurality.md) → **#894** (undecided plurality still declares a winner; wrong voter count).
  - [`bv215_26khr3_nota_wins`](../../../01_STAR/none_of_the_above/bv215_26khr3_nota_wins.md) → #1421 (NOTA wins; also carries a per-candidate `null`).
  - [`flat_scores_abstention_c3_b8`](../../../01_STAR/pet_real_bv_election/cases/cases_pages/flat_scores_abstention_c3_b8.md) · [`small_abstention_c2_b5`](../../../01_STAR/pet_real_bv_election/cases/cases_pages/small_abstention_c2_b5.md) · [`bv15_4h89vj_plurality_abstain`](../../../01_STAR/pet_real_bv_election/bv15_4h89vj_plurality_abstain.md) — abstention handling in real BV counts.
  - `YAML_library/2_negative/bv20_neg1.yaml` / `bv20_neg2.yaml` → BV20 / #791.

  **Key finding across the abstain_bugs set:** LH counts an explicit score (even all-0 or all-5) as a real vote and abstains only a *truly blank* ballot, so it never zeroes out the tally the way BetterVoting's #884 "all-equal = abstain" rule does. The winner survives via tiebreak, but the counts diverge — evidence for the #884 dispute.
- **Code contribution:** PR **#1419** (v2 JSON export) preserves `score: null` distinct from `0` — i.e. it delivers the **"Raw Audit Data"** half of **#1160** for the JSON path. Worth commenting on #1160 to link them rather than opening a new export-ambiguity ticket.

## Don't-duplicate note

The "BetterVoting has no explicit abstain/spoiled mark distinct from 0/blank" idea is **already covered** — the *policy* by #884, the *UI mislabel* by #1053 / #1090 / #518, the *export ambiguity* by #791 / #1090(Bug 2) / #1160. Rather than a new standalone issue, the useful moves are: (1) comment on **#1160** linking PR #1419 (raw JSON audit export done), and (2) keep pressing the **#884** policy question ("all-equal ≠ abstain") that the UI-mislabel tickets depend on.

## Gaps / opportunities

- #1053, #1090, and #894 now have reproductions (see `abstain_bugs/` above). ✅
- The **spoiled** / **spoiled-and-reissued** states (LH `?` / `%`) have no BetterVoting equivalent at all — not currently ticketed.
