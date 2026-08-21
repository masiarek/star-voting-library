# Coarse ballots and the tie ladder — what a three-star election does to STAR's tiebreakers

**Level: 301 · deep dive**

**One line:** shrink the range voters actually use — 0/1/2 instead of the full 0–5 — and ties stop being exotic; three quarters of a million such elections, counted across the Equal Vote methods and classified one by one, produced **no tie category this library did not already have a lesson for**, but they did show that a coarse ballot quietly *shortens* the ladder, so the lot decides both more often and one rung earlier.

Companion to [Why build "silly" tie elections?](why_contrived_tie_cases.md), which maps the branches by hand for single-winner STAR. This page is the machine version of the same question, widened to Bloc, proportional STAR, Ranked Robin and Approval — and it is what finally answered the *"is that map complete?"* the older page left open.

---

## The experiment

Ties are the corner this library teaches from, and on a full 0–5 ballot they are rare enough that every tie case here had to be *designed*. Drop the scale voters use to three values and you no longer have to design anything: three ballots over three candidates collide constantly. Same election rules, same engine, the corners just get crowded.

That is not only a testing trick. The literature that supports 0–5 in the first place does not obviously support *six* levels: as the [wider-scale page](../../../01_STAR/01_Learn/properties_and_limits/STAR_nonstandard_scale.md) records, Hillinger — reading the same convergence across grading, product ratings and opinion scales — would hand a **general electorate a three-level ballot** and reserve five or six for expert committees. So "what does STAR do on a three-value ballot" is a live design question, not a stress test.

The sweep is [`tie_taxonomy_sweep.py`](../../../STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py). It enumerates profiles (exhaustively where the space is small enough, sampled where it is not), counts each one, reduces every tie to a signature, and looks that signature up in a table of the categories this repo teaches. A signature with no entry prints under **UNMAPPED** — which is the entire point. It reads two engine surfaces and never re-counts anything:

- the [machine-readable result contract](../../tabulation_engines/result_schema.md) (`--json`), whose `tiebreaks: []` is a positive claim that no rung fired; and
- `starvote`'s own round narration at `verbosity=2`, captured in process — the only surface that names the **deterministic** rungs on a multi-winner count.

Comparing the two is itself a check, and it is how the finding at the bottom of this page turned up.

```bash
python STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py
```

## The result: no new categories

**445,154 elections counted. 275,412 tie events. Zero unmapped.**

Three to four candidates, three to six voters, one to three seats, on the two coarse scales `{0,1,2}` and `{0,1,5}`, through STAR, Bloc STAR, Allocated Score, SSS, RRV, Ranked Robin, Approval, and Choose-One as a control. Ties were dense — better than one tie event per two elections — and every one of them reduced to a signature the table below already had a lesson for.

Four categories in the map went *unreached*, and all four are the same category wearing different hats: the **five-star rung**, at both STAR loci and both Bloc loci. That is not a hole in the search. It is the next section arriving early: a coarse scale cannot reach that rung, and an exhaustive check says why — on a `{0,1,5}` ballot the smallest profile that can even *pose* the question needs **eight voters**, because the rung fires only when two candidates tie on total score while holding *different* numbers of 5s, and 5-plus-ones arithmetic does not allow that any sooner. A separate full-scale run (`--scores 0,1,2,3,4,5`) walks into both inside its first 20,000 elections.

Every tie the sweep produced landed in a category that already has a page. That is a *negative* result, and negative results are worth stating plainly: it does not prove the taxonomy is complete, it says that a search this shape did not dent it. What it does support is a narrower and more useful claim — **coarsening the ballot changes how often each branch is taken, not which branches exist.**

| ID | Tie category | Where the lesson lives |
|----|--------------|------------------------|
| **S-F1** | STAR scoring tie → head-to-head (matchups won) picks the finalists | [the ladder set](../../../01_STAR/03_Criteria/tie_break_ladder/README.md) · [matchups won vs. preference votes](../../../01_STAR/01_Learn/Tie_Breaking_STAR/matchups_won_vs_preference_votes.md) |
| **S-F2** | STAR scoring tie → five-star rung picks the finalists | [BV2180, the ice-cream ladder](../../../01_STAR/03_Criteria/tie_break_ladder/bv2180_fp62p2_ice_cream_ladder.md) |
| **S-F3** | STAR scoring tie → dead rung → lot picks the finalists | [the dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| **S-R1** | STAR runoff tie → higher total score wins | [BV830](../../../01_STAR/03_Criteria/tie_break_ladder/bv830_vb3xv2_no_condorcet_tie_score.md) |
| **S-R2** | STAR runoff tie → five-star rung wins | [dead-rung case 04](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| **S-R3** | STAR runoff tie → dead rung → lot wins | [`jfk7pd`](../../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) |
| **B-F1 · B-F2 · B-F3** | the same three finalist rungs, inside a Bloc seat | [Bloc tiebreaks](../../../02_STAR_Bloc/01_Learn/bloc_tiebreaks.md) · [tied at every rung](../../../02_STAR_Bloc/02_Examples/b484mbm_tie_every_rung.md) |
| **B-R1 · B-R2 · B-R3** | the same three runoff rungs, inside a Bloc seat | [BV750](../../../02_STAR_Bloc/02_Examples/bv750_tie_breaking_bloc.md) |
| **P-1** | STAR-PR / SSS / RRV: a tie on the round's weighted total → straight to the lot | [tiebreak ladders § STAR-PR](../../tabulation_engines/tiebreak_ladders.md) |
| **R-1 · R-2 · R-3** | Ranked Robin Copeland tie → 1st Degree, 2nd Degree, lot | [degrees of ties](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) · [the dead heat](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/dead_heat_lot_tiebreak.md) |
| **R-4** | Bloc Ranked Robin: the last seat ties → lot | [RR tiebreaks](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/README.md) |
| **A-1 · A-2** | Approval: a tie for the win, or on the seat cut line → candidate priority order | [approval indeterminacy](../../../04_Approval/01_Learn/approval_indeterminacy.md) · [multiwinner Approval](../../../04_Approval/01_Learn/Multiwinner_Approval/README.md) |
| **C-1 · C-2** | Choose-One: a tie for first, or on the SNTV cut line → lot | [the dead-tie lunch](../../../06_Other/Plurality/cases/cases_pages/lunch_choose_one_dead_tie.md) |
| **X-1** | multi-winner: candidates tie **above** the cut line — the set is safe, the order is not | [the silent tiebreak](silent_tiebreak.md) |
| **X-2** | a winner elected with **zero support** — nobody scored anybody | [the zero-support election](../../../method_comparisons/zero_support_election/README.md) |
| **X-3** | a tie the engine's report narrates that the JSON contract does not list | [the result contract](../../tabulation_engines/result_schema.md) |
| **X-4** | a rung eliminates **part** of the tied group and the survivors carry on | [matchups won vs. preference votes](../../../01_STAR/01_Learn/Tie_Breaking_STAR/matchups_won_vs_preference_votes.md) |

Three of those are shapes rather than rungs — X-1, X-2 and X-4 can happen under any method — and they are the entries that were hardest to reach by hand. X-4 in particular is the branch the older map called *"the branch symmetry cannot test"*: it needs three or more candidates tied and a rung that separates **some** of them, which a rotation-symmetric probe can never build, because a symmetric profile separates all or none.

## What a coarse ballot actually changes

Same shape of election every time — three candidates, four voters, 20,000 profiles per row (the `{0,1}` row is smaller because the whole space is only 330 profiles, so that row is a complete census rather than a sample). The only thing varying is **which score values voters are allowed to use** on a ballot whose declared maximum is still 5.

**Scoring-round ties — which rung settled the finalists**

| Voters use | Scoring ties | → head-to-head | → five-star | → lot | lot's share |
|---|---|---|---|---|---|
| `{0,1}` | 114 of 330 (34.5%) | 0 | 0 | 114 | **100%** |
| `{0,1,2}` | 4,734 of 20,000 (23.7%) | 1,136 | 0 | 3,598 | **76.0%** |
| `{0,1,2,3}` | 3,522 (17.6%) | 1,298 | 0 | 2,224 | **63.1%** |
| `{0,1,2,3,4}` | 2,822 (14.1%) | 1,225 | 0 | 1,597 | **56.6%** |
| `{0,1,2,3,4,5}` | 2,368 (11.8%) | 1,077 | 567 | 724 | **30.6%** |

**Automatic Runoff ties — which rung settled the seat**

| Voters use | Runoff ties | → score | → five-star | → lot | lot's share |
|---|---|---|---|---|---|
| `{0,1}` | 114 of 330 (34.5%) | 0 | 0 | 114 | **100%** |
| `{0,1,2}` | 6,092 of 20,000 (30.5%) | 2,630 | 0 | 3,462 | **56.8%** |
| `{0,1,2,3}` | 5,722 (28.6%) | 3,575 | 0 | 2,147 | **37.5%** |
| `{0,1,2,3,4}` | 5,714 (28.6%) | 4,229 | 0 | 1,485 | **26.0%** |
| `{0,1,2,3,4,5}` | 5,909 (29.5%) | 4,657 | 646 | 606 | **10.3%** |

Two monotone trends, and the second is the interesting one.

**Ties get commoner as the ballot gets coarser** — 11.8% of full-scale elections have a scoring tie, 34.5% of approval-shaped ones do. No surprise: fewer distinct values, more collisions.

**But when a tie does happen, the lot decides far more often.** On the runoff, the lot buys the seat in 10% of full-scale ties and 57% of `{0,1,2}` ties — nearly six times as often. And the mechanism is not "coarse ballots are vaguer". Look at the five-star column: it is **exactly zero on every row that omits the 5**.

## The rung that dies

STAR's second tiebreaker counts ballots **at the maximum of the scale** — fives, not fours. The [dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) page states this for the case where the tied candidates happen to hold no 5s. The sweep makes the stronger version visible: if the *electorate* never uses the top of the scale, the rung is not occasionally dead, it is **structurally absent**, and STAR's three-rung ladder is a two-rung ladder for that election. The `{0,1,2,3,4}` row is the cleanest proof — a five-level ballot, plenty of granularity, and still not one tie in 20,000 elections reached the five-star rung, because nobody scored a 5.

Which raises the question the tables cannot answer: is the top of the scale **5**, or is it whatever the ballot says it is?

`starvote` takes the maximum as a parameter, so both readings are runnable. Here are four ballots, read twice — once as a 0–5 ballot on which voters were merely coarse, and once as a genuine 0–2 ballot:

```text title="Abridged for the lesson — the two runs, tiebreaker rungs only"
Ada,Ben
1,2
1,2
1,0
2,1

# maximum_score=5  — "a 0–5 ballot, coarsely used"
[Automatic Runoff Round]                Ada 2, Ben 2      → tied
[Automatic Runoff Round: 1st tiebreaker] Ada 5, Ben 5     → still tied
[Automatic Runoff Round: 2nd tiebreaker] most votes of score 5:  Ada 0, Ben 0
                                         → DEAD RUNG. The lot elects Ada.

# maximum_score=2  — "a genuine 0–2 ballot"
[Automatic Runoff Round]                Ada 2, Ben 2      → tied
[Automatic Runoff Round: 1st tiebreaker] Ada 5, Ben 5     → still tied
[Automatic Runoff Round: 2nd tiebreaker] most votes of score 2:  Ben 2, Ada 1
                                         → Ben wins. No lot, no banner.
```

Identical votes. **Different winner** — and, more to the point, a different *kind* of decision: under one reading the ballots settle it, under the other the lot does. Nothing about the electorate changed; what changed is the number the ballot paper declares as the top.

This one is [LH-only by construction](../../tabulation_engines/tiebreak_ladders.md): BetterVoting has no scale parameter, and this repo's own YAML CLI pins the maximum at 5 as a [teaching guardrail](../../../01_STAR/01_Learn/properties_and_limits/STAR_nonstandard_scale.md#worked-example-star-on-a-010-ballot), so the second run is a library call rather than a case file. It is the mirror of that page's question: widening the scale changes *who advances*; narrowing it changes *who breaks the tie*.

## The other end: coarse, but at the top

Coarse does not have to mean *low*. Run the same sweep on scales that keep the 5 and drop the middle — `{4,5}`, `{3,4,5}`, `{0,4,5}`, `{0,5}`, and the degenerate `{5}` — and the picture inverts. **272,012 elections, still zero unmapped, and this time every one of the 25 categories in the map was reached**, including the four the coarse-low sweep could not touch: with 5s everywhere the five-star rung fires constantly (1,043 scoring ties and 828 runoff ties settled by it, plus 1,517 and 1,772 inside Bloc seats).

So the two halves of the experiment answer different halves of the question:

| Sweep | Elections | Unmapped | Categories reached | What it is good for |
|---|---|---|---|---|
| coarse-low — `{0,1,2}`, `{0,1,5}` | 445,154 | **0** | 21 of 25 | ties are dense, and the lot decides them |
| top-heavy — `{4,5}`, `{3,4,5}`, `{0,4,5}`, `{0,5}`, `{5}` | 272,012 | **0** | **25 of 25** | ties are dense *and* the ballots still settle them |

That is worth stating as a claim about STAR rather than about the sweep: **the five-star rung is the part of the ladder that depends on the electorate's habits, not on the electorate's size.** Two publics can be equally indecisive and land in completely different places — one where the votes finish the job, one where the lot does — purely on whether the top of the scale gets used. `{0,5}` is the case with a name: an **approval-shaped** STAR ballot, where every candidate gets either full support or none — what a strategically-pressured electorate drifts toward — and on a plain draw it keeps the rung alive. (Tighten it further, to one 5 and the rest 0, and you have true **bullet voting**, which is a shape rather than a scale and behaves quite differently — see the next section.)

## Building ties on purpose — six ways, and what each one costs the ladder

`--scores` narrows the values a voter may use. A **shape** constrains how the ballots relate to *each other*, which is the other half of the space and the half where the classic probes live. All six are in the tool (`--shapes bullet flat rotation mirror clone`), all six are published or folklore constructions, and — the headline again — **none of them found a category the map does not have.** What they differ in is *efficiency* and *depth*: how often they tie at all, and how far down the ladder the tie gets before something settles it.

Three candidates, four voters, single-winner STAR, full 0–5 scale unless the row says otherwise. Rows marked *(whole space)* are exhaustive rather than sampled.

| Shape | What the electorate looks like | Elections | Scoring ties | Runoff ties | Of those → lot |
|---|---|---:|---:|---:|---:|
| `random` | a plain draw — the baseline | 2,000 | 11.8% | 31.1% | 16.2% |
| `bullet` | every voter maxes one candidate, zeroes the rest | 35 *(whole space)* | 48.6% | 22.9% | **100%** |
| `flat` | every voter scores the whole field the same | 126 *(whole space)* | **100%** | **100%** | **100%** |
| `rotation` | Moulin's witness — k voters per cyclic rotation | 76 *(whole space)* | **100%** | 47.4% | **100%** |
| `clone` | one candidate's column copied onto another | 2,000 | 55.0% | 60.5% | 87.6% |
| `mirror` | each ballot paired with its reflection | 2,000 | **100%** | **100%** | 32.4% |
| `mirror`, scores `{0,5}` | the same, on a symmetric two-value scale | 2,000 | **100%** | **100%** | **100%** |

`rotation` reports the same rates at three voters and at six — k voters per rotation changes the size of the electorate, not its symmetry, which is the point Moulin's construction is making.

**The mirrored electorate is the interesting one**, because it ties everything and *still lets the ballots decide two times in three*. Reflecting a ballot through the middle of the scale does three things at once, and they are worth separating:

- it **flips every preference**, so each pair of ballots contributes one preference each way — the Automatic Runoff ties **by construction**, in every election, always;
- it **equalises every total**, since a value and its reflection sum to the same constant for whoever holds them — so the score rung ties too, always;
- but it does **not** equalise the five-star counts. Over one pair, candidate X collects a 5 from the original ballot when `X` scored 5 and from the reflection when `X` scored 0, so X's count is *(their fives) + (their zeros)* — a number that still differs between candidates. That rung does the deciding, on 68% of them.

Narrow the scale to `{0,5}` and that last line collapses: now every score is either a 5 or a 0, so *(fives) + (zeros)* is simply the ballot count, identical for everyone. The rung dies and the lot takes all of them.

Which is the same dead rung as [the section above](#the-rung-that-dies), reached from the opposite direction. There, nobody used the top of the scale. Here, **everybody uses it, symmetrically** — and STAR cannot tell those two electorates apart, because the rung it would use to tell them apart is the one both of them disabled.

## The bottom of the scale

Push coarseness to its limit — every voter scores every candidate `0` — and you get the shape at the very bottom of the taxonomy: **[the zero-support election](../../../method_comparisons/zero_support_election/README.md)**, three ballots and five nominees counted six ways. Every method elects the first name on the lot, which tells you nothing; what the six reports do *not* agree on is how loudly they admit it, from Choose-One appending `, by lot` to the winner line down to Approval's one-line note. That folder is the X-2 witness, worked out.

## What the sweep found in our own code

A sweep whose job is to look for unlisted tie shapes will also, if it is honest, look at whether the *reporting* of the listed ones is intact. It was not.

The [result contract](../../tabulation_engines/result_schema.md) defines an empty `tiebreaks: []` as a **positive claim** that the ballots alone decided — that is the field that catches a right-winner-wrong-path result, and the reason the contract is worth more than 567 winner-only answer keys. A fix in 2026-08-21 had taught the builder to report the **lot**. But a runoff tie broken by a *deterministic* rung fires no lot event and belongs to neither of the builder's replays, so it was reported by nothing at all. Running the sweep against both surfaces at once made that visible immediately: thousands of single-winner STAR elections whose printed report said, in full, *"Automatic Runoff Round: First tiebreaker — the highest-scoring candidate wins"*, and whose JSON said `tiebreaks: []`.

Then the same question, asked of the committed corpus rather than of generated profiles: **16 real cases in this library were making that false claim**, twelve at the `score` rung and four at `five-star`. Among them:

| Case | Its whole subject | What the JSON said |
|---|---|---|
| [`bv830_vb3xv2_no_condorcet_tie_score`](../../../01_STAR/03_Criteria/tie_break_ladder/bv830_vb3xv2_no_condorcet_tie_score.md) | a runoff tie **resolved by score** | `tiebreaks: []` |
| `tie_break_04_runoff_five_star_breaks` | a runoff tie **resolved by five-star** | `tiebreaks: []` |
| `BV_Library_star_runoff_tie_score_resolves` | the name is the finding | `tiebreaks: []` |

Files named for the rung the machine-readable result declined to mention. The fix is the mirror of the replay that already existed: `resolve_runoff()` walks STAR's second ladder — preference round, then total score, then the scale-maximum count, then the lot — through `starvote`'s own round functions, so it cannot disagree with the count, and it is pinned in both directions (`rounds.runoff.tied` and a `stage: "winner"` entry must agree, so a swallowed tie *and* an invented one both fail). Schema **1.2.0**; the full account is in [the contract's versioning section](../../tabulation_engines/result_schema.md#versioning).

**And the part that should sting.** This repo files a fair number of [bugs against BetterVoting](../../about_this_repo/upstream_bug_reports.md), several of them about exactly this — tie-break transparency, a `tieBreakType` that says `random` when nothing tied, an IRV tie broken without being flagged. So the frozen BV exports were the obvious control. Across the eight STAR races in the corpus whose Automatic Runoff was an exact tie, BetterVoting named the rung **every time** — `score`, `five_star`, `random` — and agreed with this engine on all eight once you account for its documented escalate-to-the-worst-rung reporting. The engine we audit had the disclosure. The contract we built to audit it did not.

And the comparison is only *possible* because of the fix. Take [BV2180, the ice-cream ladder](../../../01_STAR/03_Criteria/tie_break_ladder/bv2180_fp62p2_ice_cream_ladder.md): its scoring round reaches the five-star rung and its runoff is then settled by score. BetterVoting reports one value per race, escalated to the worst rung — `five_star` — which before 1.2.0 sat opposite a contract that listed the five-star finalists tie and *nothing about the runoff at all*. The two would have read as agreeing, by accident, on half the story. Now the contract lists both rungs and the escalation reconciles for a stated reason, which is the difference between a cross-check and a coincidence.

Two blind spots survive, and the sweep measures both rather than asserting them away:

- **Bloc and PR rungs below the lot are still invisible to the contract.** Those rungs run inside `starvote`'s counting functions, which report nothing back, and there is no replay for them that would not amount to re-deriving the count. The sweep flags each occurrence as X-3, so the size of the gap is a number rather than a caveat.
- **Ranked Robin reports a single-winner dead heat twice**, once as `copeland_leaders` and once as `seat_cutoff` — at one seat those are the same tie seen from both sides. Harmless for a conformance diff that compares tied sets and outcomes; wrong if anyone counts entries.

## Running it yourself, and what not to conclude

```bash
# the default sweep: 3-4 candidates, 3-4 voters, scales {0,1,2} and {0,1,5}
python STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py

# the degenerate probe on its own
python STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py --all-zeros

# top-heavy scales, which is where the five-star rung lives
python STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py --scores 4,5 --scores 0,4,5

# the constructed shapes, alone or together
python STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py --shapes mirror rotation clone

# one witness case file per category, written out
python STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py --witness-dir /tmp/witnesses
```

The honest limits, since the headline is a negative result:

- **Small elections only.** Three to six voters, three or four candidates, one to three seats. Ties are dense there and vanishing anywhere else, which is the point — but a category that only appears at scale would not show up.
- **Sampled, not exhaustive, above a few thousand profiles.** Every row of the scale tables above is either a complete census (`{0,1}`, and the `bullet` / `flat` / `rotation` shapes) or a fixed-seed sample of the same size, so the rows are comparable to each other; none of them is a proof.
- **`mirror` can put values on the ballot you did not ask for.** A reflection is closed inside `--scores` only when that set is symmetric about its own midpoint: `{0,5}` and the full scale are, `{0,1,5}` is not — reflecting a 1 there gives a 4. So a rung the mirrored sweep reaches on an asymmetric set may have been reached by the extra values rather than by the symmetry. The tool says so in its own docstring; the tables above use symmetric sets only.
- **RCV-IRV and STV are out of scope.** This is the Equal Vote method set. IRV's elimination tie is a genuinely different animal — it strikes mid-count and changes every round after it — and it has its own pages: [parallel universe tiebreaking](parallel_universe_tiebreaking.md), [batch elimination](batch_elimination.md), [the load-bearing tiebreak](load_bearing_tiebreak.md).
- **"No unmapped categories" is a statement about this search**, not a theorem. The one thing it does license: the [v1 map](why_contrived_tie_cases.md) drawn by hand for single-winner STAR extends to Bloc, proportional STAR, Ranked Robin and Approval without needing a new branch — which is what that page's own "natural extensions later" note was asking.

## See also

- [Ties & tie-breaking — the topic hub](README.md) · [Ties Are Forced](ties_are_forced.md) · [Why build "silly" tie elections?](why_contrived_tie_cases.md)
- [The zero-support election](../../../method_comparisons/zero_support_election/README.md) — the X-2 witness, six methods on three blank ballots
- [Tiebreak ladders — every method, every engine](../../tabulation_engines/tiebreak_ladders.md) · [the result contract](../../tabulation_engines/result_schema.md)
- [Unorthodox STAR — a scale wider than 0–5](../../../01_STAR/01_Learn/properties_and_limits/STAR_nonstandard_scale.md) — the same knob turned the other way
