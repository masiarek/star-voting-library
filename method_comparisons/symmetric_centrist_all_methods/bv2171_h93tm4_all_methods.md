# Condorcet centrist, minimal form (8 voters) — every BV method, one electorate

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/h93tm4) · **[results ↗](https://bettervoting.com/h93tm4/results)** (election `h93tm4`, Test ID **BV2171**).

The smallest electorate that still reproduces the whole center-squeeze symptom — 8 voters, three candidates, run through **all seven methods BetterVoting supports**. Avery is the left pole, Blake the right pole, Casey the centrist. Casey is the Condorcet winner (beats each pole 5–3) but has the fewest first choices (2). This is the minimal foil to the full 100-voter version ([BV2172](bv2172_bkwfjr_all_methods.md)); proving the effect is *structural*, not an artifact of big round numbers.

## The ballots

| # voters | 1st | 2nd | 3rd |
|---:|:--:|:--:|:--:|
| 3 | Avery | Casey | Blake |
| 3 | Blake | Casey | Avery |
| 1 | Casey | Avery | Blake |
| 1 | Casey | Blake | Avery |

First choices: Avery 3, Blake 3, **Casey 2**. Pairwise: Casey 5–3 over each pole; Avery 4–4 Blake.

## Seven methods, two outcomes

| Method | Ballot type | Winner | Why |
|---|---|:--:|---|
| STAR | scores 5/3/1 | **Casey** | Score round Casey 28 vs 22/22; runoff 5–3 |
| STAR-PR (1 seat) | scores 5/3/1 | **Casey** | 1 seat ⇒ the STAR winner |
| Approval (approve top two) | 0/1 | **Casey** | Everyone's top two include Casey → Casey 8, poles 4 |
| Ranked Robin | ranks | **Casey** | Condorcet winner, 2–0 |
| RCV-IRV | ranks | **tie 4–4** | Casey eliminated (2); poles deadlock — random on BV |
| STV (1 seat) | ranks | **tie 4–4** | = IRV single-winner |
| Choose-One | 0/1 | **tie 3–3** | Casey last (2); poles tie — random on BV |

The four whole-ballot methods elect the candidate a majority actually prefers; the three first-choice methods throw the centrist out and deadlock the poles. On BetterVoting the three ties resolve at **random** (a coin flip, not freezable). STAR-PR at 1 seat and STV at 1 seat are degenerate (= STAR and = IRV respectively) — included to complete the BV method set.

## LH engine — the STAR race (the divergence, on one screen)

```
[Condorcet Winner]
  Condorcet Winner: Casey — matches the STAR winner

[Divergence from STAR]
  STAR                   = Casey
  Choose-One (Plurality) = Avery   (differs from STAR)
  RCV-IRV                = Avery   (differs from STAR)
  Note: Ranked Robin (RCV-RR) agrees with STAR — RCV-IRV is the lone outlier.

Scoring Round:  Casey 28 · Avery 22 · Blake 22   (Casey advances; poles tie for 2nd)
Automatic Runoff:  Casey 5 vs Avery/Blake 3      (Casey wins)
```

(LH's RCV-IRV breaks the 4–4 tie with a stable seed → Avery; BetterVoting breaks it at random. Same profile, same conclusion — only the coin lands differently.)

## Files

- Tabulatable STAR source: [bv2171_h93tm4_star.yaml](cases/bv2171_h93tm4_star.yaml) · mirror: [tabulated](cases/cases_tabulated/bv2171_h93tm4_star_tabulated.txt)
- Frozen BV export: [bv2171_h93tm4_bv_export.json](cases/bv2171_h93tm4_bv_export.json)
- Full 100-voter twin: [BV2172](bv2172_bkwfjr_all_methods.md) · four-method original: [BV2170](../symmetric_centrist_bv2170/bv2170_pp2q4q_symmetric_centrist.md)
- Debate context: [FairVote Condorcet claim-check](../../00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md)
