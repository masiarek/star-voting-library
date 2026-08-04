# STAR Voting — Education & Test-Case Library

**Score every candidate 0–5; the two highest-scoring candidates meet in an automatic runoff; whichever finalist more voters scored higher wins.** That's **STAR Voting** — one better ballot that [quietly fixes a whole list of election problems](01_STAR/01_Learn/getting_started/STAR_benefits.md): **vote your heart, no more spoilers, a winner the majority actually likes.** And it's [refreshingly new](01_STAR/01_Learn/STAR_history.md) — first proposed in 2014, with the lessons of a century of older methods baked in.

<!-- --8<-- [start:below-hero] -->
<!-- Invisible marker: the website homepage (index.md) inlines everything from here
     to the matching [end:below-hero] marker at the bottom of this file, placing its
     own graphical hero above it. Don't delete these comment lines. -->

**New to STAR? This is your path — four short stops:**

<div class="star-path" markdown="1">

⭐ **[1 · What is STAR? — the five-minute intro](01_STAR/01_Learn/STAR_start_here.md)**<br>
Watch "pick one" ruin a team lunch, then watch STAR fix it. No background needed, not a word of politics.

🚀 **[2 · The benefits — why people switch](01_STAR/01_Learn/getting_started/STAR_benefits.md)**<br>
Vote your heart, no spoilers, majority winners, one election instead of two. The quick, exciting wins — *the proponents' pitch, and proudly so.*

🗳️ **[3 · Try it for real ↗](https://bettervoting.com/pet/vote)**<br>
Cast a STAR ballot in *What Makes the Best Pet?* — a live public election, no sign-in, seven pets, about a minute. (It's the same election this repo takes apart in [04_Real_Elections](01_STAR/04_Real_Elections/pet_real_bv_election/README.md).) Then [run your own free election ↗](https://bettervoting.com/new_election) on BetterVoting — or [print real paper ballots](01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) and count them by hand.

🤨 **[4 · Skeptical? Good.](01_STAR/01_Learn/getting_started/star_for_skeptics.md)**<br>
"What's the catch?" answered without cheerleading — including [what STAR *doesn't* fix](01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md).

</div>

**Want the whole argument, every objection answered? → [Why STAR Voting](07_Concepts/topics/Why_STAR_Voting.md).** Prefer ranked ballots? → **[Why Ranked Robin](05_Ranked_Robin/01_Learn/why_ranked_robin.md)**, the friendly upgrade that counts them so the consensus candidate wins. Ready for the full course? → [Voting 101 / 201 / 301](07_Concepts/CURRICULUM.md).

---

## What this library is

A library for learning, teaching, and debating **[STAR Voting](01_STAR/01_Learn/STAR_start_here.md)** (Score Then Automatic Runoff). It puts STAR first — and earns your trust by testing STAR honestly against every method it's compared to, with a real tabulation engine and runnable example elections behind every claim. The even-handedness *is* the argument: the STAR case is stronger because you can check it yourself.

**Looking for something specific? → [Start Here](07_Concepts/00_START_HERE.md)** routes you by what you want — learn STAR, see what's broken about voting today, compare methods even-handedly, or run the engine yourself.

Under the hood it does three things:

1. **Teaches** — concept pages and worked examples, organized by level: [Voting 101](07_Concepts/curriculum/CURRICULUM_101.md) (the basics) · [201](07_Concepts/curriculum/CURRICULUM_201.md) (reading results & comparisons) · [301](07_Concepts/curriculum/CURRICULUM_301.md) (proportional, criteria, theory).
2. **Proves** — every claim is backed by a runnable election: a single [YAML file a person reads and the engine runs](YAML_library/why_yaml_test_cases.md).
3. **Cross-verifies with BetterVoting** — import a real election from [BetterVoting](https://bettervoting.com) (the Equal Vote Coalition's free STAR platform), re-tabulate it independently, and confirm the official winner — turning real elections into regression cases that catch and guard BetterVoting's bugs (turnout undercounts, tie mislabels, abstention miscounts).

Built on a vendored fork of Larry Hastings' [`starvote`](https://github.com/larryhastings/starvote) engine.

> **Contributors / running it locally →** start at [**CONTRIBUTING.md**](CONTRIBUTING.md) (setup + the edit-regenerate-test loop). The [**Repository & Engine Guide**](07_Concepts/about_this_repo/repository_guide.md) has the repository map, quick-start commands, how the voting methods dispatch, the validation philosophy, and what the vendored engine adds. Guided tour: [Start Here](07_Concepts/00_START_HERE.md). House conventions: [CLAUDE.md](CLAUDE.md).

---

## Learn more

- [Start Here](07_Concepts/00_START_HERE.md) — guided entry point
- [Hands-on — do STAR, don't just read about it](01_STAR/01_Learn/hands_on/README.md) — [**print real paper ballots**](01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) from a BetterVoting election (live "scan to vote" QR, election id baked in), then vote, hand-count, and check it against the official tally
- [A short history of STAR Voting](01_STAR/01_Learn/STAR_history.md) — how new it is, the origin story, and the adoption timeline
- [STAR Voting — Curriculum (Voting 101 / 201 / 301)](07_Concepts/CURRICULUM.md) — levels 101 / 201 / 301
- [Glossary — voting methods & criteria](07_Concepts/GLOSSARY.md) — terms, precisely defined
- [Scored (rated) vs. ranked ballots](07_Concepts/topics/scoring-methods-vs-ranked-voting.md) — the distinction people most often conflate
- [Concepts — deep-dive pages for the important terms](07_Concepts/) — center squeeze, monotonicity, tie-breaking, STAR vs IRV…
- [Repository & Engine Guide](07_Concepts/about_this_repo/repository_guide.md) — repository map, quick-start commands, method dispatch, validation, the vendored engine
- [CONTRIBUTING.md](CONTRIBUTING.md) — setup and the contributor loop · [CLAUDE.md](CLAUDE.md) — the house conventions in full

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
<!-- --8<-- [end:below-hero] -->
