# STAR Voting — Education & Test-Case Library

A library for learning, teaching, and debating **[STAR Voting](00_start_here/STAR_Voting/STAR_start_here.md)** (Score Then Automatic Runoff). It puts STAR first — and earns your trust by testing STAR honestly against every method it's compared to, with a real tabulation engine and runnable example elections behind every claim. The even-handedness *is* the argument: the STAR case is stronger because you can check it yourself.

**New here? → [Start Here](00_start_here/00_START_HERE.md)** routes you by what you want — learn STAR, see what's broken about voting today, compare methods even-handedly, or run the engine yourself.

Under the hood it does three things:

1. **Teaches** — concept pages and worked examples, organized by level: [Voting 101](00_start_here/CURRICULUM_101.md) (the basics) · [201](00_start_here/CURRICULUM_201.md) (reading results & comparisons) · [301](00_start_here/CURRICULUM_301.md) (proportional, criteria, theory).
2. **Proves** — every claim is backed by a runnable election: a single [YAML file a person reads and the engine runs](00_start_here/why_yaml_test_cases.md).
3. **Cross-verifies with BetterVoting** — import a real election from [BetterVoting](https://bettervoting.com) (the Equal Vote Coalition's free STAR platform), re-tabulate it independently, and confirm the official winner — turning real elections into regression cases that catch and guard BetterVoting's bugs (turnout undercounts, tie mislabels, abstention miscounts).

Built on a vendored fork of Larry Hastings' [`starvote`](https://github.com/larryhastings/starvote) engine.

> **Contributors / running it locally →** the [**Repository & Engine Guide**](00_start_here/repository_guide.md) has the repository map, quick-start commands, how the voting methods dispatch, the validation philosophy, and what the vendored engine adds. Guided tour: [Start Here](00_start_here/00_START_HERE.md). House conventions: [CLAUDE.md](CLAUDE.md).

---

## The YAML election file

Want to author a case? The fill-in guide is [YAML Test Case — Authoring Template](00_start_here/YAML_authoring_template.md).

The schema is **flat**: a voting method, a seat count, and a ballot grid (a header row of candidate names, then one row of 0–5 scores per voter). Hand-written files add a top-level **`expected_winners:`** list — the key the positive pytest suite discovers and checks:

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

This exact election is the repo's **canonical leading example** — it lives as a runnable file ([`bv2187_qrw6wb_ann-bob-cal.yaml`](01_STAR/_main/bv2187_qrw6wb_ann-bob-cal.yaml) · [reader page](01_STAR/_main/_main_pages/bv2187_qrw6wb_ann-bob-cal.md)), is reused verbatim across the intro docs, and runs **[live on BetterVoting ↗](https://bettervoting.com/qrw6wb/results)** (election `qrw6wb`). The registry of all reusable teaching elections (and the freeze rule that keeps them stable) is [TIPS — Canonical Elections](00_start_here/TIPS_canonical_elections.md).

The full field-by-field guide — every option, the marker table, weighted rows, and the `lot_numbers` tie-break order — is the **[YAML Test Case — Authoring Template](00_start_here/YAML_authoring_template.md)**; the tie-break ladder in depth is [STAR Tie-Breaking — The Full Chain](00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md). House style keeps examples **small** — see [Choosing the Number of Voters in STAR Examples](00_start_here/TIPS_choosing_voter_counts.md).

---

## Learn more

- [Start Here](00_start_here/00_START_HERE.md) — guided entry point
- [STAR Voting — Curriculum (Voting 101 / 201 / 301)](00_start_here/CURRICULUM.md) — levels 101 / 201 / 301
- [Glossary — voting methods & criteria](00_start_here/GLOSSARY.md) — terms, precisely defined
- [Scored (rated) vs. ranked ballots](00_start_here/scoring-methods-vs-ranked-voting.md) — the distinction people most often conflate
- [Concepts — deep-dive pages for the important terms](00_start_here/) — center squeeze, monotonicity, tie-breaking, STAR vs IRV…
- [Repository & Engine Guide](00_start_here/repository_guide.md) — repository map, quick-start commands, method dispatch, validation, the vendored engine
- [CLAUDE.md — working guidance for this repo](CLAUDE.md) — house conventions for contributing consistently
