# Manipulability — the textbook example is an attack on *our* method

*Seven voters, five cities, and a definition. Zwicker's Definition 2.3 calls a rule **single voter manipulable** if some voter can get a better result by lying. The profile he uses to illustrate it, `P₃`, shows a voter overturning the **Copeland** winner by submitting their ballot completely backwards. Here is the part that matters for this library: **Ranked Robin is Copeland.** The showcase manipulation in the textbook is a manipulation of one of the two methods we advocate — so this page leads with our own failure, then shows STAR's, then everyone else's.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4w96tr) · **[results ↗](https://bettervoting.com/4w96tr/results)** (election `4w96tr`, Test ID **BV2253** — the **sincere** baseline only, three races: Choose-One, STAR, Ranked Robin). The manipulated ballots below are counterfactual and stay LH-only; casting deliberate lies as a real public election would misrepresent what this profile is.

→ **Level: 301 · deep dive** The theorem behind it: [Gibbard–Satterthwaite](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) · the taxonomy: [strategic voting](../../07_Concepts/topics/strategic_voting.md) · [strategic pathologies scorecard](../../07_Concepts/topics/strategic_pathologies.md) · same chapter, different profile: [margins matter](../copeland_vs_borda_margins/README.md) · [the social welfare function](../../07_Concepts/topics/social_welfare_function.md) · related failures: [monotonicity](../monotonicity/README.md) · [reversal symmetry](../reversal_symmetry/README.md)

---

## The election

A committee of seven picks a meeting city.

| Voters | Ranking |
|---:|---|
| 2 | Edinburgh > Cork > Athens > Dublin > Bergen |
| 3 | Dublin > Edinburgh > Bergen > Cork > Athens |
| 2 | Athens > Bergen > Cork > Dublin > Edinburgh |

Sincerely, here is where everyone lands:

| Method | Sincere winner |
|---|---|
| Choose-One (Plurality) | **Dublin** (3 first choices) |
| [Borda](../../06_Other/other_ranked_methods/borda.md) | **Edinburgh** (17; Dublin 16, Cork 13, Athens 12, Bergen 12) |
| Copeland / [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) | **Edinburgh** (3–1) |
| [STAR](../../01_STAR/01_Learn/README.md) (ranks → 5/4/3/2/0) | **Dublin** (23; runoff 5–2 over Edinburgh) |
| [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) | **indeterminate** — see below |

There is **no Condorcet winner**: Edinburgh beats Cork, Athens and Bergen but loses to Dublin 5–2. Edinburgh's symmetric Copeland score is **+2**, Bergen's is **−2**, and the other three are **0** — exactly the numbers the chapter prints.

**RCV-IRV has no sincere answer here, and that is not a dodge.** First choices are Dublin 3, Athens 2, Edinburgh 2 — a genuine two-way tie for elimination. Which of Athens or Edinburgh is dropped decides the election, and nothing in the ballots decides it. We report IRV as indeterminate rather than quoting whichever winner a particular tiebreak produced.

**The baseline is live and independently confirmed.** All three sincere races ran on BetterVoting ([BV2253 `4w96tr`](https://bettervoting.com/4w96tr/results)) and agree with the LH engine exactly:

| Race | BetterVoting | LH engine | |
|---|---|---|---|
| Choose-One (Plurality) | Dublin | Dublin | ✓ |
| STAR | Dublin | Dublin | ✓ |
| Ranked Robin | Edinburgh | Edinburgh | ✓ |

Every race carries `tieBreakType: none` — nothing here was decided by chance, so unlike some Ranked Robin cases in this repo the whole result is freezable. Frozen export: [`p3_sincere_ranked_robin_bv_export.json`](cases/p3_sincere_ranked_robin_bv_export.json).

## What Zwicker's example actually does

The two Athens-first voters are about to watch their **last** choice, Edinburgh, win. Call one of them Ali. If Ali submits their ballot **completely reversed** — `Edinburgh > Dublin > Cork > Bergen > Athens` — one ballot flips two knife-edge 4–3 contests, and Dublin goes from 2–2 to **4–0**:

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Dublin     4–0–0         4      +8  Edinburgh, Bergen, Cork, Athens
    2  Edinburgh  3–1–0         3     +14  Bergen, Cork, Athens
    3  Bergen     2–2–0         2      -8  Cork, Athens
    4  Cork       1–3–0         1      -2  Athens
    5  Athens     0–4–0         0     -12  —

Winner — Ranked Robin (RCV-RR): Dublin
   beats every opponent head-to-head — the Condorcet winner.
```

Dublin's symmetric Copeland score is **+4, the maximum possible** for five candidates. Ali has replaced their last choice with their fourth — a strict gain — by submitting a ballot that misrepresents *every* pairwise preference they hold. Full report → [`p3_manip_reversal_rr.md`](cases/cases_pages/p3_manip_reversal_rr.md), sincere baseline → [`p3_sincere_ranked_robin.md`](cases/cases_pages/p3_sincere_ranked_robin.md).

**Ranked Robin is Copeland plus a tiebreak.** So this is not a lesson about some rule we don't use. It is our method being manipulated, in a textbook, as the canonical illustration of the concept.

## The version that should worry us more

A complete reversal is a curiosity — no real voter submits their preferences backwards. But the same voter gets the same result with the mildest strategy there is. Ali submits:

```
Dublin > Athens > Bergen > Cork > Edinburgh
```

Three adjacent swaps. **Nothing is buried** — Edinburgh, the sincere last choice, is still last. Only the compromise candidate is lifted. Dublin goes 4–0 and wins outright ([full report →](cases/cases_pages/p3_manip_compromise_rr.md)).

Exhaustively, **52 of the 119 other rankings** Ali could submit strictly improve their outcome — 44 decided outright or by margin, 8 more only after the lot. Nearly half the ballot space is a successful lie.

This is **compromising**, not burial. Ranked Robin's documented resistance to burial is untouched and stays true — which makes this *worse* news rather than better, because compromising is the strategy ordinary voters actually reach for.

## STAR is manipulable here too, and more cheaply

The honest counterweight. Sincerely, STAR elects Dublin (scoring round Dublin 23, Edinburgh 22, Cork 20, Bergen 17, Athens 16; runoff Dublin 5–2). Now the two **Edinburgh-first** voters score their 4th choice, Dublin, a **0 instead of a 2** — one number each, on one candidate:

```
Scoring Round
   Edinburgh     -- 22 -- First place
   Cork          -- 20
   Dublin        -- 19        ← was 23; knocked out of the finalists entirely
Automatic Runoff Round
   Edinburgh     -- 5 -- First place
```

Dublin no longer makes the runoff, and **Edinburgh — the manipulators' outright favourite — wins**. No favourite betrayal was needed; they kept their own first choice at 5 throughout. This one is **burial**, the strategy STAR is most exposed to. Full report → [`p3_manip_star.md`](cases/cases_pages/p3_manip_star.md).

Note the two failures are mirror images, which is the fairest way to read this page: Ranked Robin was manipulated by **compromising**, STAR by **burial**. Each method fell to the strategy it is known to be exposed to, on the same seven ballots.

## Where every method stands, including ours

Can a **single voter**, acting alone, change the winner to someone they sincerely prefer?

| Method | Manipulable here by one voter? | How |
|---|---|---|
| Choose-One (Plurality) | **No** | a voter can't lower the leader's score without top-ranking them; at best she lifts her own favourite to a *tie*. Verified exhaustively over all 120 ballots for each of the 7 voters |
| [Borda](../../06_Other/other_ranked_methods/borda.md) | **Yes** | but **not** by reversal — Ali lifting Dublin to the top (`Dublin > Athens > Bergen > Cork > Edinburgh`) makes Dublin the unique Borda winner, 19 to Edinburgh's 17 |
| Copeland / [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) | **Yes** | reversal *or* a three-swap compromise; 52 of 119 ballots work |
| [STAR](../../01_STAR/01_Learn/README.md) | **Yes** | two voters burying one candidate by two points; single-voter routes exist but cost a favourite betrayal at this spacing |
| [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) | *not assessable here* | the sincere baseline is already a coin flip, so "did the manipulation change the winner" has no well-defined answer. This is an artifact of the profile, **not** evidence that IRV resists strategy |

**Plurality is the only clean row, and it is worth being precise about why.** It is strategyproof *here* only in the narrow single-voter sense — and the chapter immediately breaks even that: if the **two** Edinburgh-first voters both switch to Athens-first, Athens takes it 4–3, and both of them prefer Athens to Dublin. A rule that resists one liar but folds to two is not a rule anyone should adopt for that reason. (Plurality has its own well-documented problems — see [vote splitting](../split_voting/README.md).)

## Borda cannot be manipulated by reversal — and why

The chapter's footnote makes a general claim: Copeland can be manipulated by complete reversal, **Borda never can**. Verified on this profile — reversing Ali's ballot moves Borda's totals to Edinburgh 21, Dublin 18, Cork 13, Bergen 10, Athens 8, and **Edinburgh still wins**, so the reversal gains Ali nothing.

The reason is structural rather than lucky. Under Borda a ballot contributes points that are symmetric about the middle rank, so reversing it *negates* that voter's entire contribution to every candidate at once. A voter cannot use reversal to help one candidate without helping their rivals in exact proportion. Copeland has no such symmetry: it reads only the direction of each pairwise arrow, so a reversed ballot can flip a knife-edge 4–3 contest and leave everything else untouched — which is precisely what happens above.

This is the useful takeaway about *how* the two rules differ, and it generalises the point from [margins matter](../copeland_vs_borda_margins/README.md): Copeland's blindness to margins is exactly what makes single knife-edge contests worth attacking.

## The honest frame

**Every method on this page is manipulable, including both of ours.** [Gibbard–Satterthwaite](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) settles it for ranked rules and Gibbard's 1978 result covers the score-ballot ones: any non-dictatorial method with three or more viable candidates can be gamed by someone, somewhere. Nothing on this page is a defect unique to Copeland, and nothing here makes STAR the safe choice.

So the useful questions are not "is it manipulable?" but:

- **How hard is the strategy to find?** Ali's compromise needs no polling at all; STAR's burial needs the two manipulators to know Dublin is the threat.
- **How badly does it backfire?** Burial in STAR can elect the buried candidate's rival; compromising in Ranked Robin risks electing the compromise you only lukewarmly wanted.
- **How often does the situation arise?** This profile has no Condorcet winner. That is what makes it fragile — with a Condorcet winner present, Ranked Robin is far harder to move.

Those are quantitative questions, and the repo answers them elsewhere: [VSE and PVSI](../../07_Concepts/topics/pvsi_strategic_incentive.md) measure strategic incentive across many simulated elections instead of one hand-picked profile. **A single constructed example proves a method *can* fail. It never establishes how often, and this page does not claim otherwise.**

## Reproduce it

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/manipulability_p3/cases/p3_sincere_ranked_robin.yaml
```

| Case | File |
|---|---|
| Sincere baseline (Ranked Robin) | [`p3_sincere_ranked_robin.md`](cases/cases_pages/p3_sincere_ranked_robin.md) |
| Zwicker's complete reversal | [`p3_manip_reversal_rr.md`](cases/cases_pages/p3_manip_reversal_rr.md) |
| The three-swap compromise | [`p3_manip_compromise_rr.md`](cases/cases_pages/p3_manip_compromise_rr.md) |
| Sincere STAR | [`p3_sincere_star.md`](cases/cases_pages/p3_sincere_star.md) |
| STAR manipulated by burial | [`p3_manip_star.md`](cases/cases_pages/p3_manip_star.md) |

Borda has no LH tabulator; its figures are cross-checked with [`pref_voting`](../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md).

## Notes on the source

Profile `P₃` and Definition 2.3 are from **William S. Zwicker, "Introduction to the Theory of Voting,"** Chapter 2 of the *Handbook of Computational Social Choice* — the same chapter behind [margins matter](../copeland_vs_borda_margins/README.md) and this repo's [social welfare function](../../07_Concepts/topics/social_welfare_function.md) page.

**One discrepancy worth recording.** The chapter's prose refers to "the two `e ≻ c ≻ a ≻ b ≻ d` voters," but the printed profile table gives that column as `e ≻ c ≻ a ≻ d ≻ b` — the last two are transposed. The book's own arithmetic settles it: only the **table** reading reproduces the stated Copeland scores (`e = 2`, `b = −2`, others `0`); the prose reading gives `d = −2` and `b = 0` instead. We use the table. The transposition does not affect the plurality claim, since those voters rank Athens above Dublin under either reading.

The city names are this repo's; the source uses bare `a`–`e`. Initials are preserved: **A**thens, **B**ergen, **C**ork, **D**ublin, **E**dinburgh.
