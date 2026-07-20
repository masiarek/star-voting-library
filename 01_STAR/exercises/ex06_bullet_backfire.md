# Exercise 6 — Bullet voting backfires

*A club books a speaker. Ari's four fans genuinely like Bree too — their honest ballot is Ari 5, Bree 3, Cash 0. But the night before the vote, one of them argues: "scoring Bree helps Ari's rival — zero her, and Ari walks in." All four bullet vote. Predict what they wake up to.*

**▶ Live on BetterVoting:** honest [vote](https://bettervoting.com/x4dkfd) · **[results ↗](https://bettervoting.com/x4dkfd/results)** · strategic [vote](https://bettervoting.com/7f4f7q) · **[results ↗](https://bettervoting.com/7f4f7q/results)** (elections `x4dkfd` / `7f4f7q`, Test IDs BV2193–94; each also carries RCV-IRV and Ranked Robin races).

**You practice:** [strategic voting](../../00_start_here/topics/strategic_voting.md) in STAR — specifically **bullet voting** (supporting only your favorite) — and *why* the automatic runoff makes it a gamble rather than a free lift.

Work each part on paper before opening its solution. Both YAMLs are runnable; their `expected_winners` keys are regression-tested, and the `_tabulated` mirrors are the full audit reports.

## The ballots

Nine voters, three speakers, scores 0–5 (rows are candidates, columns are voter blocs):

**Honest profile:**

| | ×4 Ari fans | ×4 Cash fans | ×1 Bree fan |
|---|:---:|:---:|:---:|
| **Ari** | 5 | 0 | 0 |
| **Bree** | 3 | 2 | 5 |
| **Cash** | 0 | 5 | 1 |

**Strategic profile** — identical except the Ari fans bullet vote: their column becomes **Ari 5, Bree 0, Cash 0**.

## Your task

- **(a)** Tabulate the honest profile (STAR: scoring round, finalists, runoff). Who wins, and what do Ari's fans get?
- **(b)** Before computing: **write down** who you think wins after the four fans switch to bullet ballots — and who you think Ari's fans *believe* will win.
- **(c)** Tabulate the strategic profile. Walk through exactly where the plan works and where it detonates.
- **(d)** The gamble had a hidden precondition. State the general rule: *when* is bullet voting in STAR safe, and when is it playing with fire?

## Solutions

<details>
<summary><b>(a) Honest — Bree wins, 5–4; Ari's fans get their second choice</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Bree          -- 25 -- First place
   Cash          -- 21 -- Second place
   Ari           -- 20
 Bree and Cash advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Bree          -- 5 -- First place
   Cash          -- 4
   Equal Support -- 0
 Bree wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Bree 5 (56%) vs Cash 4 (44%); majority = 5.
```

Ari misses the runoff by one point (20 vs Cash's 21), and the broad compromise **Bree beats Cash 5–4** — the Ari fans' 3s are precisely what put her there. Their honest ballots bought their second choice. (A side note the engine's divergence block volunteers: on these same honest opinions, *RCV-IRV elects Cash* — Bree is squeezed out on first choices, [exercise 5](ex05_center_squeeze.md)'s lesson making a cameo. The honest STAR outcome these fans are about to gamble away is one other methods wouldn't even have found.)

</details>

<details>
<summary><b>(b) The prediction</b></summary>

The fans' theory: zeroing Bree drops her below Ari, Ari reaches the runoff, and Ari's four maximums carry the day. Write down your own call — winner, finalists, margin — then open (c).

</details>

<details>
<summary><b>(c) Strategic — Cash wins; the plan works halfway, then detonates</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Cash          -- 21 -- First place
   Ari           -- 20 -- Second place
   Bree          -- 13
 Cash and Ari advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Cash          -- 5 -- First place
   Ari           -- 4
   Equal Support -- 0
 Cash wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Cash 5 (56%) vs Ari 4 (44%); majority = 5.
```

The first half works perfectly: Bree crashes 25 → 13, out of the runoff; Ari is a finalist. Then the trap: **the runoff Ari inherits is against Cash**, and zeroing Bree never created a single Ari-over-Cash preference — those are still 4 (Ari's fans) versus 5 (Cash's fans plus the Bree fan, who scored Cash 1 > Ari 0). **Cash wins 5–4.** The fans demoted their sure second choice and elected their zero. Under the honest count they got Bree; the "clever" ballots got them their nightmare.

</details>

<details>
<summary><b>(d) The general rule</b></summary>

Bullet voting is *safe* only when your favorite would **win the runoff against whoever replaces the candidate you zeroed** — which is exactly what these fans never checked (Ari loses to Cash 4–5 no matter what). Zeroing a compromise you actually prefer to the field does two things at once: it may promote your favorite into the runoff, and it *simultaneously* removes your insurance if your favorite still loses there. That double edge is by design — the runoff is why STAR "discourages bullet voting" (glossary: [bullet voting / tactical minimization](../../00_start_here/GLOSSARY.md)) — and it's the honest version of that claim: not *impossible* to game (nothing is — [Gibbard](../../00_start_here/topics/gibbard_satterthwaite_theorem.md)), but a strategy that pays only with information voters rarely have, and costs dearly when the guess is wrong. The balanced treatment across methods is [strategic voting](../../00_start_here/topics/strategic_voting.md).

</details>

## Reading this fairly

Note what this exercise is and isn't: a *sincere-vs-strategic* pair, so per the [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) it says so loudly — the failure here is the *strategy's*, not the method's, and the same "zero the compromise" gamble misfires in Approval and ranked methods too. One honest profile, one coordinated deviation, both runnable; margins of one point, engineered for clarity.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex06_bullet_honest.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex06_bullet_backfire.yaml
```

Sources: [ex06_bullet_honest.yaml](cases/ex06_bullet_honest.yaml) · [ex06_bullet_backfire.yaml](cases/ex06_bullet_backfire.yaml). Full audit reports: [honest](cases/cases_tabulated/ex06_bullet_honest_tabulated.txt) · [strategic](cases/cases_tabulated/ex06_bullet_backfire_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast). Concept homes: [strategic voting across the Equal Vote methods](../../00_start_here/topics/strategic_voting.md) and the [second-round FAQ](../../00_start_here/STAR_Voting/the_count/STAR_second_round_FAQ.md) (why the runoff exists).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex06_bullet_backfire.md
