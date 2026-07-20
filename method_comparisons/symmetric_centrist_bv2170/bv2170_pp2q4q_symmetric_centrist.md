# Symmetric centrist (47/47/3/3) — the compromise a majority prefers, squeezed out four ways

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pp2q4q) · **[results ↗](https://bettervoting.com/pp2q4q/results)** (election `pp2q4q`, Test ID **BV2170**).

The textbook "two poles and a compromise" electorate: 100 voters, three candidates — **Avery** on the left, **Blake** on the right, and **Casey** the broadly-liked centrist. Both poles rank Casey second. It is the classic profile from the ranked-ballot literature (a Condorcet winner with almost no first-choice support), and it is *perfectly symmetric* between the two poles — which is what makes it such a sharp teaching case: the same 100 ballots elect **Casey**, one of the two poles, or nobody-in-particular, depending only on the counting method.

Casey is the **Condorcet winner**: a majority prefers Casey head-to-head over each rival (Casey beats Avery 53–47 and beats Blake 53–47). Yet Casey holds only **6 first-choice votes**. The methods that look only at first choices — RCV-IRV and Choose-One — throw Casey out immediately, and because the electorate is a mirror image, the two poles then **deadlock in an exact tie**. The methods that look at the whole ballot — STAR and Ranked Robin — elect Casey.

## The ballots

| # voters | 1st | 2nd | 3rd | reading |
|---:|:--:|:--:|:--:|:--|
| 47 | Avery | Casey | Blake | left pole, centrist second |
| 47 | Blake | Casey | Avery | right pole, centrist second |
| 3 | Casey | Avery | Blake | centrist, leans left |
| 3 | Casey | Blake | Avery | centrist, leans right |

First choices: Avery 47, Blake 47, **Casey 6**. Pairwise: Casey 53–47 over each pole; Avery 50–50 Blake.

## One electorate, four counts

| Race (BV) | Method | Winner | Determinate? |
|---|---|:--:|:--|
| Symmetric centrist — STAR | STAR | **Casey** | Yes (winner). Score round Casey 312 vs Avery/Blake 294; runoff Casey 53–47. |
| Symmetric centrist — Ranked Robin | RankedRobin (Copeland) | **Casey** | Yes. Casey 2–0, the Condorcet winner. |
| Symmetric centrist — RCV-IRV | IRV | **tie 50–50** | No — random. BV drew Blake; LH's seeded tiebreak lands on Avery. |
| Symmetric centrist — Choose-One | Plurality | **tie 47–47** | No — random. BV drew Blake. |

STAR and Ranked Robin agree on Casey. IRV and Choose-One eliminate the centrist first and end in a genuine pole tie. **On BetterVoting both ties resolved to Blake this run** (frozen in the export), but they are true 50–50 / 47–47 coin flips: a re-tally could land on Avery. That non-determinism is not a defect of the example — the deadlock of the two poles, *once the candidate a majority actually prefers has been squeezed out*, is the whole lesson.

> On freezability: STAR (Casey) and Ranked Robin (Casey) are deterministic and reproduce exactly in the LH engine. The IRV and Choose-One winners are random tiebreaks and are **not freezable** — the frozen export records this run's draw (Blake), while LH's IRV, which breaks the tie with its own stable seed rather than the published lot, records Avery. Same profile, same conclusion (a symmetric pole tie); only the coin lands differently.

---

## LH engine reports (View 2)

### STAR — Casey (the Condorcet winner)

```
--- Runoff (Preference) Matrix ---
                 |     Avery    |  * Blake    |  * Casey    |
-------------------------------------------------------------
         Avery > |     ---      |50 -  0 - 50 |47 -  0 - 53 |
       * Blake > | 50 -  0 - 50 |    ---      |47 -  0 - 53 |
       * Casey > | 53 -  0 - 47 |53 -  0 - 47 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Casey — matches the STAR winner

[Divergence from STAR]
  STAR                   = Casey
  Choose-One (Plurality) = Blake   (differs from STAR)
  RCV-IRV                = Avery   (differs from STAR)

Scoring Round
   Casey         -- 312 -- First place
   Avery         -- 294 -- Tied for second place
   Blake         -- 294 -- Tied for second place
 Casey advances, but there's a two-way tie for second.
 (pairwise 50–50, five-star 47–47 — the second finalist is lot-decided; Casey wins regardless.)

Automatic Runoff Round
   Casey         -- 53 -- First place
   Blake         -- 47
 Casey wins.
   Casey 53 (53%) vs Blake 47 (47%); majority = 51.
```

### Ranked Robin — Casey (2–0)

```
Round-Robin — every pair, head-to-head (For – Against):
   Casey  beats Avery   53 – 47
   Avery  ties  Blake   50 – 50
   Casey  beats Blake   53 – 47

Win–loss record — Copeland score = wins + ½·ties:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Casey      2–0–0         2     +12  Avery, Blake
    2  Avery      0–1–1       0.5      -6  —
    3  Blake      0–1–1       0.5      -6  —

Winner — Ranked Robin (RCV-RR): Casey
   beats every opponent head-to-head — the Condorcet winner.
```

### RCV-IRV — the centrist eliminated, poles deadlock 50–50

```
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Avery             47  Hopeful
Blake             47  Hopeful
Casey              6  Rejected      <- Condorcet winner, fewest first choices

FINAL RESULT (Casey's 6 split 3/3 to the poles)
Avery             50  Elected   (LH seeded tiebreak)
Blake             50  Rejected
```

A genuine 50–50 tie. LH's IRV breaks it with a stable seed → Avery; BetterVoting broke it at random → **Blake** this run. Not freezable.

### Choose-One (Plurality) — poles tie 47–47

```
   Avery         -- 47 -- Tied for first place
   Blake         -- 47 -- Tied for first place
   Casey         --  6
 There's a two-way tie for first.  (BV random draw → Blake; LH lot → Blake)
```

---

## Files

| Race | YAML | `_tabulated` mirror |
|---|---|---|
| STAR (lead) | [bv2170_pp2q4q_star.yaml](cases/bv2170_pp2q4q_star.yaml) | [txt](cases/cases_tabulated/bv2170_pp2q4q_star_tabulated.txt) |
| RCV-IRV | [bv2170_pp2q4q_irv.yaml](cases/bv2170_pp2q4q_irv.yaml) | [txt](cases/cases_tabulated/bv2170_pp2q4q_irv_tabulated.txt) |
| Ranked Robin | [bv2170_pp2q4q_ranked_robin.yaml](cases/bv2170_pp2q4q_ranked_robin.yaml) | [txt](cases/cases_tabulated/bv2170_pp2q4q_ranked_robin_tabulated.txt) |
| Choose-One | [bv2170_pp2q4q_plurality.yaml](cases/bv2170_pp2q4q_plurality.yaml) | [txt](cases/cases_tabulated/bv2170_pp2q4q_plurality_tabulated.txt) |

Frozen BetterVoting export (Election + Ballots + Results): [bv2170_pp2q4q_bv_export.json](cases/bv2170_pp2q4q_bv_export.json).

*BetterVoting result screenshots (View 1) can be dropped into `img/` as `img/pp2q4q_<what>.png` and linked here.*
