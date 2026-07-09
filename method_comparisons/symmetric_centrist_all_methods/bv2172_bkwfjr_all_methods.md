# Condorcet centrist, full form (100 voters, 47/47/3/3) — every BV method, one electorate

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/bkwfjr) · **[results ↗](https://bettervoting.com/bkwfjr/results)** (election `bkwfjr`, Test ID **BV2172**).

The profile as drawn in the ["Should we always elect the Condorcet winner?" explainer](https://youtu.be/NlisR8vbpN4?t=53) — 100 voters, three candidates, run through **all seven methods BetterVoting supports**. Avery is the left pole, Blake the right pole, Casey the centrist. Casey is the Condorcet winner (beats each pole 53–47) but has only 6 first choices. The minimal 8-voter twin ([BV2171](bv2171_h93tm4_all_methods.md)) shows the identical symptom with the fewest possible ballots.

## The ballots

| # voters | 1st | 2nd | 3rd |
|---:|:--:|:--:|:--:|
| 47 | Avery | Casey | Blake |
| 47 | Blake | Casey | Avery |
| 3 | Casey | Avery | Blake |
| 3 | Casey | Blake | Avery |

First choices: Avery 47, Blake 47, **Casey 6**. Pairwise: Casey 53–47 over each pole; Avery 50–50 Blake.

## Seven methods, two outcomes

| Method | Ballot type | Winner | Why |
|---|---|:--:|---|
| STAR | scores 5/3/1 | **Casey** | Score round Casey 312 vs 294/294; runoff 53–47 |
| STAR-PR (1 seat) | scores 5/3/1 | **Casey** | 1 seat ⇒ the STAR winner |
| Approval (approve top two) | 0/1 | **Casey** | Everyone's top two include Casey → Casey 100, poles 50 |
| Ranked Robin | ranks | **Casey** | Condorcet winner, 2–0 |
| RCV-IRV | ranks | **tie 50–50** | Casey eliminated (6); poles deadlock — random on BV |
| STV (1 seat) | ranks | **tie 50–50** | = IRV single-winner |
| Choose-One | 0/1 | **tie 47–47** | Casey last (6); poles tie — random on BV |

The four whole-ballot methods elect the candidate a majority actually prefers; the three first-choice methods throw the centrist out and deadlock the poles. On BetterVoting the three ties resolve at **random** (a coin flip, not freezable). STAR-PR at 1 seat and STV at 1 seat are degenerate (= STAR and = IRV) — included to complete the BV method set.

## LH engine — the STAR race (the divergence, on one screen)

```
[Condorcet Winner]
  Condorcet Winner: Casey — matches the STAR winner

[Divergence from STAR]
  STAR                   = Casey
  Choose-One (Plurality) = Avery   (differs from STAR)
  RCV-IRV                = Avery   (differs from STAR)
  Note: Ranked Robin (RCV-RR) agrees with STAR — RCV-IRV is the lone outlier.

Scoring Round:  Casey 312 · Avery 294 · Blake 294   (Casey advances; poles tie for 2nd)
Automatic Runoff:  Casey 53 vs Avery/Blake 47        (Casey wins)
```

(LH's RCV-IRV breaks the 50–50 tie with a stable seed → Avery; BetterVoting breaks it at random. Same profile, same conclusion — only the coin lands differently.)

## Why 47/47/3/3?

The numbers look deliberately chosen: a realistic polarized split (47% / 47% / 6%), a clean but non-landslide pairwise majority for Casey (53–47, not a blowout), a vivid first-choice squeeze (Casey with just 6), and a count that isn't reducible (gcd of 47 and 3 is 1) so it reads like real data rather than a toy. The [minimal 3/3/1/1 twin](bv2171_h93tm4_all_methods.md) strips all of that away and gets the same result — evidence the effect is structural.

## Files

- Tabulatable STAR source: [bv2172_bkwfjr_star.yaml](bv2172_bkwfjr_star.yaml) · mirror: [tabulated](symmetric_centrist_all_methods_tabulated/bv2172_bkwfjr_star_tabulated.txt)
- Frozen BV export: [bv2172_bkwfjr_bv_export.json](bv2172_bkwfjr_bv_export.json)
- Minimal 8-voter twin: [BV2171](bv2171_h93tm4_all_methods.md) · four-method original: [BV2170](../symmetric_centrist_bv2170/bv2170_pp2q4q_symmetric_centrist.md)
- Debate context: [FairVote Condorcet claim-check](../../00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md)
