# STAR Voting — Education & Test-Case Library

**Score every candidate 0–5; the two highest-scoring candidates meet in an automatic runoff; whichever finalist more voters scored higher wins.** That's **STAR Voting** — one better ballot that [quietly fixes a whole list of election problems](01_STAR/01_Learn/getting_started/STAR_benefits.md): **vote your heart, no more spoilers, a winner the majority actually likes.** And it's [refreshingly new](01_STAR/01_Learn/STAR_history.md) — first proposed in 2014, with the lessons of a century of older methods baked in.

## What this library is

<!-- --8<-- [start:what-this-is] -->
<!-- Invisible marker: the website homepage (index.md) inlines the paragraph below
     into its hero, beside the ballot image, under its own "What this library is"
     headline. Don't delete these comment lines. -->
A library for learning, teaching, and debating **[STAR Voting](01_STAR/01_Learn/STAR_start_here.md)** (Score Then Automatic Runoff). It puts STAR first — and earns your trust by testing STAR honestly against every method it's compared to, with a real tabulation engine and runnable example elections behind every claim. The even-handedness *is* the argument: the STAR case is stronger because you can check it yourself.
<!-- --8<-- [end:what-this-is] -->

<!-- --8<-- [start:below-hero] -->
<!-- Invisible marker: the website homepage (index.md) inlines everything from here
     to the matching [end:below-hero] marker at the bottom of this file, placing its
     own hero (headline + ballot image) above it. Don't delete these comment lines. -->

**Looking for something specific? → [Start Here](07_Concepts/00_START_HERE.md)** routes you by what you want — learn STAR, see what's broken about voting today, compare methods even-handedly, or run the engine yourself.

Under the hood it does three things:

1. **Teaches** — concept pages and worked examples, organized by level: [Voting 101](07_Concepts/curriculum/CURRICULUM_101.md) (the basics) · [201](07_Concepts/curriculum/CURRICULUM_201.md) (reading results & comparisons) · [301](07_Concepts/curriculum/CURRICULUM_301.md) (proportional, criteria, theory).
2. **Proves** — every claim is backed by a runnable election: a single [YAML file a person reads and the engine runs](YAML_library/why_yaml_test_cases.md).
3. **Cross-verifies with BetterVoting** — import a real election from [BetterVoting](https://bettervoting.com) (the Equal Vote Coalition's free STAR platform), re-tabulate it independently, and confirm the official winner — turning real elections into regression cases that catch and guard BetterVoting's bugs (turnout undercounts, tie mislabels, abstention miscounts).

Built on a vendored fork of Larry Hastings' [`starvote`](https://github.com/larryhastings/starvote) engine.

---

## The YAML election file

Every claim in this library is backed by one of these — a whole election in a file a person can read and the engine can count:

```yaml
voting_method: STAR
num_winners: 1
ballots: |-
  Ann,Bob,Cal
  5,4,0
  3,5,2
  0,3,5
expected_winners:
- Bob
```

This exact election is the repo's **canonical leading example** — it lives as a runnable file ([`bv2187_qrw6wb_ann-bob-cal.yaml`](01_STAR/02_Examples/cases/bv2187_qrw6wb_ann-bob-cal.yaml) · [reader page](01_STAR/02_Examples/cases/cases_pages/bv2187_qrw6wb_ann-bob-cal.md)), is reused verbatim across the intro docs, and runs **[live on BetterVoting ↗](https://bettervoting.com/qrw6wb/results)** (election `qrw6wb`). The registry of all reusable teaching elections (and the freeze rule that keeps them stable) is [TIPS — Canonical Elections](07_Concepts/tips/TIPS_canonical_elections.md).

**Why the format is YAML, what every field does, and what happens to the file once you run it → [YAML election files — why, what, how](YAML_library/README.md)** — the format's front door, with the [fill-in authoring template](YAML_library/YAML_authoring_template.md) one click further. House style keeps examples **small** ([how many voters?](07_Concepts/tips/TIPS_choosing_voter_counts.md)), and the ladder that settles a dead heat is [STAR Tie-Breaking — The Full Chain](01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md).

---

## Browse the library

The same ten sections as the sidebar, in the same order — each one's landing page says what's inside and indexes its runnable cases.

| Section | What's in it |
|---|---|
| ⭐ **[01 STAR](01_STAR/README.md)** | The headline method, one seat. The lessons in [`01_Learn/`](01_STAR/01_Learn/README.md) — the ballot, the two rounds, tie-breaking, the honest limits — then the runnable examples, the [real BetterVoting elections](01_STAR/04_Real_Elections/README.md), and the criteria pages. |
| **[02 STAR Bloc](02_STAR_Bloc/README.md)** | Several seats at once, *majoritarian*: the same ballot, run once per seat — and, just as importantly, when **not** to use it. |
| **[03 STAR PR](03_STAR_PR/README.md)** | Several seats at once, *proportional*: the same score ballot counted so seats reflect the electorate's proportions (`sss` · `allocated` · `rrv`). |
| **[04 Approval](04_Approval/README.md)** | Approve or don't — Score voting at one bit of resolution. Enormous gain in expressiveness over choose-one, for almost no ballot complexity. |
| **[05 Ranked Robin](05_Ranked_Robin/README.md)** | Ranked ballots counted head-to-head, so the candidate who beats the most rivals wins — the friendly upgrade for people who like ranking. |
| **[06 Other methods](06_Other/README.md)** | Taught, not promoted: Choose-One (Plurality), [RCV-IRV](06_Other/RCV_IRV/README.md), STV, Range/Score, and the historical also-rans — here for honest comparison. |
| **[07 Concepts](07_Concepts/README.md)** | The cross-method half: the [curriculum](07_Concepts/CURRICULUM.md) (101 / 201 / 301), the [glossary](07_Concepts/GLOSSARY.md), the topic pages (center squeeze, monotonicity, summability…), and the [voting paradoxes](07_Concepts/voting_paradoxes/README.md). |
| **[STARVote LH tabulation engine](STARVote_LH_tabulation_engine/README.md)** | The engine that counts every example here — Larry Hastings' `starvote`, vendored and forked, plus what this fork adds. |
| **[YAML library](YAML_library/README.md)** | The election-file format itself: why YAML, what every field does, the BetterVoting importer, and the deliberately-broken files that prove bad input fails politely. |
| **[Method comparisons](method_comparisons/README.md)** | The crown jewels — *same ballots, different methods*, where the contrast between them **is** the lesson. |

> **Contributors / running it locally →** start at [**CONTRIBUTING.md**](CONTRIBUTING.md) (setup + the edit-regenerate-test loop). The [**Repository & Engine Guide**](07_Concepts/about_this_repo/repository_guide.md) has the repository map, quick-start commands, how the voting methods dispatch, the validation philosophy, and what the vendored engine adds. House conventions: [CLAUDE.md](CLAUDE.md).
<!-- --8<-- [end:below-hero] -->
