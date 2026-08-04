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

<!-- report:bv2172_bkwfjr_star -->
```text
[Divergence from STAR]
  STAR                   = Casey
  Choose-One (Plurality) = Avery   (differs from STAR)
  RCV-IRV                = Avery   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2172_bkwfjr_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Avery,Blake,Casey
   47 ×     5,    1,    3
   47 ×     1,    5,    3
    3 ×     3,    1,    5
    3 ×     1,    3,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Casey         -- 312 -- First place
   Avery         -- 294 -- Tied for second place
   Blake         -- 294 -- Tied for second place
 Casey advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Avery         -- 50 -- Tied for second place
   Blake         -- 50 -- Tied for second place
   Equal Support --  0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Avery         -- 47 -- Tied for second place
   Blake         -- 47 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Avery', 'Blake', 'Casey']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Avery', 'Blake']
  Resolved: ['Avery'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Casey         -- 53 -- First place
   Avery         -- 47
   Equal Support --  0
 Casey wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Casey 53 (53%)  ·  Avery 47 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Casey
```
<!-- /report -->
(LH's RCV-IRV breaks the 50–50 tie with a stable seed → Avery; BetterVoting breaks it at random. Same profile, same conclusion — only the coin lands differently.)

## Why 47/47/3/3?

The numbers look deliberately chosen: a realistic polarized split (47% / 47% / 6%), a clean but non-landslide pairwise majority for Casey (53–47, not a blowout), a vivid first-choice squeeze (Casey with just 6), and a count that isn't reducible (gcd of 47 and 3 is 1) so it reads like real data rather than a toy. The [minimal 3/3/1/1 twin](bv2171_h93tm4_all_methods.md) strips all of that away and gets the same result — evidence the effect is structural.

## Files

- Tabulatable STAR source: [bv2172_bkwfjr_star.yaml](cases/bv2172_bkwfjr_star.yaml) · mirror: [tabulated](cases/cases_tabulated/bv2172_bkwfjr_star_tabulated.txt)
- Frozen BV export: [bv2172_bkwfjr_bv_export.json](cases/bv2172_bkwfjr_bv_export.json)
- Minimal 8-voter twin: [BV2171](bv2171_h93tm4_all_methods.md) · four-method original: [BV2170](../symmetric_centrist_bv2170/bv2170_pp2q4q_symmetric_centrist.md)
- Debate context: [FairVote Condorcet claim-check](../../07_Concepts/topics/condorcet/fairvote_condorcet_claim_check.md)
