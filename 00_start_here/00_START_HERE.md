# Start Here

This is the **STAR Voting education library** — for learning, teaching, and debating **[STAR Voting](STAR_Voting/STAR_start_here.md)** (Score Then Automatic Runoff). STAR comes first here. What makes the case for it trustworthy is that we *don't hide the ball*: STAR is tested honestly against every method it's compared to, with a real tabulation engine and runnable example elections behind every claim. The even-handedness **is** the argument — the STAR case is stronger because you can check it yourself.

**Pick your path — what brings you here?**

---

## ⭐ Learn STAR Voting

The main event.

- **New here — the "why" before the "how"** → [STAR — start here](STAR_Voting/STAR_start_here.md)
- **How the count works** → [the Scoring Round](STAR_Voting/STAR_Scoring_Round.md) + [the Automatic Runoff](STAR_Voting/STAR_Automatic_Runoff.md) (two rounds, one ballot)
- **The case for it, in brief** → [The benefits of STAR Voting](STAR_Voting/STAR_benefits.md) · debate prep → [Why STAR Voting](topics/Why_STAR_Voting.md)
- **Have a specific question?** → [STAR FAQ — mechanics, with worked examples](STAR_Voting/STAR_FAQ.md)
- **The full course** → [Curriculum — Voting 101 / 201 / 301](CURRICULUM.md)

## What's wrong with how we vote now?

The problem STAR is built to fix — start here if you're new to voting reform.

- [Choose-One / Plurality (FPTP)](topics/plurality.md) — the status quo, and why it breaks with more than two candidates
- [The spoiler effect](topics/spoiler_effect.md) — the core failure
- [Center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) — how even ranked methods can eliminate the consensus candidate
- [Two-party dominance](topics/two_party_dominance.md) — is it good or bad, and what actually changes it
- [Alaska 2022](RCV_IRV/RCV_IRV_alaska_2022.md) — a real RCV-IRV failure (spoiler + center squeeze + non-monotonicity in one race)

## Why STAR over the alternatives?

The honest comparison — where STAR's case is actually made.

- [Scores vs. ranks](scores_and_ranks/scores_vs_ranks.md) — the ballot distinction everything turns on
- [Choosing among the Equal Vote methods](topics/choosing_among_evc_methods.md) — STAR vs. Approval vs. Ranked Robin, the tradeoff triangle, even-handed
- [RCV-IRV vs. STAR](topics/rcv_irv_vs_star.md) — head-to-head with the method most people mean by "RCV"
- [Strategic voting](topics/strategic_voting.md) — the four kinds of insincere vote, and why honesty pays in STAR
- **Skeptical?** [STAR for skeptics — the honest 5-minute path](STAR_Voting/star_for_skeptics.md) — "you think this is weird, what's the catch?", answered without cheerleading
- **More than one seat?** [Electing more than one, simply](topics/electing_more_than_one.md) — majoritarian vs. proportional, in plain language

## The whole field, even-handed

The credibility layer — read the arguments *against*, too.

- [How to Learn About Voting Methods](topics/how_to_learn_about_voting_methods.md) — a method-neutral reading path, beginner → advanced (after Marcus Ogren)
- [Same ballots, different methods](../method_comparisons/README.md) — where methods disagree, worked (center squeeze, monotonicity, the divergence ledger, [paradoxes & whoops](../method_comparisons/paradoxes_and_whoops/README.md))
- **Honest limits** — every method's weaknesses, stated plainly: [STAR](STAR_Voting/STAR_honest_limits.md) · [Approval](Approval_Voting/approval_honest_limits.md) · [Ranked Robin](RCV_Ranked_Robin/RCV_RR_honest_limits.md)
- [Who champions each method](topics/advocacy_organizations.md) — FairVote, CES, the Equal Vote Coalition

## Run & verify elections (the library + engine)

The thing that makes every claim above checkable.

- [Repository & Engine Guide](about_this_repo/repository_guide.md) — how to tabulate a file, import a BetterVoting export, run the tests
- [The YAML test-case index](YAML_test_case_index/) — every example election, grouped by method · [BetterVoting-backed cases](YAML_test_case_index/BV_registry.md)
- [Why YAML?](about_this_repo/why_yaml_test_cases.md) — one file a person reads and a computer runs

## Reference

- [Glossary](GLOSSARY.md) — every term, precisely defined
- [Ballot & terminology basics](topics/ballot_and_terminology_basics.md) — the four "RCV" confusions people get wrong

**The methods, one page each:**

| Method | Ballot | Learn more |
|---|---|---|
| **STAR** | score 0–5, then automatic runoff | [STAR — start here →](STAR_Voting/STAR_start_here.md) |
| **Approval** | approve any number (0/1) | [Approval overview →](Approval_Voting/approval_voting.md) |
| **Range / Score** | grade each; highest total wins | [Range / Score overview →](Range_Voting/range_voting.md) |
| **Ranked Robin** (Condorcet) | rank; every pair head-to-head | [Ranked Robin overview →](RCV_Ranked_Robin/ranked_robin.md) |
| **RCV-IRV** | rank; instant runoff | [RCV-IRV (Hare) →](RCV_IRV/RCV-IRV-Hare.md) |
| **3-2-1** | Good / OK / Bad | [3-2-1 overview →](../06_Other/three_two_one/README.md) |

# file: 00_START_HERE.md
