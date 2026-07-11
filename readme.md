# STAR Voting — Education & Test-Case Library

A library that does three things:

**1. A human-readable test-case library.** Real and hand-written voting-method elections — each a single YAML file a *person* can read and the *engine* can run. → [Why YAML? One file a person reads and a computer runs](00_start_here/why_yaml_test_cases.md).

**2. Cross-verification with BetterVoting.** Import a real election from [BetterVoting](https://bettervoting.com) (the Equal Vote Coalition's free STAR platform), re-tabulate it with an independent, auditable engine, and confirm the winner matches its official tally — turning real elections into regression cases that catch and guard BetterVoting's bugs (turnout undercounts, tie mislabels, abstention miscounts).

**3. Educational material.** Concept pages and worked examples, organized by level — [Voting 101 / 201 / 301](00_start_here/CURRICULUM.md).

Built on a vendored fork of Larry Hastings' [`starvote`](https://github.com/larryhastings/starvote) engine. New here? Start with [Why YAML?](00_start_here/why_yaml_test_cases.md), then [the pipeline](00_start_here/the_pipeline.md) that wraps it.

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

Richer files — the shape the BetterVoting converter produces — add candidates with explicit IDs, human context, an optional `lot_numbers:` tie-break order, and an `expected_results:` block. Score cells may also carry **markers** (`-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all count as 0 but are preserved so reports and quorums stay honest), and rows can be **weighted** (`42 × 0,3,5`). Approval ballots accept only `0`/`1`.

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
