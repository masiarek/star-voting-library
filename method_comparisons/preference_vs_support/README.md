# Preference vs. Support, as a live election — the rank can't see what the score can

*Two elections with **byte-identical rankings**. The only thing that changes is how hard the two wings score the centrist **Blair** — a grudging **1** in one, a genuine **4** in the other. Because the orders never move, **RCV-IRV and Ranked Robin return the exact same winners in both** — they read only order, and the order didn't change. **STAR is the only method that moves**, because STAR reads the one thing that did change: support. This is the [Preference vs. Support](../../00_start_here/scores_and_ranks/preference_vs_support.md) lesson made concrete.*

**▶ Live on BetterVoting:**
- **Tolerated** (Blair = 1): [vote](https://bettervoting.com/ywx39y) · **[results ↗](https://bettervoting.com/ywx39y/results)** (election `ywx39y`, BV2225)
- **Supported** (Blair = 4): [vote](https://bettervoting.com/82gg36) · **[results ↗](https://bettervoting.com/82gg36/results)** (election `82gg36`, BV2226)

→ Companion pages: [Preference vs. Support](../../00_start_here/scores_and_ranks/preference_vs_support.md) · [Scores vs. ranks](../../00_start_here/scores_and_ranks/scores_vs_ranks.md) · [Center squeeze](../center_squeeze/) (one electorate, method varies) · [What makes a good winner?](../../00_start_here/topics/what_makes_a_good_winner.md)

---

## The ballots — identical rankings, one number changed

Three candidates on a spectrum: **Alex** (a pole), **Blair** (the center), **Cole** (the other pole). 36 voters, three blocs. Read the *order* off either score column and the two elections are the same ballot:

| Voters | Ranking (identical in both) | TOLERATED scores | SUPPORTED scores |
|---|---|:--:|:--:|
| 15 | Alex > Blair > Cole | `5, 1, 0` | `5, 4, 0` |
| 6 | Blair > Alex > Cole | `1, 5, 0` | `1, 5, 0` |
| 15 | Cole > Blair > Alex | `0, 1, 5` | `0, 4, 5` |

Only the wings' score for **Blair** changed: **1 → 4**. Nobody's *preference order* moved a millimetre.

## The result — one table, the whole lesson

| Method | Reads… | TOLERATED (Blair = 1) | SUPPORTED (Blair = 4) | Moved? |
|---|---|:--:|:--:|:--:|
| **RCV-IRV** | order only | **Alex** | **Alex** | ❌ can't — center-squeezes Blair both times |
| **Ranked Robin** | order only | **Blair** | **Blair** | ❌ can't — Blair is the Condorcet winner both times |
| **STAR** | order **+ support** | **Alex** | **Blair** | ✅ **the only method that responds** |

IRV and Ranked Robin **cannot tell the two electorates apart** — the rankings are identical, so their tallies are byte-for-byte identical. Only STAR registers that in the second election the wings *genuinely support* Blair (4s) rather than merely tolerate him (1s), and shifts the winner accordingly.

### Read it even-handedly — no method is the villain

- **RCV-IRV** eliminates Blair for having the fewest first-choices in *both* elections — the textbook [center squeeze](../center_squeeze/). It never sees Blair's second-choice strength at all.
- **Ranked Robin** looks *good* here: it finds the consensus Blair from the order alone (he beats both poles 21–15 head-to-head). But it crowns a **barely-tolerated** Blair exactly as readily as a **beloved** one — it has no way to know the difference. That's the honest limit of an order-only method, not a knock on Ranked Robin's design.
- **STAR** is the one that says: *when Blair earns only 1s, he hasn't the support to win — elect the candidate with a real base (Alex); when Blair earns real 4s, he's earned the seat.* Support, tracked.

The point isn't "STAR wins the argument." It's that **support is real information, and only a score ballot carries it** — the same claim the [Preference vs. Support](../../00_start_here/scores_and_ranks/preference_vs_support.md) page makes with `1,0,1,0` vs `5,4,5,4`, now as 36 real ballots you can re-run.

## The engine says so — TOLERATED (Blair = 1) → STAR elects Alex

```
Scoring Round
   Alex          -- 81 -- First place
   Cole          -- 75 -- Second place
   Blair         -- 60            ← thin support: Blair misses the runoff
 Alex and Cole advance.

Automatic Runoff Round
   Alex          -- 21 -- First place
   Cole          -- 15
 Alex wins.

[Divergence from STAR]
  STAR               = Alex
  RCV-RR (Condorcet) = Blair   (differs from STAR)
```
(RCV-IRV also elects **Alex** here — it squeezes Blair out. Full detail: [`bv2225_ywx39y_center_tolerated` mirror](cases/cases_tabulated/bv2225_ywx39y_center_tolerated_tabulated.txt) · [page](cases/cases_pages/bv2225_ywx39y_center_tolerated.md).)

## The engine says so — SUPPORTED (Blair = 4) → STAR elects Blair

```
Scoring Round
   Blair         -- 150 -- First place   ← real support: Blair now leads
   Alex          --  81 -- Second place
   Cole          --  75
 Blair and Alex advance.

Automatic Runoff Round
   Blair         -- 21 -- First place
   Alex          -- 15
 Blair wins.

[Divergence from STAR]
  STAR                   = Blair
  RCV-IRV                = Alex   (differs from STAR)
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
```
(Same rankings as the tolerated election, so **RCV-IRV → Alex** and **Ranked Robin → Blair** are both *unchanged*; only STAR moved. Full detail: [`bv2226_82gg36_center_supported` mirror](cases/cases_tabulated/bv2226_82gg36_center_supported_tabulated.txt) · [page](cases/cases_pages/bv2226_82gg36_center_supported.md).)

## Reproduce it

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
  method_comparisons/preference_vs_support/cases/bv2225_ywx39y_center_tolerated.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
  method_comparisons/preference_vs_support/cases/bv2226_82gg36_center_supported.yaml
```

Each STAR file's `[Divergence from STAR]` block runs RCV-IRV and Ranked Robin on the same ballots — that's where the "same ranks, IRV & RR don't move, STAR does" table comes from. Both elections are also live on BetterVoting (results links above), and **BetterVoting's own tabulations confirm every cell of the table** — STAR → Alex/Blair, IRV → Alex/Alex, Ranked Robin → Blair/Blair — verified from the frozen full exports ([`…tolerated_bv_export.json`](cases/bv2225_ywx39y_center_tolerated_bv_export.json) · [`…supported_bv_export.json`](cases/bv2226_82gg36_center_supported_bv_export.json), each Election + Ballots + Results). BV and the LH engine agree exactly.
