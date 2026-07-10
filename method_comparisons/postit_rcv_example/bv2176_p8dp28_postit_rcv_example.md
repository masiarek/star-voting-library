# The Post-it RCV example (20 voters) — the runoff RCV-IRV never held

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28`, Test ID **BV2176**).

The 20-voter election from Equal Vote's video **["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg)** — the whiteboard demo that walks through an RCV-IRV count sticky note by sticky note, then asks the question the count itself never asks: *was the eliminated candidate actually stronger head-to-head?* Four candidates (Purple, Green, Blue, Pink), one electorate, three tabulations live on BetterVoting: RCV-IRV elects **Purple**, STAR (on the video's own 0–5 scores) elects **Blue**, and Ranked Robin exposes a Condorcet cycle whose 2–1 tie the two engines break differently — **Green** on BetterVoting, **Blue** in the LH engine. Same ballots, three defensible winners: the tabulation decides. <!-- terminology-ok: bare RCV is inside the quoted video title -->

## The ballots

The same 20 voters, ranked (the video's Post-its) and scored 0–5 (the video's STAR comparison):

| # voters | ranked ballot | scores (Purple, Green, Blue, Pink) |
|---:|:--|:--|
| 7 | Purple | 5, 0, 0, 0 |
| 6 | Green > Blue > Pink | 0, 5, 4, 3 |
| 2 | Blue > Pink | 0, 0, 5, 4 |
| 1 | Blue > Green > Pink | 0, 4, 5, 3 |
| 1 | Blue > Purple | 4, 0, 5, 0 |
| 1 | Pink > Green > Purple | 3, 4, 0, 5 |
| 1 | Pink > Purple | 4, 0, 0, 5 |
| 1 | Pink | 0, 0, 0, 5 |

First choices: Purple 7, Green 6, Blue 4, Pink 3. Score totals: Purple 46, Blue 44, Pink 44, Green 38.

## The video's count — and the video's question

**RCV-IRV** (the whiteboard walk-through): round 1 eliminates Pink (3 first choices; 1 ballot transfers to Green, 1 to Purple, 1 bullet-vote exhausts). Round 2 stands at Purple 8, Green 7, Blue 4 — Blue is eliminated (1 to Green, 1 to Purple, and both Blue>Pink ballots exhaust, Pink being already gone). Final: **Purple 9, Green 8**, with 3 of the 20 ballots exhausted — Purple wins with 9 of the 17 still-active ballots.

The video then flips the round-2 elimination: *what if Green (7 votes) had gone out instead of Blue (4)?* All six Green>Blue>Pink ballots land on Blue, and **Blue wins 10–9**. That hypothetical is not a fluke of transfer order — it is the actual head-to-head: on these 20 ballots **Blue beats Purple 10–9**. RCV-IRV eliminated Blue without ever holding that matchup.

**STAR** holds it automatically. Scoring round: Purple 46 advances; the **44–44 tie** between Blue and Pink for the second finalist slot breaks by the official protocol's next rung — head-to-head, where Blue is preferred over Pink 10–3. The automatic runoff is then exactly the matchup the video asked about: **Blue 10, Purple 9** (1 Equal Support) — Blue wins. It is also a **Runoff Reversal**: the score leader (Purple, 46) loses the majority check, STAR working as designed. BetterVoting concurs on every rung (`tieBreakType: head_to_head` on the scoring tie).

## One electorate, three counts

| Race (BV) | Method | BV winner | LH winner | How |
|---|---|:--:|:--:|:--|
| Post-its 20 voters — STAR | STAR | **Blue** | **Blue** | 46/38/44/44; second-finalist tie → head-to-head Blue 10–3 Pink; runoff Blue 10–9 (Runoff Reversal) |
| Post-its 20 voters — RCV-IRV | IRV | **Purple** | **Purple** | 7/6/4/3 → 8/7/4 → 9–8; 3 exhausted |
| Post-its 20 voters — Ranked Robin | RankedRobin (Copeland) | **Green** | **Blue** | 2-way Copeland tie at 2–1 — the two ladders part ways (below) |

## The Ranked Robin race — one tie, two ladders, both deterministic

There is **no Condorcet winner** here: the pairwise picture is a genuine cycle (Purple beats Green 9–8, Green beats Blue 7–4, Blue beats Purple 10–9 — and Pink beats Purple 12–8). Green and Blue each go **2–1** (Copeland 2), and that tie is exactly where [the two engines' tiebreak ladders diverge](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md):

- **BetterVoting** (`RankedRobin.ts`): exactly 2 tied → their own head-to-head. Green beats Blue **7–4** → **Green**, deterministically (BV-confirmed live).
- **LH** (`run_ranked_robin`): total margin. Blue +5 vs Green +4 → **Blue**, deterministically.

Both ladders are deterministic on this profile, so the race is freezable — making BV2176 the **first live BetterVoting election to exhibit the documented ladder divergence** (the previous worked example, the dead-heat case, is LH-only because BV's ladder falls through to random there). The independent `pref_voting` Copeland check reports the leader *set* {Blue, Green}: both engines tie-broke inside it, consistently with their published rules.

---

## LH engine reports (View 2)

### STAR — Blue (the runoff the video asked for)

```
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Purple        -- 46 -- First place
   Blue          -- 44 -- Tied for second place
   Pink          -- 44 -- Tied for second place
   Green         -- 38
 Purple advances, but there's a two-way tie for second.

Scoring Round: First tiebreaker
 The candidate preferred in the most head-to-head matchups advances.
   Blue          -- 10 -- Second place
   Pink          --  3
   Equal Support --  7
 Purple and Blue advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Blue          -- 10 -- First place
   Purple        --  9
   Equal Support --  1
 Blue wins.
   Voters with a preference: 19 of 20 (1 Equal Support).
   Blue 10 (53%) vs Purple 9 (47%); majority = 10.

[Runoff Reversal]
 - Score Round Winner(s) = (Purple)
 - Runoff Round Winner   = (Blue)

[Condorcet Winner]
  No Condorcet winner (majority cycle: Purple > Green > Pink > Purple)

[Divergence from STAR]
  STAR                   = Blue
  Choose-One (Plurality) = Purple   (differs from STAR)
  RCV-IRV                = Purple   (differs from STAR)
  Approval               = Pink   (differs from STAR)
```

### RCV-IRV — Purple (the video's whiteboard rounds)

```
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Purple             7  Hopeful
Green              6  Hopeful
Blue               4  Hopeful
Pink               3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Purple             8  Hopeful
Green              7  Hopeful
Blue               4  Rejected
Pink               0  Rejected
Blank Votes        1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Purple             9  Elected
Green              8  Rejected
Blue               0  Rejected
Pink               0  Rejected
Blank Votes        3  Rejected
```

### Ranked Robin — the cycle, the 2–1 tie, and LH's margin rung

```
Round-Robin — every pair, head-to-head (For – Against):
   Purple  beats Green     9 –  8
   Blue    beats Purple   10 –  9
   Pink    beats Purple   12 –  8
   Green   beats Blue      7 –  4
   Green   beats Pink      7 –  5
   Blue    beats Pink     10 –  3

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Blue       2–1–0         2      +5  Purple, Pink
    2  Green      2–1–0         2      +4  Blue, Pink
    3  Purple     1–2–0         1      -4  Green
    4  Pink       1–2–0         1      -5  Purple

Winner — Ranked Robin (RCV-RR): Blue
   *** 2 candidates tie for the most wins (Green, Blue) — a Condorcet cycle
   (no candidate beats all others). Resolved by total margin, then lot order.
```

BetterVoting's live result for the same race: **Green** (Copeland 2, elected via the head-to-head rung of its ladder).

---

## Files

| Race | YAML | `_tabulated` mirror |
|---|---|---|
| STAR (lead) | [bv2176_p8dp28_star.yaml](bv2176_p8dp28_star.yaml) | [txt](postit_rcv_example_tabulated/bv2176_p8dp28_star_tabulated.txt) |
| RCV-IRV | [bv2176_p8dp28_irv.yaml](bv2176_p8dp28_irv.yaml) | [txt](postit_rcv_example_tabulated/bv2176_p8dp28_irv_tabulated.txt) |
| Ranked Robin | [bv2176_p8dp28_ranked_robin.yaml](bv2176_p8dp28_ranked_robin.yaml) | [txt](postit_rcv_example_tabulated/bv2176_p8dp28_ranked_robin_tabulated.txt) |

Frozen BetterVoting export (Election + Ballots + Results): `bv2176_p8dp28_bv_export.json` — *pending; export from the BV UI and drop it here.*

Related: [the video](https://youtu.be/Vte4nly_Neg) · [LH vs BV on Ranked Robin ties](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) · [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · up: [method_comparisons](../)

*BetterVoting result screenshots (View 1) can be dropped into `img/` as `img/p8dp28_<what>.png` and linked here.*

# file: bv2176_p8dp28_postit_rcv_example.md
