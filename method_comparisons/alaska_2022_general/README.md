# Alaska 2022 general — the mirror image: IRV got it right

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/m3hb6y) · **[results ↗](https://bettervoting.com/m3hb6y/results)** (election `m3hb6y`, Test ID BV2214 — all four races).

**▶ Runnable companion to a published analysis.** [Clelland (2023)](https://arxiv.org/abs/2303.00108) analyzed this general election too (her §6 postscript): unlike the special, it had *no* Condorcet failure — Peltola was the Condorcet winner and every method agrees. This case makes that hands-on, on ballots that match her Table 8.

> **Which Alaska election is this?** The **November 2022 US House *general*** — the one where RCV-IRV worked *fine*. It is the companion to the [August *special*](../alaska_2022/README.md) (where IRV misfired). Confused? See the [full map](../../06_Other/RCV_IRV/concepts/case_studies/alaska_rcv_elections.md).

**One line:** same three candidates as the special, six months later — and this time **all four counts agree on Peltola.** Because the electorate had shifted, **Peltola was now the Condorcet winner** (she beats both rivals head-to-head), so Plurality, RCV-IRV, Ranked Robin, and STAR *all* elect her. This is the honest other half of the story: IRV's [center-squeeze](../../07_Concepts/topics/center_squeeze/README.md) failure is **real but conditional** — it strikes only when a centrist Condorcet winner has too few first choices, which was true in August and *not* true in November.

---

## Why this is the special's mirror image

| | August **special** ([case](../alaska_2022/README.md)) | November **general** (this case) |
|---|---|---|
| Condorcet winner | **Begich** (centrist, beats both) | **Peltola** (beats both) |
| First-choice leader | Peltola | Peltola |
| Plurality | Peltola | Peltola |
| RCV-IRV | Peltola | Peltola |
| Ranked Robin | **Begich** | Peltola |
| STAR | **Begich** | Peltola |
| Result | methods **split 2-2**; IRV cut the Condorcet winner | methods **all agree**; IRV elected the Condorcet winner |

In the special, the Condorcet winner (Begich) had the *fewest* first choices, so IRV eliminated him — the squeeze. In the general, the Condorcet winner (Peltola) *also* led first choices, so nothing squeezed her out and every method converges. **Same mechanism, opposite outcome — because the configuration was different.**

## The reduced model

200 voters, three candidates (the real general's fourth candidate, Bye, finished last and is dropped — exactly as Equal Vote's [Real RCV](https://realrcv.equal.vote/alaska22general) visualizer does). Reconstructed from realrcv's own 200-dot model and matched to its stated results — and, it turns out, to the **authoritative Cast Vote Record profile in [Clelland (2023), Table 8](https://arxiv.org/abs/2303.00108)**: every one of the nine blocs lines up (Peltola-only 66,349 → our 50; Begich › Palin 43,072 → our 33; Palin-only 22,751 → our 17; …). So this model is a faithful ~1,318:1 reduction of the real general, independently confirmed:

| Voters | Ballot | | Voters | Ballot | | Voters | Ballot |
|--:|--|--|--:|--|--|--:|--|
| 50 | Peltola | | 11 | Begich | | 17 | Palin |
| 42 | Peltola › Begich | | 33 | Begich › Palin | | 32 | Palin › Begich |
| 6 | Peltola › Palin | | 6 | Begich › Peltola | | 3 | Palin › Peltola |

First choices: **Peltola 98, Palin 52, Begich 50.**

## The four counts

| Method | Winner | Why |
|---|:---:|---|
| **Choose-One (Plurality)** | **Peltola** | Most first choices (98) |
| **RCV-IRV (Hare)** | **Peltola** | Begich (fewest) eliminated; 11 exhaust; Peltola beats Palin **104–85** |
| **Ranked Robin** | **Peltola** | Beats Begich 101–82 **and** Palin 104–85 — the Condorcet winner |
| **STAR** | **Peltola** | Runoff winner (see below) |

BetterVoting and an independent open-source count agree on all four, every race deterministic (`tieBreakType: none`).

## View 2 — an independent count (the full tabulation)

*The same ballots, re-counted by the open-source engine this repo runs — **Larry Hastings' `starvote`, extended here** (hence "LH" elsewhere in the repo) — so the result is verifiable, not taken on trust.*

<!-- report:bv2214_m3hb6y_alaska_2022_general -->
```text
[Divergence from STAR]
  STAR     = Peltola
  Approval = Begich   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Begich)
 - Runoff Round Winner   = (Peltola)
  Candidate Begich earned the highest total score, but
  Candidate Peltola won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 200 ballots.
Count × Peltola,Begich,Palin
   50 ×       5,     0,    0
   42 ×       5,     4,    0
   33 ×       0,     5,    4
   32 ×       0,     4,    5
   17 ×       0,     0,    5
   11 ×       0,     5,    0
    6 ×       5,     0,    4
    6 ×       4,     5,    0
    3 ×       4,     0,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Begich        -- 546 -- First place
   Peltola       -- 526 -- Second place
   Palin         -- 416
 Begich and Peltola advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Peltola       -- 101 -- First place
   Begich        --  82
   Equal Support --  17
 Peltola wins.
   Runoff math:
     200  ballots cast
   −  17  Equal Support (no preference between the two finalists)
     ───
     183  voters with a preference  (majority = 92)
           Peltola 101 (55%)  ·  Begich 82 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Peltola
```
<!-- /report -->
**A nice nuance — STAR self-correcting.** Begich actually *leads* the STAR scoring round (546) as everyone's broad second choice, just like in the special. But this time the runoff overturns him:

<!-- report:bv2214_m3hb6y_alaska_2022_general -->
```text
[Divergence from STAR]
  STAR     = Peltola
  Approval = Begich   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Begich)
 - Runoff Round Winner   = (Peltola)
  Candidate Begich earned the highest total score, but
  Candidate Peltola won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 200 ballots.
Count × Peltola,Begich,Palin
   50 ×       5,     0,    0
   42 ×       5,     4,    0
   33 ×       0,     5,    4
   32 ×       0,     4,    5
   17 ×       0,     0,    5
   11 ×       0,     5,    0
    6 ×       5,     0,    4
    6 ×       4,     5,    0
    3 ×       4,     0,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Begich        -- 546 -- First place
   Peltola       -- 526 -- Second place
   Palin         -- 416
 Begich and Peltola advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Peltola       -- 101 -- First place
   Begich        --  82
   Equal Support --  17
 Peltola wins.
   Runoff math:
     200  ballots cast
   −  17  Equal Support (no preference between the two finalists)
     ───
     183  voters with a preference  (majority = 92)
           Peltola 101 (55%)  ·  Begich 82 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Peltola
```
<!-- /report -->
Begich is the *most-approved* candidate (that's why [Approval](../../04_Approval/01_Learn/README.md) elects him), but Peltola is the *majority-preferred* one — and STAR's runoff, like every majority method here, picks Peltola. In the special, that same runoff step is what let STAR reach the Condorcet winner Begich; here it keeps STAR aligned with the majority. The runoff is doing its job in both.

Full engine detail: [the full report](cases/cases_tabulated/bv2214_m3hb6y_alaska_2022_general_tabulated.txt) · run it: [`bv2214_m3hb6y_alaska_2022_general.yaml`](cases/bv2214_m3hb6y_alaska_2022_general.yaml).

---

## The takeaway

This case exists to keep the [Alaska critique](../alaska_2022/alaska_301.md) **honest**. IRV is not broken — it handled the general (and the 2022 Senate, and 2024, and most of its races) correctly. Its center-squeeze failure is a *specific, structural* risk that materialized in the August special, not a constant. The argument for whole-ballot methods is "avoid a real failure mode at no cost to the races IRV already gets right" — and this election is the "gets right" half of that sentence.

## Related

- **The special (where IRV misfired):** [runnable model](../alaska_2022/README.md) · [101](../alaska_2022/alaska_101.md) · [201](../alaska_2022/alaska_201.md) · [301 + fairness](../alaska_2022/alaska_301.md)
- **The map:** [Alaska's RCV elections — the whole picture](../../06_Other/RCV_IRV/concepts/case_studies/alaska_rcv_elections.md)
- Source visualization: Equal Vote's [Real RCV — Alaska 2022 general](https://realrcv.equal.vote/alaska22general)
