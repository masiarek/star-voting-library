# Exercise 10 — Later-no-harm: did the threes harm Amir, or did the zeros hide Bess?

*Nine voters, three candidates. Amir's four fans face the classic scored-ballot dilemma: they honestly like Bess second — should they say so? Run it both ways: first with the fans scoring nothing below their favorite, then with their honest 3s for Bess. One of those elections is a textbook **later-no-harm failure**. The exercise is deciding what it means.*

**You practice:** the **[later-no-harm](../../00_start_here/GLOSSARY.md)** criterion — the one RCV-IRV keeps and STAR deliberately gives up — run live in both directions, and the discipline of keeping it distinct from [favorite betrayal](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md).

Work each part on paper before opening its solution. Both YAMLs are runnable; their `expected_winners` keys are regression-tested, and the `_tabulated` mirrors are the full audit reports.

## The ballots

Nine voters, scores 0–5. Only the first column changes between the two runs:

| | ×4 Amir fans (reticent → generous) | ×2 Bess-first | ×3 Cato-first |
|---|:---:|:---:|:---:|
| **Amir** | 5 → 5 | 2 | 0 |
| **Bess** | **0 → 3** | 5 | 1 |
| **Cato** | 0 → 0 | 0 | 5 |

## Your task

- **(a)** Tabulate the **reticent** profile (fans score Amir 5, everyone else 0). Who wins, against whom, by what count?
- **(b)** Before computing: the fans now add an honest **Bess 3** to their ballots — twelve points that can only help Bess. **Write down** your prediction, and what you'd tell the fans.
- **(c)** Tabulate the **generous** profile. Name the criterion whose failure you just watched, precisely.
- **(d)** Now argue the other side: what do the honest ballots *reveal* that the reticent ones concealed? (Check Bess head-to-head against both rivals, and check what RCV-IRV does on the honest profile.)
- **(e)** Keep the ledger straight: which criterion did STAR just fail, which one does RCV-IRV fail instead, and why can't a method simply keep both?

## Solutions

<details>
<summary><b>(a) Reticent — Amir wins, 6–3, over Cato</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Amir          -- 24 -- First place
   Cato          -- 15 -- Second place
   Bess          -- 13
 Amir and Cato advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Amir          -- 6 -- First place
   Cato          -- 3
   Equal Support -- 0
 Amir wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Amir 6 (67%) vs Cato 3 (33%); majority = 5.
```

With the fans silent below the top, Bess limps in third at 13 and the runoff is Amir vs Cato — **Amir in a walk**. The fans' favorite holds the trophy.

</details>

<details>
<summary><b>(b) The prediction</b></summary>

The soothing intuition: "your 3 for Bess can't hurt Amir — Amir still has your 5." Commit to a winner before opening (c).

</details>

<details>
<summary><b>(c) Generous — Bess wins, 5–4, over Amir: a later-no-harm failure</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Bess          -- 25 -- First place
   Amir          -- 24 -- Second place
   Cato          -- 15
 Bess and Amir advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Bess          -- 5 -- First place
   Amir          -- 4
   Equal Support -- 0
 Bess wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Bess 5 (56%) vs Amir 4 (44%); majority = 5.
```

The twelve honest points lift Bess 13 → 25, past Cato and into the runoff — where the Bess-first pair and the Cato bloc (who score Bess 1 > Amir 0) outvote Amir's fans **5–4**. Adding a *later* (lower) preference cost the fans' *earlier* (higher) one the win: that is precisely a **later-no-harm violation**, and it is a real property of STAR — the fans' 3s changed *who Amir had to face*, exactly the runoff-slot mechanism of [exercise 2](ex02_tenth_ballot.md).

</details>

<details>
<summary><b>(d) The other reading — the zeros were hiding the consensus winner</b></summary>

Look at what the honest ballots reveal: **every one of the nine voters scores Bess above zero**, and Bess beats Amir head-to-head 5–4 *and* Cato 6–3 — on honest preferences, **Bess is the Condorcet winner**. The reticent profile didn't "protect Amir" in any neutral sense; it *suppressed the information* that a majority prefers Bess. And here's the twist the engine's divergence block hands you: on the honest ballots, **RCV-IRV still elects Amir** — Bess, with only two first-choices, is eliminated first (the [center squeeze](ex05_center_squeeze.md), cameo appearance). IRV keeps its later-no-harm promise *by never looking at the preferences that would break it*. Same election, both faces of the trade: STAR honors the revealed consensus and forfeits LNH; IRV keeps LNH and forfeits the consensus winner.

</details>

<details>
<summary><b>(e) The ledger</b></summary>

- **STAR fails later-no-harm** (this exercise) — knowingly: [equal.vote's own materials concede it](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md), because honoring compromise support is the design goal.
- **RCV-IRV keeps later-no-harm but fails [favorite betrayal](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md)** structurally (center squeeze pushes lesser-evil ranking), plus the squeeze itself — the price of not counting lower preferences until eliminations force it.
- They can't both be had in a method worth having: later-no-harm *requires* the count to ignore your compromise until your favorite is dead; using that information *at all* — which is what makes broad winners findable — is what LNH forbids. Keep the two criteria distinct (the repo's standing rule): LNH is about your *lower* rankings hurting your *top*; favorite betrayal is about needing to *demote your top* to get a tolerable result. A method's choice between them is a values statement, not a bug on either side.

</details>

## Reading this fairly

Sincere ballots throughout — the "failure" in (c) needs no strategy, which per the [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) makes it fair currency against STAR; this page states it as plainly as any critic would. The symmetric honesty is part (d): the same election shows what keeping LNH costs IRV. One-point margins, engineered for arithmetic you can do at a whiteboard.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex10_reticent.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex10_generous.yaml
```

Sources: [ex10_reticent.yaml](ex10_reticent.yaml) · [ex10_generous.yaml](ex10_generous.yaml). Full audit reports: [reticent](exercises_tabulated/ex10_reticent_tabulated.txt) · [generous](exercises_tabulated/ex10_generous_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast). Concept homes: the glossary's [later-no-harm entry](../../00_start_here/GLOSSARY.md), [favorite betrayal 301](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) (why the two criteria must not be conflated), and [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex10_later_no_harm.md
