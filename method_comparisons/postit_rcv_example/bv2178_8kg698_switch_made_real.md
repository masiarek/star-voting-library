# The Post-it switch, made real — two ballots flip and RCV-IRV elects Blue

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8kg698) · **[results ↗](https://bettervoting.com/8kg698/results)** (election `8kg698`, Test ID **BV2178**).

Equal Vote's video ["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg) ends its count with a hypothetical: *what if round 2 had eliminated Green (7 votes) instead of Blue (4)?* Its answer — all six Green>Blue>Pink ballots land on Blue, and **Blue wins 10–9**. But RCV-IRV would never *do* that: it always eliminates the current last place, and Green held 7 votes to Blue's 4. The hypothetical can't be demonstrated on any real tabulator as-is. <!-- terminology-ok: bare RCV is inside the quoted video title -->

This election demonstrates it anyway — with the smallest honest change. **Exactly two of the six Green>Blue>Pink voters flip their top two choices** (to Blue>Green>Pink; scores 0,4,5,3). Nothing else moves. That's enough to reverse Green's and Blue's round-2 standing, and RCV-IRV then walks straight into the video's scenario for real:

## The count, before and after

| | BV2176/77 (the video) | BV2178 (two ballots flip) |
|---|---|---|
| Round 1 | Purple 7, Green 6, Blue 4, Pink 3 → Pink out | Purple 7, **Blue 6, Green 4**, Pink 3 → Pink out |
| Round 2 | Purple 8, Green 7, Blue 4 → **Blue out** | Purple 8, Blue 6, Green 5 → **Green out** |
| Final | **Purple 9**, Green 8 (3 exhausted) | **Blue 10, Purple 9** (1 exhausted) |

The final tally — Blue 10, Purple 9 — is digit-for-digit the video's hypothetical. Two voters moved; the RCV-IRV winner flipped from Purple to Blue. The lesson cuts both ways:

- **For the video's point:** RCV-IRV only discovers Blue's head-to-head strength when Blue's supporters happen to rank Blue *first*. Blue beat Purple 10–9 in *both* electorates — but IRV elects Blue in only one of them. The information was always on the ballots; the elimination order determines whether IRV ever reads it.
- **For balance:** the flip didn't just game IRV's mechanics — it genuinely changed the electorate. In the original profile Blue was in a Condorcet **cycle** (Green beat Blue 7–4); after the flip **Blue beats everyone** — Purple 10–9, Green 6–5, Pink 10–3 — an outright **Condorcet winner**. The two electorates have different consensus answers, and IRV happens to match the consensus only in the second.

## Every method, before and after

| Method | BV2176/77 (the video) | BV2178 (switch) |
|---|:--:|:--:|
| STAR | **Blue** (scores 46/38/44/44; runoff 10–9 — a Runoff Reversal) | **Blue** (scores Blue 46, Purple 46, Pink 44, Green 36 — the co-leaders *are* the finalists; same runoff 10–9) |
| Ranked Robin | **Green** on BV / **Blue** in LH (2–1 tie, [two ladders](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md)) | **Blue** everywhere — Condorcet winner 3–0, no tie, no ladder |
| RCV-IRV | **Purple** (9–8) | **Blue** (10–9) — the video's hypothetical, real |
| Choose-One | **Purple** (7) | **Purple** (7 vs 6) — still reading only first choices |

STAR is the only method above whose winner survives the switch — it was already electing the head-to-head favorite in the runoff. Ranked Robin snaps from its knife-edge tie (where two engines defensibly disagree) to unanimity. IRV swings entirely. Choose-One never notices anything happened.

## LH engine report (View 2) — the switch RCV-IRV count

```
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Purple             7  Hopeful
Blue               6  Hopeful
Green              4  Hopeful
Pink               3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Purple             8  Hopeful
Blue               6  Hopeful
Green              5  Rejected
Pink               0  Rejected
Blank Votes        1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Blue              10  Elected
Purple             9  Rejected
Green              0  Rejected
Pink               0  Rejected
Blank Votes        1  Rejected
```

And the switch pairwise picture — Blue, clean Condorcet winner:

```
Round-Robin — every pair, head-to-head (For – Against):
   Purple  beats Green     9 –  8
   Blue    beats Purple   10 –  9
   Pink    beats Purple   12 –  8
   Blue    beats Green     6 –  5
   Green   beats Pink      7 –  5
   Blue    beats Pink     10 –  3

    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Blue       3–0–0         3      +9  Green, Purple, Pink

Winner — Ranked Robin (RCV-RR): Blue
   beats every opponent head-to-head — the Condorcet winner.
```

## Files

| Race | YAML | `_tabulated` mirror |
|---|---|---|
| STAR (lead) | [bv2178_8kg698_star.yaml](bv2178_8kg698_star.yaml) | [txt](postit_rcv_example_tabulated/bv2178_8kg698_star_tabulated.txt) |
| RCV-IRV | [bv2178_8kg698_irv.yaml](bv2178_8kg698_irv.yaml) | [txt](postit_rcv_example_tabulated/bv2178_8kg698_irv_tabulated.txt) |
| Ranked Robin | [bv2178_8kg698_ranked_robin.yaml](bv2178_8kg698_ranked_robin.yaml) | [txt](postit_rcv_example_tabulated/bv2178_8kg698_ranked_robin_tabulated.txt) |
| Choose-One | (documented in the STAR mirror's divergence block: Purple) | — |

Frozen BetterVoting export (Election + Ballots + Results): `bv2178_8kg698_bv_export.json` — *pending; export from the BV UI and drop it here.*

Related: [the BV2176 case page](bv2176_p8dp28_postit_rcv_example.md) · [seven ways (BV2177)](bv2177_v8r66y_seven_methods.md) · [is the video fair and balanced?](postit_video_fair_and_balanced.md) · up: [method_comparisons](../)

# file: bv2178_8kg698_switch_made_real.md
