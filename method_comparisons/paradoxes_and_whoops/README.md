# Paradoxes & whoopses — when methods disagree 🎭

A small gallery of **low-stakes elections with surprising results** — the kind where the *same ballots* hand the win to a *different candidate depending on the method.* They're fun ("ha! three winners from one set of ballots!"), they're great teaching moments, and — read with care — they keep us **honest**.

> **The even-handedness pledge.** These examples are *not* a stick for beating one method. Every voting method fails *some* fairness criterion (that's Arrow & Gibbard — no method escapes), so this folder makes a point of letting **each camp take a turn as the punchline**. If you catch yourself only collecting IRV's faults, that's the bias to resist — add the matching STAR, Approval, and Condorcet whoopses too. Read **[Reading these fairly — the test for an honest "whoops"](reading_these_fairly.md)** before adding any case.

## The cases

| Case | Lesson | The whoops | Who takes the hit | Live |
|---|--------|-----------|-------------------|------|
| BV2155 | [Tennessee — four ways, three winners](bv2155_cphxpt_tennessee_four_ways.md) | one ballot set → Plurality=Memphis, IRV=Knoxville, STAR & Ranked Robin=Nashville | **Plurality & IRV** | [results ↗](https://bettervoting.com/cphxpt/results) |
| BV2156 | [STAR misses the Condorcet winner](bv2156_3grpbb_star_misses_condorcet.md) | the head-to-head winner is too low-scored to reach the runoff | **STAR** | [results ↗](https://bettervoting.com/3grpbb/results) |
| BV2157 | [a Condorcet cycle (rock-paper-scissors)](bv2157_mmcmpy_condorcet_cycle_rps.md) | majority rule is intransitive — *no* Condorcet winner exists | **Condorcet / Ranked Robin** | [results ↗](https://bettervoting.com/mmcmpy/results) |
| BV2158 | [IRV buries the centrist (Ossipoff)](bv2158_gr72hd_ossipoff_centrist_irv.md) | the plurality *and* Condorcet winner is eliminated; IRV elects D | **IRV** | [results ↗](https://bettervoting.com/gr72hd/results) |
| BV2159 | [many IRV pathologies in one (Brams)](bv2159_f4cjpy_brams_irv_pathologies.md) | Condorcet failure + no-show + truncation + non-monotonicity | **IRV** | [results ↗](https://bettervoting.com/f4cjpy/results) |
| BV2183 | [Forced Exhaustion Ceiling](bv2183_dfw8rj_forced_exhaustion_ceiling.md) | *(constructed ceiling)* a 2-rank cap force-exhausts 21 of 50 ballots — more than the winner's own votes | **IRV** | [results ↗](https://bettervoting.com/dfw8rj/results) |

Cases 01–03 are STAR/score files (engine-verified, in the test library); 04–05 are **ranked-ballot** RCV-IRV cases (IRV rounds engine-verified, Condorcet winners checked by pairwise tally). Each carries a **fairness box**.

## Balance ledger

The even-handedness pledge isn't a vibe — it's a count. Keep this honest, and when it tilts, the **next** case should hit the over-represented direction's *opposite*.

| Method | Times it's the punchline | Cases |
|--------|:---:|-------|
| Plurality | 1 | 01 |
| **RCV-IRV** | **3** | 01, 04, 05 |
| STAR / score | 1 | 02 |
| Condorcet / Ranked Robin | 1 | 03 |
| Approval | 0 | — |

**Balance owed (as of cases 01–05): the folder leans IRV (3).** The next additions should embarrass the *score family* — **Approval** (0 so far) and **STAR** — not IRV. Candidate follow-ups: an Approval "bland-winner" / chicken-dilemma case, or a STAR non-monotonicity construction. *Don't add another IRV whoops until this evens out.*

## How to read these (the short version)

A "whoops" is only worth teaching if it's an **honest** one. The full test is in [Reading these fairly — the test for an honest "whoops"](reading_these_fairly.md), but the gist:

- **Structural, not contrived** — happens across a region of realistic electorates, not at one knife-edge with absurd weights.
- **Sincere, not strategic** — failures under honest voting are fair game; "but you can game it" applies to *every* method (Gibbard), so it's the weakest, muddiest angle.
- **Realistic electorate** — spatial / natural distributions, not alien voter behavior.
- **Bonus: it really happened** — Burlington 2009, Alaska 2022 aren't constructions.

All three cases here pass that test (Tennessee is canonical; the STAR miss and the Condorcet cycle are foundational, sincere-vote results) — which is itself the lesson: these aren't cheap gotchas.

## Live on BetterVoting (BV2155–BV2159)

Every case in this gallery is now a **real BetterVoting election** (created 2026-07; STAR is race 1 in each, per house style, with the comparison methods as further races on the same ballots). All 16 races match an independent count from Larry Hastings' `starvote`, extended in this repo (the "LH" engine), exactly — the contrast here is **method vs method**, and BetterVoting and the engine agree on every count. Frozen exports sit beside each case as `bv215N_<bvid>_bv_export.json`.

## Run them yourself

```
cd STARVote_LH_tabulation_engine
python starvote_larry_hastings.py "../method_comparisons/paradoxes_and_whoops/bv2155_cphxpt_tennessee_four_ways.yaml"
```

Each writes a full audit copy to `paradoxes_and_whoops_tabulated/`. All three also live as flat-schema positive test cases in `YAML_library/1_positive/` (each verifies the **STAR** winner — the gallery is about *disagreement*, so the test pins STAR's answer, and the lesson narrates the others).

## Books on voting paradoxes

Voting theory is rife with mathematical anomalies, and several books catalogue them:

- **Hannu Nurmi — *Voting Paradoxes and How to Deal with Them* (1999).** The reference manual: systematically catalogues the no-show paradox, monotonicity failures, Condorcet cycles, etc., and rates how vulnerable each method is to each.
- **Donald G. Saari — *Disposing Dictators, Demystifying Voting Paradoxes* (2008).** A geometric take on social choice — argues Arrow's theorem and the paradoxes reflect positional systems *discarding information*, not democracy being broken.
- **William Poundstone — *Gaming the Vote: Why Elections Aren't Fair* (2008).** The general-audience pick: history of paradoxes and strategic voting, arguing independent- score methods (Approval, Score) sidestep paradoxes inherent to strict ranking like IRV.
- **Michel Balinski & Rida Laraki — *Majority Judgment* (2011).** Argues that turning individual rankings into a collective ranking makes Arrow/Condorcet paradoxes inevitable, and proposes grading candidates on a common scale instead.

## More whoopses to mine (sources)

- **rangevoting.org** (Warren Smith, the Center for Range Voting) — a deep trove of method-failure constructions and paradoxes.
- Burlington 2009, Alaska 2022 (real center-squeeze elections — see [Center Squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md)).
- Classic social-choice paradoxes (Condorcet, Arrow, no-show, monotonicity).

> Adding one? Run it through the engine, write the fairness box, and make sure the camp it embarrasses isn't always the same one.
