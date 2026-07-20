# Burlington 2009 — the real election, the real ballots, three winners

The most-cited real-world IRV failure, reproduced in this repo from the **actual 8,980 ballots** (PrefLib dataset 00005, from Burlington's published records). One ranked-ballot set, three different winners depending only on the count:

→ **Interactive visualization:** Equal Vote's [Real RCV — Burlington 2009](https://realrcv.equal.vote/burlington09) (a scrollytelling walk through the final rounds) · browse [every real US RCV case study](https://realrcv.equal.vote) — most worked fine, which is the honest backdrop for why Burlington and [Alaska 2022](../alaska_2022/README.md) stand out.

| Count | Winner |
|---|---|
| Choose-One Plurality (= round 1 first choices) | **Kurt Wright** (R) — 2,950 |
| RCV-IRV (the rule actually in force) | **Bob Kiss** (P) — won the final 4,313–4,059 |
| Any Condorcet count (Ranked Robin here) | **Andy Montroll** (D) — beats *everyone* head-to-head |

Every teaching claim on this page is runnable: the yamls below are the real profile, and Larry Hastings' open-source `starvote` engine, extended in this repo (the "LH" tabulator), reproduces the official figures within ±1 (a 6-ballot / 0.07% exclusion of equal-rank overvotes not representable in ranked syntax — every margin at stake is hundreds of votes).

## What happened under IRV

```text
ROUND 1                          SEMIFINAL                    FINAL
Wright     2950                  Wright     3293              Kiss    4313  Elected
Kiss       2585                  Kiss       2981              Wright  4059
Montroll   2062                  Montroll   2553  Rejected
Smith      1306  Rejected
Simpson      35  Rejected
WriteIn      36  Rejected
```

Montroll — the one candidate a majority preferred to each rival — had the fewest of the top three *first* choices, so IRV cut him in the semifinal. That is the **[center squeeze](../../00_start_here/topics/center_squeeze/README.md)**, not as a whiteboard construction but as a certified municipal result. ([Run it](cases/burlington_2009_irv.yaml).)

## The pairwise truth

```text
Round-Robin — every pair, head-to-head (For – Against):
   Montroll  beats Kiss       4063 – 3476
   Montroll  beats Wright     4596 – 3663
   Montroll  beats Smith      4569 – 2996
   Montroll  beats Simpson    6261 –  591
   Montroll  beats WriteIn    6656 –  100

    #  Candidate  W–L–T  Copeland  Margin
    1  Montroll   5–0–0         5  +15319   <- the Condorcet winner
    2  Kiss       4–1–0         4  +10742   <- the IRV winner
    3  Wright     3–2–0         3   +8850   <- the plurality leader
```

A perfect 5–0 record ([run it](cases/burlington_2009_ranked_robin.yaml)). Wright voters preferred Montroll to Kiss 3-to-1 among those expressing a preference; Kiss voters preferred Montroll to Wright. The middle of the electorate agreed on the Democrat — and the count in force never asked the question.

## The raise: Kiss gains 750 votes and loses

Non-monotonicity, built from the same real profile ([run it](cases/burlington_2009_raise_kiss_nonmono.yaml)). Let 750 Wright-first voters **raise the winner Kiss to first** — all 281 who already ranked Kiss second (their top two swap) plus 469 of the 840 Wright-only bullet voters (now `Kiss > Wright`):

```text
SEMIFINAL                        FINAL
Kiss       3731                  Montroll  4063  Elected
Montroll   2553                  Kiss      3945
Wright     2543  Rejected
```

Kiss's new support knocks *Wright* below Montroll in the semifinal; Montroll survives to the final and beats Kiss. **Kiss gained 750 first-place votes and lost the election he had won.** More support, worse result — the additional-support paradox on certified ballots. (The selection is engineered but not exotic: the 469 bullet-ballot moves erode Montroll's 587-vote head-to-head cushion by only 469, so his final-round win survives the raise. The mirror reading — roughly the same bloc *staying home* also elects Montroll, an outcome those Wright voters preferred to Kiss — is the [no-show paradox](../../00_start_here/voting_paradoxes/no_show.md); Alaska 2022 repeated both patterns, worked in [favorite_betrayal_voting_301.md §4](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md).)

## Reading this fairly

- **Kiss won under the rules everyone campaigned under**, and IRV's defenders correctly note no method is paradox-free (Arrow — see the [social-choice shelf](../../00_start_here/books/social_choice_theory.md)). The claim this page supports is narrower and stronger: center squeeze, non-monotonicity, and no-show are **IRV-specific mechanics** — on these very ballots, Ranked Robin (and any Condorcet count) elects Montroll, and the paradox files above stop being constructible.
- **The voters did nothing wrong.** Every pathology here operates on *sincere* ballots. Wright voters ranking honestly got their last choice; had they insincerely ranked Montroll first, they'd have done better — a real-world [favorite-betrayal failure](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) in the system marketed as making honesty safe.
- **Aftermath:** Burlington repealed IRV in 2010. (It later re-adopted ranked ballots for city-council races in 2021 — the debate continues, which is exactly why the ballots deserve to stay runnable.)
- **Scope honesty:** these are ranked ballots, so only ranked-ballot counts run natively; a STAR count would require invented score levels, and this repo doesn't invent data. The score-ballot version of this electorate's lesson lives in [center squeeze](../../method_comparisons/center_squeeze_bv2137/) with designed ballots.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/burlington_2009/cases/burlington_2009_irv.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/burlington_2009/cases/burlington_2009_ranked_robin.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/burlington_2009/cases/burlington_2009_raise_kiss_nonmono.yaml
```

Full mirrors: [`burlington_2009_tabulated/`](cases/cases_tabulated/). LH-only (no BetterVoting election — 8,974 weighted ballots across 378 patterns; the value here is fidelity to the record, not castability).

---

**Sources.** Ballot data: [PrefLib dataset 00005](https://preflib.github.io/PrefLib-Jekyll/dataset/00005) (`00005-00000002.toi`), derived from Burlington's published 2009 records. Official result figures (round 1 Wright 2951 / Kiss 2585 / Montroll 2063; final Kiss 4313–4061; pairwise Montroll over Kiss 4067–3477) reproduce here within ±1 after the 6-overvote exclusion. Analyses: [Wikipedia, 2009 Burlington mayoral election](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election) (neutral overview); the non-monotonicity/no-show literature on Burlington and Alaska 2022 (Graham-Squire & McCune, arXiv:2301.12075). Sibling constructions in this repo: [monotonicity pairs](../monotonicity/), [participation/no-show pair](../participation_no_show/), [center squeeze](../center_squeeze/).

# file: README.md
