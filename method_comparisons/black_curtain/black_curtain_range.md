# The Black Curtain, read as Range / Score voting

*The four [Black Curtain](README.md) elections, tabulated by the **range voting engine** (pref_voting `score_voting`, cross-checked against a hand sum). Same ballots as the STAR pages — but counted as pure **Range**: highest total score wins, no runoff. Watch Range and STAR **part ways** exactly where the runoff matters.*

→ Method overview: [Range / Score voting](../../00_start_here/Range_Voting/range_voting.md) · Engine: [the Range engine](../../06_Other/Range/Range_tabulation_engine/) · The set's STAR write-up: [The Black Curtain — one electorate, four "identical" landslides](README.md).

---

## The lesson

Range and STAR read the **same score ballots**. Range stops at the score total; STAR adds an **automatic runoff** between the top two. So they agree when the score leader would also win the runoff — and **diverge when the runoff overturns the score leader**. Black Curtain makes both cases visible on identical voters:

| Election | STAR | **Range / Score** | Same? |
|---|---|---|:--:|
| 1 — hidden consensus | Cal | **Bob** | ✗ Range picks the broad consensus (Bob) STAR's runoff rejects |
| 2 — near-clones | Cal | **Cal** | ✓ |
| 3 — polarized on Cal | Cal | **Ann** | ✗ Range picks the everyone-likes-her Ann; STAR's majority bloc keeps Cal |
| 4 — four candidates | Cal | **Cal** | ✓ (Bob is a close 2nd, 14 vs 15 — see the [scale-granularity case](../../00_start_here/scores_and_ranks/scale_granularity_flips_the_winner.md)) |

The takeaway: **Range answers "who has the broadest summed support?"** and STAR answers **"of the two strongest, whom does the majority prefer head-to-head?"** Elections 1 and 3 are precisely the "enthusiasts vs. consensus" split — Range rewards the mildly-liked-by-everyone candidate, which is either its virtue or its vulnerability depending on your values (see the [pros and cons](../../00_start_here/Range_Voting/range_voting.md#pros-and-cons)).

---

## The elections (ballots + Range result)

Candidate cast: Ann, Bob, Cal (+ Dee). Scores are the 0–5 mapping of the video's 0–9 ballots (see the STAR README). Each block below links its source `.yaml` and its full `_RANGE_tabulated.txt` mirror.

### 1 — hidden consensus → **Bob**

Every voter scored Bob a near-top 4, but Bob is nobody's first choice. Range sees the consensus; STAR's runoff (Cal vs Bob, 3–2) does not.

```
Ann,Bob,Cal
0,4,5   ×3
5,4,0   ×2

Total score:  Bob 20 ← winner · Cal 15 · Ann 10   (pref_voting ✓ Bob)
```

[`Black_Curtain_01_c3_b5_hidden-consensus.yaml`](Black_Curtain_01_c3_b5_hidden-consensus.yaml) · [full range report](black_curtain_tabulated/Black_Curtain_01_c3_b5_hidden-consensus_RANGE_tabulated.txt) · [STAR page](black_curtain_pages/Black_Curtain_01_c3_b5_hidden-consensus.md)

### 2 — near-clones → **Cal**

Both blocs love Ann and Cal; Bob is universally hated. Range and STAR agree on Cal (Cal 23, Ann 22 — a one-point margin).

```
Ann,Bob,Cal
4,0,5   ×3
5,0,4   ×2

Total score:  Cal 23 ← winner · Ann 22 · Bob 0   (pref_voting ✓ Cal)
```

[`Black_Curtain_02_c3_b5_near-clones.yaml`](Black_Curtain_02_c3_b5_near-clones.yaml) · [full range report](black_curtain_tabulated/Black_Curtain_02_c3_b5_near-clones_RANGE_tabulated.txt) · [STAR page](black_curtain_pages/Black_Curtain_02_c3_b5_near-clones.md)

### 3 — polarized on Cal → **Ann**

Ann is scored high by *all five* voters; Cal is loved by three and zeroed by two. Range elects the broadly-liked Ann (22); STAR's runoff keeps the 3-voter majority's Cal.

```
Ann,Bob,Cal
4,0,5   ×3
5,1,0   ×2

Total score:  Ann 22 ← winner · Cal 15 · Bob 2   (pref_voting ✓ Ann)
```

[`Black_Curtain_03_c3_b5_polarized-on-cal.yaml`](Black_Curtain_03_c3_b5_polarized-on-cal.yaml) · [full range report](black_curtain_tabulated/Black_Curtain_03_c3_b5_polarized-on-cal_RANGE_tabulated.txt) · [STAR page](black_curtain_pages/Black_Curtain_03_c3_b5_polarized-on-cal.md)

### 4 — four candidates → **Cal**

Range and STAR agree on Cal — but only by **one point** (Cal 15, Bob 14). At the video's finer 0–9 scale, Score elects Bob; the 0–5 rescale flips it. That fragility is its own lesson: [scale granularity can flip the winner](../../00_start_here/scores_and_ranks/scale_granularity_flips_the_winner.md).

```
Ann,Bob,Cal,Dee
0,2,5,3   ×3
5,4,0,1   ×2

Total score:  Cal 15 ← winner · Bob 14 · Dee 11 · Ann 10   (pref_voting ✓ Cal)
```

[`Black_Curtain_04_c4_b5_four-candidates.yaml`](Black_Curtain_04_c4_b5_four-candidates.yaml) · [full range report](black_curtain_tabulated/Black_Curtain_04_c4_b5_four-candidates_RANGE_tabulated.txt) · [STAR page](black_curtain_pages/Black_Curtain_04_c4_b5_four-candidates.md)

---

*Tabulated by [`06_Other/Range/Range_tabulation_engine/range_tabulation.py`](../../06_Other/Range/Range_tabulation_engine/range_tabulation.py) (pref_voting `score_voting` + hand-sum cross-check). The full per-election `_RANGE_tabulated.txt` mirrors live in [`black_curtain_tabulated/`](black_curtain_tabulated/).*

# file: black_curtain_range.md
