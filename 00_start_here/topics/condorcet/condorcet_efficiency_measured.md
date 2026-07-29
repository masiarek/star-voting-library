# Condorcet efficiency, measured

→ Topic hub: [Condorcet efficiency](README.md) · the simulation: [`condorcet_efficiency_simulation.py`](../../../06_Other/simulations/condorcet_efficiency_simulation.py) ([folder README](../../../06_Other/simulations/README.md)) · glossary: [`Condorcet efficiency`](../../GLOSSARY.md#properties-criteria) · **Level: Voting 301** — Curriculum [301.6](../../curriculum/CURRICULUM_301.md)

"STAR's Condorcet efficiency is very high" is one of the most-repeated claims in voting reform — and, until this page existed, one this repo made in four places without a number anyone could reproduce. This page fixes that by **measuring** it, under the folder rule that governs every simulation here: *always report the model and the parameters with the number.*

The short answer: **there is no single number, and the honest range is wider than the slogan suggests.** STAR lands between **74% and 99%** depending on how many candidates are running and what the electorate looks like. "Very high" is fair at three candidates in a realistic electorate. It is not fair at seven.

## What is actually being measured

A method's **Condorcet efficiency** is a conditional probability:

> **Condorcet efficiency** = P(the method elects the [Condorcet winner](README.md) | a Condorcet winner exists)

That conditional carries real weight and is the most common place these numbers get mangled. When the electorate produces a **cycle** there *is* no Condorcet winner, so no method can possibly elect one. Folding cycles into the denominator would drag every method's score down by the cycle rate and end up measuring **the electorate rather than the method**. So cycle elections are excluded, and the share of elections that had a Condorcet winner at all is reported separately as the `CW exists` column — which turns out to be one of the more revealing columns in the table.

Six methods read **the same sampled electorate**, each through its own ballot, so the comparison is apples-to-apples. Voter utilities are sampled first and every ballot is derived from them — never the reverse ([simulate utilities, not ballots](../simulate_utilities_not_ballots.md)).

**Ranked Robin is the control, not a result.** [Copeland](../../../05_Ranked_Robin/concepts/ranked_robin.md) is Condorcet-efficient by construction, so its column *must* read exactly 100.0%. It is printed precisely so that a reader can check the harness: any cell below 100.0% would mean the pairwise code and the method code disagree, and every other number in the run would be worthless.

## The measured table

4,000 elections per cell, seed 20260727, sincere approval cutoff = score ≥ 4.

```
model       C     V   CW exists | RankedRobin        STAR       Score    Approval     RCV-IRV   Plurality
---------------------------------------------------------------------------------------------------------
noise       3    51       90.8% |      100.0%       89.7%       83.2%       77.4%       96.7%       77.8%
noise       3   501       90.4% |      100.0%       90.0%       83.4%       76.7%       96.4%       76.2%
noise       5    51       75.9% |      100.0%       83.7%       77.1%       64.8%       88.9%       60.0%
noise       5   501       73.8% |      100.0%       82.9%       75.4%       65.9%       89.9%       57.2%
noise       7    51       63.7% |      100.0%       83.8%       76.1%       62.6%       84.5%       49.5%
noise       7   501       63.6% |      100.0%       82.8%       76.8%       59.8%       84.6%       46.2%

spatial1d   3    51       99.6% |      100.0%       94.8%       83.2%       82.8%       89.1%       73.1%
spatial1d   3   501       99.9% |      100.0%       97.3%       84.4%       83.5%       86.8%       69.5%
spatial1d   5    51       97.9% |      100.0%       85.0%       74.6%       64.2%       66.7%       46.1%
spatial1d   5   501       99.5% |      100.0%       86.5%       72.1%       67.0%       60.8%       41.6%
spatial1d   7    51       95.0% |      100.0%       74.0%       65.3%       53.3%       52.1%       34.8%
spatial1d   7   501       98.9% |      100.0%       79.4%       67.6%       55.8%       47.0%       29.9%

spatial2d   3    51       99.7% |      100.0%       96.1%       89.4%       89.7%       96.1%       84.2%
spatial2d   3   501      100.0% |      100.0%       98.5%       91.6%       92.0%       96.5%       83.9%
spatial2d   5    51       98.5% |      100.0%       90.7%       83.5%       79.4%       85.7%       62.5%
spatial2d   5   501       99.9% |      100.0%       95.7%       87.2%       85.9%       85.2%       60.6%
spatial2d   7    51       96.7% |      100.0%       87.5%       80.7%       73.3%       71.9%       47.2%
spatial2d   7   501       99.6% |      100.0%       92.2%       84.5%       81.3%       72.3%       45.1%

faction2d   3    51       99.2% |      100.0%       97.1%       89.3%       90.0%       95.8%       90.2%
faction2d   3   501       99.2% |      100.0%       99.2%       89.9%       92.1%       95.6%       90.2%
faction2d   5    51       97.1% |      100.0%       92.4%       83.0%       79.9%       86.5%       73.8%
faction2d   5   501       97.2% |      100.0%       94.6%       84.4%       80.1%       85.4%       73.5%
faction2d   7    51       94.5% |      100.0%       88.8%       80.1%       69.9%       77.3%       62.5%
faction2d   7   501       95.4% |      100.0%       92.0%       81.7%       73.7%       76.3%       60.9%
```

`noise` is impartial culture (every utility independent and uniform); `spatial1d` / `spatial2d` place voters and candidates in 1- and 2-dimensional issue space; `faction2d` clusters voters around three centers. Reproduce with:

```bash
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --trials 4000
```

## What it means

**1. The model swings the answer more than the method does.** RCV-IRV ranges from 96.7% to 47.0% across these cells — a 50-point spread, wider than the gap between *any two methods* in any single row. Anyone quoting a bare Condorcet-efficiency number for any method, this repo included, is quoting a model choice as much as a result.

**2. Under impartial culture, RCV-IRV beats STAR — and that deserves to be said plainly.** At three candidates, IRV scores 96.7% against STAR's 89.7%. This is not a rounding artifact; it holds at both electorate sizes and across the field sizes under `noise`. It is the kind of result [the repo's fairness rule](../../../method_comparisons/) exists to make us print rather than bury.

But the same model that flatters IRV also destroys its own credibility: impartial culture manufactures cycles at rates no real electorate shows (`CW exists` falls to **63.6%** at seven candidates — more than a third of elections with no Condorcet winner at all, against 95–100% in every structured model). A model that implausible is not one either camp should quote. The honest reading is that **impartial culture is where IRV looks best and where nobody should be arguing from.**

**3. In structured electorates the ordering reverses, and the reversal grows with the field.** In 1-D spatial — the classic left-right spectrum, and precisely where [center squeeze](../center_squeeze/) lives — IRV falls from 89.1% at three candidates to **47.0%** at seven, while STAR holds 74–79%. At seven candidates in 1-D, IRV elects the head-to-head winner **less than half the time**. That is the center-squeeze mechanism showing up as a statistic instead of an anecdote, and it is a much stronger result for STAR than the impartial-culture number is against it.

**4. Dimensionality, not just field size, drives IRV's collapse.** IRV does markedly better in 2-D (71.9–96.5%) than in 1-D (47.0–89.1%). Center squeeze is sharpest on a single spectrum, where "the moderate" is a well-defined position that elimination reliably cuts. Add a second issue dimension and the squeeze softens. This is worth knowing before treating any one spatial result as *the* answer.

**5. Plurality is the floor in every single cell**, bottoming out at 29.9%. Approval sits above it and below Score throughout — but its number is the least meaningful of the six, because it is set by the **cutoff rule**, a modelling choice and not a fact about Approval. Sweep it with `--approval-cutoff` and the column moves.

**6. More candidates hurt everyone except the control.** Every method's efficiency declines with field size in every model. Nothing here is a small-field phenomenon that vanishes at scale.

**7. More voters cut both ways.** Under structured models, more ballots *raise* efficiency (sampling noise fades, structure dominates: STAR 87.5% → 92.2% in `spatial2d` at 7). Under impartial culture they change almost nothing. This mirrors the [STAR-vs-RR divergence](../../../05_Ranked_Robin/star_vs_rr_divergence/README.md) finding that "fewer ballots → more disagreement" is a property of *structured* electorates, not random ones.

## Why STAR misses — and the surprise in the answer

A Condorcet winner who *reaches* STAR's runoff wins it, since they beat any opponent head-to-head. So STAR can only miss two ways, and the simulation counts them separately:

- **Top-two miss** — the CW never reached the runoff, having placed third or worse on score. This is the mechanism everyone talks about: a broadly-preferred but low-intensity compromise, everyone's tepid second choice, squeezed out of the top two. It is the [preference-vs-support](../../scores_and_ranks/preference_vs_support.md) tradeoff STAR makes deliberately.
- **Grid loss** — the CW *reached* the runoff and still lost. This sounds impossible, and it is the larger of the two in almost every cell.

| | 3 cands | 5 cands | 7 cands |
|---|:--:|:--:|:--:|
| `spatial1d`, top-two miss | 0.0% | 5.2% | 11.2% |
| `spatial1d`, **grid loss** | **5.2%** | **9.8%** | **14.9%** |
| `noise`, top-two miss | 1.2% | 4.0% | 4.7% |
| `noise`, **grid loss** | **9.0%** | **12.3%** | **11.6%** |

The resolution is that the Condorcet winner is defined on voters' **true preferences**, while STAR's runoff is counted on the **0–5 score ballot**. Each voter's scores are a monotone transform of their utilities, so rounding can never flip an *individual* ballot — it can only flatten a real preference into a tie. But it flattens *different voters at different rates*, and that is enough to move the aggregate. Run the breakdown:

```bash
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --mechanism --trials 8000 --voters 51
```

```
model       C     V |  grid losses  exact tie   reversal  unexplained
--------------------------------------------------------------------
noise       3    51 |          677        253        424            0
spatial2d   5    51 |          603        123        480            0
spatial1d   7    51 |         1066        230        836            0
```

**Roughly two-thirds of grid losses are outright reversals**, not ties — the head-to-head genuinely comes out the other way once preferences are expressed on six rungs. So **most of STAR's measured shortfall here is preference the ballot could not carry, not the top-two rule discarding a candidate.**

Read that finding carefully, in both directions. It is *not* a defence that clears STAR: a real STAR election really is counted on a 0–5 ballot, so this loss is real and lands on STAR. But it is also **not** a property of the automatic runoff, and it is inherited by every score-ballot method here — Score and Approval carry it too. It also means the comparison is structurally generous to Ranked Robin, which reads a full-resolution ranking. At seven candidates a 0–5 ballot **cannot** express a strict ranking at all; at three candidates it can, and the compression is the voter's choice rather than the ballot's limit. That is the single biggest caveat on this page.

## Caveats (read before quoting)

- **Sincere ballots only.** No strategy of any kind. Strategic voting moves these numbers and does not move them equally across methods — that is a different simulation ([`fbc_simulation.py`](../../../06_Other/simulations/README.md) covers the strategic side).
- **Scores are min-max normalized per voter** onto 0–5. Real voters do not perfectly normalize, and this rule is what produces the grid-loss effect above. It is the most consequential modelling assumption on the page.
- **Ballot resolution is not held constant across methods** — ranked methods get full-resolution preferences, score methods get six rungs. Realistic (a 0–5 ballot genuinely cannot rank seven candidates), but it means part of the STAR-vs-RR gap at large fields measures **ballot expressiveness rather than tabulation rule**.
- **Approval's number is a cutoff artifact.** There is no such thing as "Approval's Condorcet efficiency" without naming the cutoff rule.
- **The Condorcet winner is computed from utilities, not from any ballot.** Reading it off the 0–5 ballot instead would grade STAR against a target its own ballot had already shaped, and would flatter Approval by the same trick.
- **Tie-breaks are lowest-column-index throughout** — arbitrary, but identically arbitrary for every method, which is what keeps the comparison fair. STAR alone uses the real engine's tie-break rungs (it borrows the engine-verified model from [`star_vs_rr_divergence.py`](../../../06_Other/simulations/star_vs_rr_divergence.py), guarded by `tests/test_sim_star_model.py`).
- **Four models is not the world.** Real electorates are none of these.

## How this squares with the literature

The classic source for Condorcet-efficiency numbers is **Samuel Merrill III**, *Making Multicandidate Elections More Democratic* (Princeton, 1988), building on his 1984 *AJPS* article — the work that established the impartial-culture and spatial-model results for Plurality, Hare/IRV, Borda, Approval and Condorcet rules. The `noise` block above reproduces the *shape* of Merrill's impartial-culture findings independently: Plurality in the high 70s and IRV in the mid 90s at three candidates, both declining with field size. That agreement is worth something, since nothing here was fitted to it. **Check the figures against Merrill directly before quoting exact numbers** — the ballot-derivation rules differ, and this page's are stated above.

For the modern empirical treatment, [Green-Armytage, Tideman & Cosman (2016)](condorcet_reading_list.md) test 54 rules across five data-generating processes. **The lean, disclosed:** Merrill is broadly sympathetic to Condorcet and Approval methods and predates STAR entirely; Green-Armytage and Tideman are Condorcet-sympathetic authors whose paper reports findings that favour Hare. Neither is a STAR source, which is exactly why they are the right ones to check against.

## Where this lands

STAR is **not** Condorcet-compliant and this repo does not claim otherwise ([STAR's honest limits](../../STAR_Voting/properties_and_limits/STAR_honest_limits.md), [Campbell–Kelly](campbell_kelly_theorem.md)). What these numbers support is narrower and more defensible than the slogan:

> In realistic electorates, STAR elects the Condorcet winner **most of the time** — 92–99% at three candidates, 74–92% as the field grows — and it is the **most Condorcet-efficient non-Condorcet method measured here in every structured model**. Under impartial culture at small fields, RCV-IRV does better; under a single-issue spectrum with a crowded field, RCV-IRV elects the head-to-head winner less than half the time.

If what you want is a *guarantee* rather than a rate, that is what [Ranked Robin](../../../05_Ranked_Robin/concepts/ranked_robin.md) is for — and the 100.0% control column is the proof. The price of that guarantee, and why STAR does not pay it, is the subject of [what makes a good winner](../what_makes_a_good_winner.md).

---

**See also:** [Topic hub: Condorcet efficiency](README.md) · [30 worked STAR ≠ Ranked Robin elections](../../../05_Ranked_Robin/star_vs_rr_divergence/README.md) · [the divergence ledger](../../../method_comparisons/divergence_review/INDEX.md) (real library elections where the methods disagree) · [center squeeze](../center_squeeze/) · [the Smith set](../smith_set.md) · [reading list](condorcet_reading_list.md) · [simulations folder](../../../06_Other/simulations/README.md)
