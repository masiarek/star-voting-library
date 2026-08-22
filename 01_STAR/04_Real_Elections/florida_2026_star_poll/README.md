# Florida 2026 — four STAR races on one open ballot

**Level: 201 · deep dive**

*A public, open-to-anyone online poll ran the 2026 Florida statewide ballot — U.S. Senate, Attorney General, Agriculture Commissioner, Chief Financial Officer — as four STAR races on a single ballot, with every candidate from every party on the same paper. It is small (25 ballots) and self-selected, so it settles nothing about Florida. What it does show, from real ballots rather than a constructed example, is **what an open score ballot records that a closed partisan primary structurally cannot**: cross-party support, non-zero backing for an unaffiliated candidate, and — in the headline race — a runoff decided by 7 of the 25 voters because everyone else scored both finalists the same.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xj8pxc) · **[results ↗](https://bettervoting.com/xj8pxc/results)** (election `xj8pxc`)

**▶ The full counts:** [Senate ↗](cases/cases_pages/bxj8pxc_senate.md) · [Attorney General ↗](cases/cases_pages/bxj8pxc_attorney_general.md) · [Agriculture ↗](cases/cases_pages/bxj8pxc_agriculture.md) · [CFO ↗](cases/cases_pages/bxj8pxc_cfo.md)

**▶ The data:** four engine cases in [`cases/`](cases/bxj8pxc_senate.yaml) · the frozen BV export [`bxj8pxc_bv_export.json`](cases/bxj8pxc_bv_export.json)

> **Not our election.** This poll belongs to someone else; the repo neither minted it nor casts ballots in it. The export here is a **snapshot frozen 2026-08-22**. The poll stays open to 2026-11-11, so the live page will keep moving away from these numbers — the frozen JSON, not the live page, is what the engine is checked against.

---

## The four races

Every race is single-winner STAR. "Tallied" is BetterVoting's count of ballots that scored at least one candidate in that race; `*` marks the incumbent.

| Race | Field | Tallied | Scoring round (top 2) | Automatic Runoff | Winner |
|---|:--:|:--:|---|:--:|---|
| [Agriculture Commissioner](cases/cases_pages/bxj8pxc_agriculture.md) | 5 | 25 | Matt The Welder (REP) **79** · Romagnano (DEM) 39 | 15 – 8 | Matt The Welder (REP) |
| [U.S. Senate (special)](cases/cases_pages/bxj8pxc_senate.md) | 7 | 22 | Nixon (DEM) **57** · Vindman (DEM) 47 | 6 – 1 | Nixon (DEM) |
| [Attorney General](cases/cases_pages/bxj8pxc_attorney_general.md) | 4 | 21 | Rodriguez (DEM) **50** · Lewis (DEM) 46 | 5 – 3 | Rodriguez (DEM) |
| [Chief Financial Officer](cases/cases_pages/bxj8pxc_cfo.md) | 4 | 18 | Smith (NPA) **37** · Collige (REP) 26 | 9 – 5 | Smith (NPA) |

Three things fall out of that table before any analysis:

- **No runoff reversals.** In all four races the scoring-round leader also wins the runoff, so this poll is not an example of STAR's headline behavior — for that see [Runoff reversals on BV](../runoff_reversal_bv_cases/README.md). The Attorney General race does split STAR from three *other* methods, though; [see below](#the-attorney-general-race-splits-the-methods).
- **The incumbent loses three of four.** Simpson `*` finishes 3rd in Agriculture, Moody `*` 3rd in the Senate race, Ingoglia `*` 3rd for CFO. Only Uthmeier `*` (Attorney General, 3rd in scoring) is in a race his party wins — and he doesn't win it either.
- **Two races put two same-party candidates in the runoff.** Both Senate finalists are Democrats; both Attorney General finalists are Democrats. That is a property of *this sample's* lean, not of STAR — but it is the mechanism worth understanding, and the Senate race below is where it is visible.

## The Senate race, in detail

Seven candidates for Marco Rubio's seat, all on one ballot: four Republicans, two Democrats, one unaffiliated (NPA). In the real closed primary these voters would have received one party's ballot and could have scored nobody outside it.

<!-- ballots:bxj8pxc_senate -->
*(No ballot art for `bxj8pxc_senate` — draw it with `build_style_ballot_images.py --from-yaml 01_STAR/04_Real_Elections/florida_2026_star_poll/cases/bxj8pxc_senate.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Moody (REP)*,Nixon (DEM),Vindman (DEM),Gillespie (NPA),Gleason (REP),Perry (REP),Rivera (REP)
&,&,&,5,&,&,&   # b-d67ygqqb
&,&,&,&,&,&,&   # b-7qr6fp6d
&,5,&,&,&,&,&   # b-dh7xj93b
&,5,5,&,&,&,&   # b-qkyw76rq
5,&,&,&,&,&,&   # b-cqcfrhgf
&,&,&,&,&,&,&   # b-6mwmcfmd
&,&,&,&,&,&,5   # b-8kq29hv8
0,5,5,4,0,0,0   # b-xfftm9yb
0,5,5,3,0,0,0   # b-gyvqdrry
0,0,0,0,0,0,0   # b-6ywyq88y
&,5,3,0,0,0,0   # b-9v7q4dvt
0,4,4,1,0,0,0   # b-6c2y3d3p
5,&,&,&,&,&,&   # b-3xdd4ptb
0,5,0,0,0,0,0   # b-9ry7jmwv
5,0,0,0,0,0,0   # b-rqd88v3w
0,5,4,1,0,0,0   # b-bk8xd8fw
0,5,5,4,1,1,1   # b-8bfw9dyf
0,&,5,&,&,&,&   # b-gffckf36
5,0,0,0,0,0,5   # b-6hfy233k
5,&,&,&,&,&,&   # b-ypm6vddm
5,&,&,&,&,&,&   # b-pfvxtxmh
2,5,4,3,2,1,0   # b-fhgbkw3x
0,5,4,1,0,0,0   # b-mybbty26
0,3,3,1,0,0,0   # b-xc3yfg8c
5,0,0,0,5,5,5   # b-vjpmvx6c
```
<!-- /ballots -->

<!-- report:bxj8pxc_senate -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 25 ballots. Note: 2 of 25 ballots are marked as abstentions.
Count × Moody (REP)*,Nixon (DEM),Vindman (DEM),Gillespie (NPA),Gleason (REP),Perry (REP),Rivera (REP)
    4 ×            5,          &,            &,              &,            &,          &,           &
    2 ×            &,          &,            &,              &,            &,          &,           &
    2 ×            0,          5,            4,              1,            0,          0,           0
    1 ×            &,          &,            &,              5,            &,          &,           &
    1 ×            &,          5,            &,              &,            &,          &,           &
    1 ×            &,          5,            5,              &,            &,          &,           &
    1 ×            &,          &,            &,              &,            &,          &,           5
    1 ×            0,          5,            5,              4,            0,          0,           0
    1 ×            0,          5,            5,              3,            0,          0,           0
    1 ×            0,          0,            0,              0,            0,          0,           0
    1 ×            &,          5,            3,              0,            0,          0,           0
    1 ×            0,          4,            4,              1,            0,          0,           0
    1 ×            0,          5,            0,              0,            0,          0,           0
    1 ×            5,          0,            0,              0,            0,          0,           0
    1 ×            0,          5,            5,              4,            1,          1,           1
    1 ×            0,          &,            5,              &,            &,          &,           &
    1 ×            5,          0,            0,              0,            0,          0,           5
    1 ×            2,          5,            4,              3,            2,          1,           0
    1 ×            0,          3,            3,              1,            0,          0,           0
    1 ×            5,          0,            0,              0,            5,          5,           5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Nixon (DEM)     -- 57 -- First place
   Vindman (DEM)   -- 47 -- Second place
   Moody (REP)*    -- 37
   Gillespie (NPA) -- 23
   Rivera (REP)    -- 16
   Gleason (REP)   --  8
   Perry (REP)     --  7
 Nixon (DEM) and Vindman (DEM) advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nixon (DEM)     -- 6 -- First place
   Vindman (DEM)   -- 1
   Equal Support   -- 18
 Nixon (DEM) wins.
   Runoff math:
     25  ballots cast
   − 18  Equal Support (no preference between the two finalists)
     ──
      7  voters with a preference  (majority = 4)
           Nixon (DEM) 6 (86%)  ·  Vindman (DEM) 1 (14%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Nixon (DEM)
```
<!-- /report -->

### The runoff is decided by 7 people

This is the number to take away. The Automatic Runoff is Nixon 6, Vindman 1 — and **Equal Support 18**. Of 25 ballots cast, 18 scored the two finalists identically (most of them by scoring both Democrats 0, or by leaving the race blank), so they express no preference between the two candidates who reached the runoff and count for neither.

```text
  25  ballots cast
− 18  Equal Support (no preference between the two finalists)
  ──
   7  voters with a preference  (majority = 4)
        Nixon (DEM) 6 (86%)  ·  Vindman (DEM) 1 (14%)
```

An 86% runoff win, stated without its denominator, sounds like a landslide; it is six people. This is exactly why the engine prints the [runoff percentages](../../01_Learn/the_count/runoff_percentages.md) against the decided-voters denominator with the Equal Support gap named inline, rather than letting a reader infer it — and why **Equal Support** is a reported bucket rather than a rounding error. (In a real electorate the same shape appears whenever both finalists come from one faction: everyone outside that faction is suddenly a no-preference voter.)

Nixon is also the **[Condorcet winner](../../../07_Concepts/topics/condorcet/README.md)** here — she beats every other candidate head to head, so the runoff slot is not doing any work in this particular result. Perry is the Condorcet loser.

## The Attorney General race splits the methods

The Senate race is the one the poll was built around, but the **Attorney General** race is the one that separates counting methods. Four candidates, two per party, 21 ballots tallied — and the engine's divergence block reports:

```text
[Divergence from STAR]
  STAR                   = Rodriguez (DEM)
  Choose-One (Plurality) = Lewis (DEM)   (differs from STAR)
  RCV-IRV                = Lewis (DEM)   (differs from STAR)
  Approval               = Lewis (DEM)   (differs from STAR)
```

Rodriguez leads the scoring round 50–46, wins the Automatic Runoff 5–3, **and is the Condorcet winner** — he beats every other candidate head to head. Ranked Robin agrees with STAR. Choose-One, Approval and instant runoff all elect Lewis instead.

**Read that with the engine's own caveat attached, because it matters here:** 6 of 25 ballots (24%) gave two or more candidates the *same* non-zero score. A score ballot has to be converted before a ranked or single-mark method can read it, and those ties were resolved by candidate priority order — so the non-STAR winners partly reflect a conversion convention rather than anything the voters expressed. This is a real divergence on real ballots, not a constructed one, but with n = 21 and a quarter of the ballots needing tie-break help it is **suggestive, not decisive**. The honest claim is the narrow one: on this ballot set the Condorcet winner is what STAR and Ranked Robin return, and the methods that read only a voter's top choice return someone else.

## What the open ballot recorded that a closed primary could not

Two findings, both checkable against the ballots above.

**An unaffiliated candidate got measured.** Neil Gillespie (NPA) was on no primary ballot at all and therefore has no primary vote total. On this ballot he scores **23**, fourth of seven, ahead of three of the four Republicans — almost entirely as *secondary* support: of the 13 ballots whose top score went to a Democrat, **8 (62%)** gave Gillespie a non-zero score, every one of them between 1 and 4. None of that support is expressible on a choose-one ballot, and none of it would have appeared anywhere in the official returns.

**The two leans used the ballot differently.** Grouping each ballot by the party of the candidate it scored highest:

| Ballots whose top score went to… | n | Used any intermediate score (1–4) |
|---|:--:|:--:|
| a Republican | 8 | **0** |
| a Democrat | 13 | **9** |

Every single Republican-leaning ballot is pure 0s and 5s — approval-style bullet voting on a 0–5 scale. Democratic-leaning ballots use the middle of the scale freely. With n = 21 that is an observation about 21 people, not about either party; it is offered as something the ballots *record*, which is the point of keeping the raw file.

## Where the engine and BetterVoting disagree

Same winners in all four races, but not the same denominators — and the difference is systematic:

| Race | All-blank ballots | All-explicit-`0` ballots | LH abstentions | BV abstentions |
|---|:--:|:--:|:--:|:--:|
| Agriculture | 0 | 0 | 0 | 0 |
| Senate | 2 | 1 | **2** | **3** |
| Attorney General | 2 | 2 | **2** | **4** |
| CFO | 4 | 3 | **4** | **7** |

BetterVoting counts a ballot that scores every candidate an explicit `0` as an *abstention*; the engine counts it as a cast vote whose scores happen to be zero. LH's abstention count is the all-blank ballots and nothing else. Neither changes a winner here — it changes what "of N voters" means, which is why the Senate runoff reads as 15 Equal Support out of 22 on BetterVoting and 18 out of 25 in the engine report above.

That divergence is not new and not a finding of this page: it is the [abstain, blank & zero handling](../abstain_bugs/README.md) set, and the underlying dispute is [bettervoting#884](https://github.com/Equal-Vote/bettervoting/issues/884). What this poll adds is a real-world instance of it appearing in **three races at once**, in an election nobody constructed to trigger it.

## What this poll cannot tell you

Worth stating plainly, because the temptation to over-read a small clean dataset is strong:

- **25 self-selected ballots.** An open online poll anyone can find and vote in is a convenience sample. The real Senate primary drew about 2.9 million votes. Nothing here estimates Florida opinion.
- **Different contests.** The poll is one all-candidate field; Florida's primary is two closed, party-separated contests whose winners advance. A poll winner and a primary winner are not the same object, so "the poll disagreed with the primary" is not by itself a method effect.
- **Still open.** Votes keep arriving. Any figure on this page is the 2026-08-22 snapshot, and the frozen export is what makes it reproducible.

Re-weighting a sample like this toward the real electorate's partisan composition is a reasonable thing to try, and it moves the result substantially — but it is an analysis *of* the poll rather than a result *from* it, and with 21 partisan-leaning ballots in two cells it inherits all of the noise above.

---

**Related:** where the runoff denominator comes from → [runoff percentages](../../01_Learn/the_count/runoff_percentages.md) · the abstention divergence in full → [abstain, blank & zero handling](../abstain_bugs/README.md) · another real public poll, read the same way → [pres24 range usage](../pres24_range_usage/README.md) · every BV-backed case → [the BV registry](../../../07_Concepts/YAML_test_case_index/BV_registry.md)
