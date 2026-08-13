# Does it matter when voters don't use the whole 0–5 scale?

**Level: 301 · deep dive**

*A measured answer, from real ballots. In Equal Vote's public [US 2024 Presidential poll](https://bettervoting.com/pres24) — 2,772 ballots, 8 candidates — **14.1% of STAR ballots never used both ends of the scale**. This page reproduces that figure exactly, then tests whether it changed anything. It did not, and the reason is specific and checkable rather than reassuring.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pres24) · **[results ↗](https://bettervoting.com/pres24/results)** (election `pres24`) · **[the full LH count ↗](cases/cases_pages/pres24_star_range_usage.md)** · ballots as an engine case: [`pres24_star_range_usage.yaml`](cases/pres24_star_range_usage.yaml) · [`_tabulated` mirror](cases/cases_tabulated/pres24_star_range_usage_tabulated.txt) · rerun the measurements: [`analyze_range_usage.py`](analyze_range_usage.py)

---

## The number checks out — 14.1%, not a rounding of something else

Counting a **blank as a zero** (which is what the ballot instructions say and what the count does), a ballot "used the full range" if it gave someone a 5 *and* left someone at an effective 0:

| | ballots | share |
|---|---:|---:|
| Used the full range | 2,380 | **85.9%** |
| Did **not** | 392 | **14.1%** |

That reproduces the 86 / 14 split exactly. Worth noting *why* it reproduces: the naive version of this metric — looking for a literal `0` keystroke — gives **63.1%**, because 43.5% of voters expressed their zero by *leaving a candidate blank* instead of clicking 0. Those two ballots are identical to the count. Any future scan of scale usage has to treat blank and 0 as the same thing, or it will invent a 23-point problem that doesn't exist.

## What the 392 are actually missing: the top, not the bottom

This is the part that reframes the question.

| Of the 392 | ballots | share of the 392 |
|---|---:|---:|
| Missing a **5** — nobody earned full marks | 352 | **90%** |
| Missing a bottom — everyone scored ≥ 1 | 40 | 10% |

And the highest score they *did* give:

| Top score on the ballot | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| ballots | 3 | 13 | 11 | 75 | **250** | 40 |

The dominant behavior — 250 ballots, nearly two-thirds of the group — is *"my favorite gets a 4."* That is not a compressed or confused ballot. It is a voter grading on an absolute scale and declining to award full marks to anyone in the 2024 presidential field. The repo already has a name and a page for it: **[Compressed Middle](../../01_Learn/voting_styles/compressed_middle.md)**, one of the [thirteen legal voting styles](../../01_Learn/voting_styles/README.md), whose opening line is *"nobody here is a 5."* Only **3** ballots of the 2,772 scored nothing at all.

**They are also not the low-effort ballots.** Distinct score levels used per ballot:

| | 4+ levels used | mean levels |
|---|---:|---:|
| Not full range (392) | **67.6%** | 3.80 |
| Full range (2,380) | 60.9% | 3.90 |

The group flagged as a problem differentiates *more* candidates than the electorate at large. A bullet vote uses two levels and passes the full-range test; a 4-3-2-1 ballot uses four and fails it. **"Used both endpoints" is not a measure of expressiveness**, and it should not be reported as one.

## Did it change the outcome? No — and not by luck

Four ways of asking, including two that are deliberately unfair to the compressed ballots:

| Treatment of the 392 | 2nd finalist | Winner |
|---|---|---|
| As cast (baseline) | Cornell West | **Kamala Harris** |
| Stretched to a full 0–5 range | Cornell West | **Kamala Harris** |
| **Discarded entirely** | Cornell West | **Kamala Harris** |
| Every ballot normalized | Cornell West | **Kamala Harris** |

The reason is structural, not lucky: **the scoring-round leader is also the [Condorcet winner](../../../07_Concepts/topics/condorcet/README.md)** — Harris beats all seven rivals head-to-head, by margins from 1,604–577 to 1,895–316. So *whoever* takes the second finalist slot, the runoff returns the same winner. Rescaling ballots can only reshuffle who comes second; it cannot reach the result. A **bootstrap of 2,000 resamples** returns Harris **2,000 / 2,000** times. And one more layer of the same point: the poll ran the *same electorate* through four ballots — Choose-One, [RCV-IRV](../../../06_Other/RCV_IRV/README.md), Approval and STAR — and **all four elected Harris**. A result this robust is not one that a 14% change in scale usage could reach.

### Where the real fragility is — and it isn't scale usage

Gemini's caveat, quoted in the thread, was that compression rarely matters *"unless a race features an extremely narrow gap between the 2nd and 3rd place candidates."* **This poll is that race.** West 4,262 vs Stein 4,197 — a **65-point gap, 1.5%** of second place. The escape clause was satisfied and went unnoticed.

The conclusion survives anyway, for two reasons the caveat didn't reach:

1. **The second slot is indeterminate from plain sampling noise, not from compression.** In the bootstrap, West takes it 79% of the time and Stein 21%. That coin-flip exists whether or not anyone compressed anything.
2. **Compression was not the thumb on the scale.** Stretching those 392 ballots *widens* the 2nd–3rd gap from 65 to 78 — it makes second place *more* secure, not less. Compression here was roughly neutral across candidates, because the voters doing it were not concentrated in one camp.

So the honest verdict is stronger than "low to moderate concern": for this election the winner is provably invariant, and the one genuinely wobbly number is wobbly for a reason a full-scale prompt would not fix.

## The metric that *does* measure lost power: Equal Support

A ballot's influence in the [automatic runoff](../../01_Learn/the_count/README.md) is binary — you either prefer one finalist or you don't. Scale usage is irrelevant there; **[Equal Support](../../../07_Concepts/GLOSSARY.md)** is the number that counts.

| | expressed a runoff preference | Equal Support |
|---|---:|---:|
| Not full range (392) | **81.9%** | 71 |
| Full range (2,380) | 78.2% | 520 |

The flagged ballots carried **more** runoff weight than the average ballot. The 520 Equal Support ballots in the compliant group are mostly sincere — voters who rated both eventual finalists 0, having backed a candidate on the other side of the field. Nothing is wrong with those either, but it does mean the two metrics point in opposite directions: *if you want to report one number about wasted voting power, report Equal Support, not scale usage.*

## On the suggested "are you sure?" prompt

The data supports the education framing over the validation framing, with one caution worth stating plainly:

- **A prompt nudging voters toward 0 and 5 is a nudge toward strategic maximization** — awkward for a method whose central claim is that you never have to exaggerate. It also lands asymmetrically: it would alter the ballots of one identifiable 14% and nobody else's. Tolerable in a casual poll; in a certified public election, an administrator-side nudge that systematically moves one subgroup's ballots is the kind of thing that invites challenge.
- **The unambiguous case is different.** A voter who left candidates blank *and* has no top score may have abandoned the form partway. Prompting on an **incomplete** ballot is a genuine error check; prompting on a **complete but modest** one second-guesses a sincere opinion.
- **A "your ballot as counted" review screen** does the educational job without telling anyone what to think — it shows blanks resolving to 0, which is the misconception actually worth fixing (43.5% of these voters used blanks as zeros, and a scan that didn't know that mismeasured the poll by 23 points).

## The count

Verified three ways: this repo's engine, BetterVoting's own tabulation, and the independent script above. All agree on every score, every five-star count, and every pairwise total.

```text title="Abridged for the lesson — the full 4,649-line report is linked above"
Scoring Round
   Kamala Harris (D)         -- 8250 -- First place
   Cornell West (I)          -- 4272 -- Second place
   Jill Stein (G)            -- 4207
   Chase Oliver (L)          -- 3817
   Donald J. Trump (R)       -- 3790
   Robert F. Kennedy Jr. (I) -- 3454
   Claudia De la Cruz (S)    -- 3415
   Randall Terry (C)         -- 1748
 Kamala Harris (D) and Cornell West (I) advance.

Automatic Runoff Round
   Kamala Harris (D)         -- 1604 -- First place
   Cornell West (I)          --  577
   Equal Support             --  591
 Kamala Harris (D) wins.
   Voters with a preference: 2181 of 2772 (591 Equal Support).
   Kamala Harris (D) 1604 (74%) vs Cornell West (I) 577 (26%); majority = 1091.
```

**One reconciliation note, so the two engines can be compared line by line.** BetterVoting reports each candidate's score **10 points lower** than the engine above — 8,240 vs 8,250, and the same −10 on all eight. The cause is benign, already documented in this repo, and now confirmed at scale: **7 ballots score every candidate identically** (three all-0s, three all-3s, one all-1s), and BetterVoting treats a ballot with no preference at all as an **abstention**, excluding it from the score totals — the same divergence the [abstain, blank & zero handling](../abstain_bugs/README.md) set isolates on small constructed cases ([#884](https://github.com/Equal-Vote/bettervoting/issues/884)). This is that divergence appearing in 2,772 real ballots, where it moves every score by the same 10 points and decides nothing. Those 7 ballots contribute exactly 10 points to *every* candidate, so they cannot change any ranking, any pairwise comparison, or the winner. Excluding them, the two engines match to the point on all eight candidates and all eight five-star counts.

## Reproduce it

The 13 MB export is deliberately **not** committed — one command regenerates it, and the ballots live here in engine form at 50 KB.

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/fetch_bv_export.py pres24 -o /tmp/pres24.json
```

```bash
python3 01_STAR/04_Real_Elections/pres24_range_usage/analyze_range_usage.py /tmp/pres24.json
```

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/04_Real_Elections/pres24_range_usage/cases/pres24_star_range_usage.yaml
```

## See also

- [The STAR ballot & every legal way to fill it out](../../01_Learn/voting_styles/README.md) — the thirteen styles, including [Compressed Middle](../../01_Learn/voting_styles/compressed_middle.md), [Partial Ballot](../../01_Learn/voting_styles/partial_ballot.md) and [Protest Vote](../../01_Learn/voting_styles/protest_vote.md)
- [Real elections](../README.md) — the other real-ballot case sets
