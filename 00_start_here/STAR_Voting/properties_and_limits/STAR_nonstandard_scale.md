# Unorthodox STAR — running the runoff on a scale wider than 0–5

### Voting 301 · advanced / "what if" — the scale is a parameter, not a rule

STAR ballots are **0–5** everywhere you'll meet them — [BetterVoting](https://bettervoting.com), the Equal Vote Coalition, every case in this repo. But *nothing in the STAR algorithm requires it.* The "5" is a design **convention**, and the underlying engine treats the scale as a plain parameter. This page is the "what if": run STAR on **0–9**, **0–10**, even **0–99**, see that it works, understand what actually changes — and learn how to make LH do it.

*This is deliberately non-standard. Don't ship a 0–10 STAR election and call it "STAR" without saying so — the point here is understanding, not a recommendation.*

---

## Why 0–5 in the first place?

The 0–5 range is a **usability** choice, not a mathematical one. It maps onto the five-star rating everyone already knows (movies, rideshares) plus an explicit 0, giving **six levels** — enough to express order *and* intensity without asking a voter to agonize over "is this a 7 or an 8 out of 100?" Equal Vote settled on it because it's expressive enough to matter and simple enough to fill out fast, with low ballot-error rates. It's a sweet spot, not a boundary.

**One subtle consequence of six levels.** With only six distinct scores (0, 1, 2, 3, 4, 5), a voter can put at most **six candidates in a strictly different order**. With **seven or more** candidates, some must share a score — so a 0–5 ballot can't encode every strict *ordering* that a ranked ballot can. This is the one narrow sense in which a ranked ballot out-expresses a 0–5 STAR ballot: [Clelland (2023)](https://arxiv.org/abs/2303.00108) puts it precisely — STAR offers a greater range of expression than IRV *"unless there are more than 6 candidates."* (Widen the scale and the threshold moves up: 0–9 strictly orders ten.) It rarely bites in practice — few single-winner races have seven serious contenders, and STAR trades this for what ranks can *never* capture, **strength** of support (and the [runoff, being scale-agnostic](#what-the-scale-changes-and-what-it-doesnt), doesn't care about it at all).

## What the scale changes — and what it doesn't

STAR has two rounds, and they react to the scale very differently:

- **The automatic runoff is scale-agnostic.** The runoff asks one question per ballot: *which finalist did you score higher?* That's a **preference**, and a preference doesn't care whether the gap was 5-vs-4 or 50-vs-40. Widen the scale and the runoff step is untouched.
- **The scoring round is where granularity bites.** Who the **top two finalists** are depends on total scores, and a wider scale gives intensity more room to move those totals. A candidate with a few passionate max-scores can climb past a broadly-but-mildly-liked rival when the max is 10 that they couldn't reach when the max was 5. So a wider scale can change *who advances* — and therefore, sometimes, who wins. That's exactly the effect worked in [Scale granularity can flip the winner](../../scores_and_ranks/scale_granularity_flips_the_winner.md).

So "unorthodox STAR" isn't just cosmetic: it's a real knob that trades **more expressiveness** for **more room to exaggerate** and a **less familiar ballot**.

## Worked example — STAR on a 0–10 ballot

Take the ten 0–10 ballots from the [Range/Score worked comparison](../../Range_Voting/range_voting.md) (Sullivan's Example 5.2) and run them through **STAR** instead of pure Range — Larry Hastings' engine at `maximum_score=10`:

```text
[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C -- 70 -- First place
   A -- 61 -- Second place
   D -- 58
   B -- 47
 C and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 6 -- First place
   A             -- 3
   No Preference -- 1
 C wins.

[STAR Voting: Winner]
 C
```

C leads the scoring round at 70, A is second at 61, and in the runoff C is preferred 6–3 (one voter scored them equally). Winner: **C** — the same candidate pure Range and median-Range pick on this electorate. The runoff simply confirmed the score leader; the wide scale changed none of that here. (For a case where scale *does* flip the outcome, see the granularity page linked above.)

## How to make LH do it

The catch: this repo's **teaching CLI** (`starvote_larry_hastings.py`) deliberately **rejects scores above 5** — a guardrail (`validate_star_rows(..., max_score=5)`) that keeps YAML demos on the 0–5 convention and catches typos. That cap is *ours*, not the engine's. Larry Hastings' underlying `starvote` library takes the scale as an argument, so you run the wide-scale election by calling it directly:

```python
import starvote

ballots = [
    {"A": 10, "B": 0,  "C": 0,  "D": 0},
    {"A": 5,  "B": 7,  "C": 10, "D": 8},
    {"A": 0,  "B": 4,  "C": 10, "D": 8},
    {"A": 7,  "B": 7,  "C": 1,  "D": 10},
    {"A": 7,  "B": 9,  "C": 7,  "D": 4},
    {"A": 6,  "B": 6,  "C": 9,  "D": 4},
    {"A": 8,  "B": 3,  "C": 10, "D": 3},
    {"A": 0,  "B": 8,  "C": 5,  "D": 5},
    {"A": 8,  "B": 0,  "C": 10, "D": 6},
    {"A": 10, "B": 3,  "C": 8,  "D": 10},
]

winner = starvote.election(starvote.star, ballots, maximum_score=10)
# → ['C']

# add verbosity=1 for the round-by-round tabulation shown above:
starvote.election(starvote.star, ballots, maximum_score=10, verbosity=1)
```

That's the whole trick — `maximum_score=N` for any N. (If you'd rather drive it through the YAML CLI, you'd raise or remove the `max_score=5` argument in `validate_star_rows`; but the library call above is cleaner for a one-off experiment and doesn't touch the guardrail everyone else relies on.) The same parameter is how the repo's divergence tools (`tools_adam/find_divergence.py`) already sweep across scales, and how the [Range engine](../../../06_Other/Range/Range_tabulation_engine/) tabulates 0–10 ballots natively.

## So should you widen the scale?

Rarely, and only on purpose. The honest ledger:

- **For** a wider scale: more expressive; the median variant of Score becomes more meaningful; matches an existing 0–10 / 0–100 culture (some surveys, sports scoring).
- **Against**: a less familiar ballot (higher error rates, slower to fill); **more room for strategic min/max exaggeration**, which pulls a score ballot back toward Approval; and it can shift who the finalists are in ways voters don't intuit (granularity effects). STAR's runoff blunts the strategy problem, but a wide scale hands some of that advantage back.

0–5 is where Equal Vote landed for good reasons. The value of this exercise isn't a better STAR — it's seeing **exactly which part of STAR the scale touches** (the finalists) and which part it can't (the runoff's majority test).

---

## Where this fits

- **Level:** Voting 301 — advanced / "what if." Read after the [scoring round](../the_count/STAR_Scoring_Round.md) and [automatic runoff](../the_count/STAR_Automatic_Runoff.md) are second nature.
- **Pairs with:** [Scale granularity can flip the winner](../../scores_and_ranks/scale_granularity_flips_the_winner.md) (the case where the scale *does* change the outcome) and the [Range/Score worked comparison](../../Range_Voting/range_voting.md) (the same 0–10 electorate as pure Score).
- **Engine note:** the 0–5 cap is the fork's teaching guardrail, not a limit of Larry's engine — see the Engines section of the repo's working notes.

Cross-references:
- [STAR — start here](../STAR_start_here.md) · [the scoring round](../the_count/STAR_Scoring_Round.md) · [the automatic runoff](../the_count/STAR_Automatic_Runoff.md)
- [Range / Score voting](../../Range_Voting/range_voting.md) · [the fidelity ladder](../../scores_and_ranks/fidelity_ladder.md)
- [Curriculum 301](../../curriculum/CURRICULUM_301.md)
