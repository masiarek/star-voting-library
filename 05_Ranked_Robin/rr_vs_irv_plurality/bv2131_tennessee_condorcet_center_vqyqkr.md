# BV2131 — Tennessee capital: Ranked Robin elects the Condorcet center (Nashville)

*The textbook Tennessee example, and the first BV-backed **Ranked Robin** case. Four cities; each voter ranks by geographic distance; blocs weighted by population. On **one** ranked ballot set the three methods split three ways — plurality → **Memphis**, RCV-IRV → **Knoxville**, Ranked Robin / Condorcet → **Nashville** — so it's the cleanest single illustration of why "most first-choices" and "last one standing" can both miss the candidate a majority actually prefers.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vqyqkr) · **[results ↗](https://bettervoting.com/vqyqkr/results)** (election `vqyqkr`).

Reference files: [`bv2131_tennessee_condorcet_center_vqyqkr.yaml`](bv2131_tennessee_condorcet_center_vqyqkr.yaml) (`expected_winners: [Nashville]`) · frozen export [`bv2131_tennessee_condorcet_center_vqyqkr_bv_export.json`](bv2131_tennessee_condorcet_center_vqyqkr_bv_export.json). Test ID **BV2131** (= `BV` + the BetterVoting election id `vqyqkr`).

## The ballots

Each bloc votes by geographic distance; the weight is that city's share of the electorate (100 voters).

```text
42 × Memphis > Nashville > Chattanooga > Knoxville
26 × Nashville > Chattanooga > Knoxville > Memphis
15 × Chattanooga > Knoxville > Nashville > Memphis
17 × Knoxville > Chattanooga > Nashville > Memphis
```

## Three methods, three winners — same ballots

| Method | Reads | Winner | Why |
|--------|-------|--------|-----|
| **Plurality** | first choices only | **Memphis** | biggest first-choice bloc (42), even though 58% rank it *last* |
| **RCV-IRV** | ranked, elimination | **Knoxville** | Chattanooga (15) is eliminated first, its votes lift Knoxville past Nashville; Nashville is squeezed out in round 2 |
| **Ranked Robin** | ranked, round-robin | **Nashville** | beats **every** rival head-to-head — the Condorcet winner |

The center-squeeze is the story: Nashville is the second choice of almost everyone, so it wins every pairwise matchup, but it holds only 26 first-choices — so IRV discards it before the final round.

## View 1 — Ranked Robin (LH native `run_ranked_robin`)

Full report in the [`_tabulated` mirror](rr_vs_irv_plurality_tabulated/bv2131_tennessee_condorcet_center_vqyqkr_tabulated.txt):

```text
Round-Robin — every pair, head-to-head (For – Against):
   Nashville    beats Memphis       58 – 42
   Chattanooga  beats Memphis       58 – 42
   Knoxville    beats Memphis       58 – 42
   Nashville    beats Chattanooga   68 – 32
   Nashville    beats Knoxville     68 – 32
   Chattanooga  beats Knoxville     83 – 17

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate    W–L–T  Copeland  Margin  Beats
    1  Nashville    3–0–0         3     +88  Chattanooga, Knoxville, Memphis
    2  Chattanooga  2–1–0         2     +46  Knoxville, Memphis
    3  Knoxville    1–2–0         1     -86  Memphis
    4  Memphis      0–3–0         0     -48  —

Winner — Ranked Robin (RCV-RR): Nashville
   beats every opponent head-to-head — the Condorcet winner.
```

Nashville is 3–0–0 (Copeland 3): no tiebreak is invoked, so the LH margin→lot ladder never comes into play here — this is the *agreement* case, not the divergence one. (For where the LH and BetterVoting tiebreak rules diverge, see [the tiebreak note](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) and its LH-only [dead-heat case](../rr_tiebreaks/).)

## View 2 — BetterVoting (`RankedRobin.ts`, frozen results)

Reproduced live at [**bettervoting.com/vqyqkr/results**](https://bettervoting.com/vqyqkr/results). From the frozen `_bv_export.json` Results, `tieBreakType: none`:

| Candidate | `votesPreferredOver` (BV) | Copeland |
|-----------|---------------------------|:--------:|
| **Nashville** | Chattanooga 68 · Memphis 58 · Knoxville 68 | **3** |
| Chattanooga | Knoxville 83 · Memphis 58 | 2 |
| Knoxville | Memphis 58 | 1 |
| Memphis | — | 0 |

Every pairwise count matches the LH `For` column exactly (58/42, 68/32, 83/17). BV elects **Nashville**.

## View 3 — pref_voting (independent Copeland cross-check)

A third, independent tally guards against the LH native code misbehaving: `pref_voting` builds its own `Profile` from the raw ballots and runs its own Copeland (it does **not** reuse LH's matrix). Run it locally (declared in `pyproject.toml`; `uv sync` first):

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py \
  05_Ranked_Robin/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.yaml
```

> _pref_voting cross-check output — paste here after running `uv sync` locally. Expected: `pref_voting Copeland leader(s): Nashville` · `AGREE ✓ (unique Copeland winner)`._

## Agreement

| Tally | Winner | Detail |
|-------|--------|--------|
| LH native `run_ranked_robin` | **Nashville** | Copeland 3, no tiebreak |
| BetterVoting `RankedRobin.ts` | **Nashville** | `tieBreakType: none` |
| pref_voting Copeland | **Nashville** *(pending local run)* | independent `Profile` |

All three agree on the Condorcet winner — while plurality (Memphis) and RCV-IRV (Knoxville) each pick someone else.

## See also

- Folder overview: [rr_vs_irv_plurality — README](README.md)
- The RR-vs-Condorcet distinction (cycles): [condorcet_vs_ranked_robin](../condorcet_vs_ranked_robin/) · lesson [ranked_robin_vs_condorcet.md](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md)
- The tiebreak divergence (LH margin→lot vs BV head-to-head→random): [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md)
- [Condorcet efficiency — topic hub](../../00_start_here/topics/condorcet/README.md) · [Glossary](../../00_start_here/GLOSSARY.md)
