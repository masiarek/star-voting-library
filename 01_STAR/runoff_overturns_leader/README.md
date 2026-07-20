# When the top-scoring candidate isn't the winner

This is STAR's single most important lesson — the one BetterVoting itself asks about when it pops up *"Why is the top-scoring candidate different from the winner?"* (Presenting with BetterVoting? [Explaining Runoff Reversal to Voters](explaining_to_voters.md) has a corrected, plain-language version of that popover.)

**Teaching this?** The step-by-step presenter's guide — the order to teach it in, why it's a *good* thing, and the devil's-advocate questions with answers — is [Teaching Runoff Reversal — a step-by-step guide](teaching_runoff_reversal.md).

**Real BetterVoting cases — the `Runoff_01`–`Runoff_08` two-view series** now live in a sibling folder: **[runoff_reversal_bv_cases/](../runoff_reversal_bv_cases/)** — real BV elections, each a two-view lesson (BetterVoting screenshots beside an independent count from Larry Hastings' open-source `starvote` engine, extended in this repo — the "LH" tabulator) walking the *how much vs how many* arc, from the smallest possible reversal to the 61-candidate CA-Governor field. The small teaching demos that have no live BetterVoting election stay **here** (below).

Concept hub for all of it: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/the_count/STAR_Automatic_Runoff.md).

**The name for it:** we call this a **Runoff Reversal** — the Scoring-Round leader *loses* the Automatic Runoff to the finalist more voters prefer. (In technical or debate writing, the precise phrasing is "the runoff overturns the score leader," to avoid colliding with *reversal symmetry* in social-choice theory.)

The short answer is in the name of the method. **STAR = Score Then Automatic Runoff.** The count has just two steps:

1. **Scoring Round.** Add every candidate's stars. The two highest-scoring candidates become the **Finalists**.
2. **Automatic Runoff.** Now look only at those two. Each ballot's *full* vote goes to whichever finalist it scored higher. The finalist more voters prefer wins.

That second step is the whole point. The candidate with the biggest pile of stars is the one who *leads the score round* — but leading the score round only makes you a **finalist**, not the winner. The winner is whichever finalist **more voters actually prefer**. Usually that's the same candidate. Sometimes it isn't — and *that* is the lesson.

## The one-screen version (your real election)

This is the actual recorded race in [`03_c7_b3_ice-cream-live.yaml`](cases/03_c7_b3_ice-cream-live.yaml) (BetterVoting id `c3m79f`), three voters:

```
          ChocoDrk  ChocoAlm  ChocoHzn  ...
voter 1       4         5         3
voter 2       0         3         0
voter 3       5         0         0
score total   9         8         3      ← ChocoDrk leads the score round
```

**Score round:** ChocoDrk has the most stars (9), so it tops the round. ChocoAlm is second (8). Those two are the finalists.

**Automatic runoff — ChocoDrk vs ChocoAlm only:**

- Voter 1 scored ChocoAlm 5, ChocoDrk 4 → prefers **ChocoAlm**
- Voter 2 scored ChocoAlm 3, ChocoDrk 0 → prefers **ChocoAlm**
- Voter 3 scored ChocoDrk 5, ChocoAlm 0 → prefers **ChocoDrk**

Two of three voters prefer ChocoAlm, so **ChocoAlm wins, 2–1 (67% to 33%)** — even though ChocoDrk had more total stars.

Why is that the *right* answer? ChocoDrk's lead came from one superfan giving it a 5. ChocoAlm is the candidate **more people actually prefer when it comes down to the two of them**. The runoff makes sure the winner has majority support, not just a loud minority — and it does it without anyone having to vote dishonestly.

## The lessons in this folder

Each file is a tiny, self-contained election you can run through the engine. They're built so the score-round leader **loses** the runoff — except the last one, which is the control case where the leader **wins** (so you can see the runoff isn't rigged).

The **Page** (left) is the readable write-up with ballots + full results; the raw **`.yaml`** (right) is the tabulatable source.

| Page (read this) | Field | What happens | src |
|------|-------|--------------|:--:|
| [01a — more stars, fewer voters](cases/cases_pages/01a_c3_b3_more-stars-fewer-voters.md) | 3 cand, 3 voters | The atom: Almond leads 13 stars, **Brownie** wins the runoff 2–1 | [`.yaml`](cases/01a_c3_b3_more-stars-fewer-voters.yaml) |
| [01b — overturn holds at scale](cases/cases_pages/01b_c3_b9_overturn-holds-at-scale.md) | 3 cand, 9 voters | Same election, bigger crowd: Almond leads 39–33, **Brownie** wins 6–3 (67/33) | [`.yaml`](cases/01b_c3_b9_overturn-holds-at-scale.yaml) |
| [02 — leader overturned](cases/cases_pages/02_c5_b5_leader-overturned.md) | 5 cand, 5 voters | Austin leads 22 stars, **Boston** (the broad compromise) wins the runoff 3–2 | [`.yaml`](cases/02_c5_b5_leader-overturned.yaml) |
| [03 — ice-cream, live](cases/cases_pages/03_c7_b3_ice-cream-live.md) | 7 cand, 3 voters | The real race: ChocoDrk leads 9, **ChocoAlm** wins 2–1 | [`.yaml`](cases/03_c7_b3_ice-cream-live.yaml) |
| [04 — runoff confirms leader](cases/cases_pages/04_c4_b3_runoff-confirms-leader.md) | 4 cand, 3 voters | **Control:** Blue leads *and* wins — the runoff confirms the leader | [`.yaml`](cases/04_c4_b3_runoff-confirms-leader.yaml) |
| [05 — low scores (BV1265)](cases/cases_pages/05_c3_b5_low-scores-bv1265.md) | 3 cand, 5 voters | A *real* BetterVoting election with all-low scores: C leads (7), **A** wins the runoff 3–2 | [`.yaml`](cases/05_c3_b5_low-scores-bv1265.yaml) |
| [reversal — the *convincing* case](cases/cases_pages/reversal_convincing_c3_b100.md) | 3 cand, 100 voters | Intense-minority Max leads on stars 335–255, **Nora** (broad) wins the runoff 55–45 — the runoff clearly earns its keep | [`.yaml`](cases/reversal_convincing_c3_b100.yaml) |
| [reversal — the *jarring* case](cases/cases_pages/reversal_jarring_c3_b100.md) | 3 cand, 100 voters | Near-consensus Uma leads 449–255 (avg **4.5**) yet polarizing **Rye** wins 51–49 — STAR choosing majority over utility, the honest drawback | [`.yaml`](cases/reversal_jarring_c3_b100.yaml) |

The last two are the contrasting pair behind the [second-round FAQ](../../00_start_here/STAR_Voting/the_count/STAR_second_round_FAQ.md) — one reversal almost everyone accepts, one that's a genuine philosophical trade-off (a token no-hoper keeps each a proper three-way race).

Two more, in the main folder, push the field even wider:

- [**06b — nine-candidate overturn**](../_main/cases/cases_pages/06b_c9_runoff-overturns-leader.md) ([`.yaml`](../_main/cases/06b_c9_runoff-overturns-leader.yaml)) — nine candidates: Andre leads with 9 stars, **Carmen** wins the runoff (Carmen is also the candidate who beats every other one-on-one).
- [**06a — nine-candidate confirm**](../_main/cases/cases_pages/06a_c9_b3_large-field-equal-support.md) ([`.yaml`](../_main/cases/06a_c9_b3_large-field-equal-support.yaml)) — another nine-candidate field where the runoff **confirms** the leader.

## Why it starts at three candidates

With only **two** candidates there's nothing to teach here: both are automatically finalists, so the runoff is just "which of the two do more voters prefer" — plain majority rule, and the star totals never get to matter. The interesting behavior only appears once the score round has to *choose* two finalists out of a larger field, i.e. **three candidates or more**. That's why the smallest lesson here is 3 candidates.

## "Is overturning the leader fair?"

It's the opposite of unfair — it's the safeguard. A high score total can come from a small group of enthusiasts. The runoff asks a different, majority-protecting question: *of the two finalists, which one do more voters prefer?* When the score leader really is the most-preferred candidate, the leader wins (that's `04` and `06a`). The runoff only changes the answer when enthusiasm and majority preference point at different candidates — and in that case majority preference is exactly what you want to win.

A related point: because your runoff vote is decided by the scores you already gave, you never have to lowball a candidate to "protect" your favorite. Scoring honestly is also the smart strategy.

## Going deeper — read the full count (201)

Everything above is the *minimal* view: scores → finalists → runoff → winner, which is all a first-time voter needs. But every example here also writes a complete **audit report** to its `_tabulated.txt` sibling (in `runoff_overturns_leader_tabulated/`) — the pairwise **preference matrix**, the **score distribution**, and the engine's plain-English **Majority Preference** block stating exactly which candidate led on score and which won the runoff. Learning to read that report is **Voting 201**: see the annotated walkthrough [How to read a STAR report](../../00_start_here/tabulation_engines/LH_starvote/reading_a_star_report.md) (it uses this folder's BV1265 example), plus [CURRICULUM 201.1 — Reading the results](../../00_start_here/CURRICULUM.md) and the step-by-step [STAR vs RCV-IRV count](../../00_start_here/topics/tabulation_star_vs_irv.md). Don't put the full report in front of a 101 beginner — point them here when they're ready.

## How often does it happen? (301)

Often enough to matter — but the exact rate depends entirely on your modelling assumptions, which is a lesson in itself. A brute-force simulation ([`06_Other/simulations/runoff_reversal_simulation.py`](../../06_Other/simulations/runoff_reversal_simulation.py)) measures it: under a realistic *spatial* electorate of ~100 voters, a clean Runoff Reversal happens in roughly **1 election in 11**; under white-noise *Impartial Culture* it's higher, and at tiny electorates the figure is dominated by ties. The takeaway for a debate: never quote a bare percentage without naming the model, the electorate size, and how ties were counted. Full writeup: [Simulations — measure it, don't guess it](../../06_Other/simulations/README.md#runoff-reversal-frequency-simulation).

## Run them yourself

From the engine directory:

```
python starvote_larry_hastings.py "01_Single_winner/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml"
```

Watch for the engine's **Majority Preference** note — it prints exactly which candidate earned the highest score and which one won the runoff, whenever the two differ.
