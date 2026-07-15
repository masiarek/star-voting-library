# Abstention vs. a zero vs. "None of the Above" — three different things

Three ballot situations look similar on a STAR score sheet but mean genuinely different things. Confusing them is behind a lot of "why is the count off?" questions, so here they are side by side.

## The three cases

**1. A zero — `0` (an active low score).** You scored the candidate the lowest possible amount. It's a real evaluation ("I do not support this candidate") and it counts as a cast, tallied score. A **bullet vote** (5 for one, 0 for everyone else) is made of zeros — the voter *participated fully*, they just rated most candidates 0.

**2. An abstention — blank / unscored.** You left the line blank. Two flavors:

- **Whole-ballot abstention** — every line blank (or, in STAR, *all lines equal*, e.g. `0,0,0` or `5,5,5`). The ballot expresses **no preference**, so it's set aside as an **abstention**: it counts as turnout but contributes nothing to any candidate's score or to the runoff. **Set aside is not discarded** — the ballot is still counted as turnout (and toward [quorum](../topics/quorum.md)); it's only kept out of the *preference* math. And that costs no one anything: an all-equal ballot rates every candidate the same, so folding it in would move every total by the identical amount and tip no scoring round and no runoff — the winner is unchanged either way. Setting it aside simply keeps the turnout count honest instead of padding everyone's score with a ballot that voiced no opinion.
- **Per-candidate abstention** — you scored some candidates and left one blank. That one blank tallies as 0 for the math, but the ballot still counts — a single unscored candidate does **not** turn the whole ballot into an abstention.

**3. None of the Above — `c-nota` (an active vote for "reject the field").** "None of the Above" is a real *candidate* on BetterVoting. Scoring it 5 is an **active preference** — a vote *for* the option "none of these should be seated." It competes like any candidate: it can reach the runoff and win (see the [BV215 case](../../01_STAR/none_of_the_above/bv215_26khr3_nota_wins.md), where it does).

## The one-line contrast

> **Abstaining / all-zeros _withdraws_ you from the decision. Scoring None-of-the-Above _participates_ in it** — you're casting a real vote, for the specific option "reject these candidates."

An all-blank ballot removes your weight from the room. A `0,0,0,…,5-for-NOTA` ballot keeps your full weight and throws it behind a "none" outcome. Same-looking scores, opposite effect.

## Side by side (a 3-candidate race)

| Ballot | Ada | Bruno | None of the Above | What it means | Effect on the count |
|---|:-:|:-:|:-:|---|---|
| Bullet / zeros | 5 | 0 | 0 | Full support for Ada, rejects the rest | Cast vote; all scores tallied |
| Whole-ballot abstention | – | – | – | No preference at all | Set aside as an abstention (turnout only) |
| Per-candidate abstention | 5 | 1 | – | Scored two, left NOTA blank | Cast vote; blank tallies as 0, ballot still counts |
| None of the Above | 0 | 0 | 5 | Actively rejects both real candidates | Cast vote; NOTA competes and can win |

(`–` = blank. In this library's YAML the whole-ballot vs per-candidate blanks use the LH markers below.)

## How each system records it

**BetterVoting** stores a score as `0`–`5`, or `null` when a candidate is left unscored — and "None of the Above" is just a candidate (`c-nota`) you score. So BV distinguishes exactly three states per candidate line: **a number, `null` (didn't score), or a NOTA score.** `null` is preserved and is *not* the same as `0` (BetterVoting reports a whole-ballot abstention only when the whole ballot is blank/equal — a single `null` doesn't count as one).

**The Larry Hastings engine** goes further: it has a small **marker vocabulary** for *why* a line is zero — all tabulate as 0, but each is recorded and reported distinctly:

| Marker | Meaning |
|:-:|---|
| `-` | blank |
| `~` | race abstention |
| `&` | candidate abstention |
| `?` | spoiled ballot |
| `%` | spoiled **and** re-issued |

See [STAR ballot voting styles](STAR_ballot_voting_styles.md) and [Ballot & Terminology Basics](../topics/ballot_and_terminology_basics.md). That the file can carry these distinct markers at all — instead of collapsing every non-vote into a bare `0` — is a direct payoff of the [one legible-*and*-runnable YAML](../about_this_repo/why_yaml_test_cases.md) design: the format stores the *intent* behind a zero, which a flat CSV of scores can't.

## The gap: BetterVoting can't capture *intent* behind a non-score

This is a real difference in expressiveness. In the LH engine a `0` (an active low score) is distinct from `-` (blank), `~` / `&` (a deliberate abstention), and `?` / `%` (spoiled) — even though they all tabulate as 0 — so reports and audits can tell **a rejection apart from a non-participation apart from a spoiled ballot.**

BetterVoting has only two of those states: a score, or `null`. It has **no explicit "abstained" or "spoiled" mark.** A voter who means *"I deliberately abstain on this candidate"* and one who simply *skipped the line* produce the identical `null`; a deliberate `0`-as-protest and a `0`-as-indifference are identical too. The voter's *intent* behind a non-score isn't captured, which limits abstention/turnout reporting and auditing.

That's a candidate **missing-feature** for BetterVoting relative to LH: an explicit abstain (and spoiled) affordance on the ballot, stored distinctly from a plain `0` or a blank — so the count can report *deliberate abstentions* and *spoiled ballots* honestly instead of folding them into zeros and nulls.

## See it in the cases

- **Abstentions in a real STAR count:** [`flat_scores_abstention_c3_b8`](../../01_STAR/pet_real_bv_election/pet_real_bv_election_pages/flat_scores_abstention_c3_b8.md) · [`small_abstention_c2_b5`](../../01_STAR/pet_real_bv_election/pet_real_bv_election_pages/small_abstention_c2_b5.md)
- **None of the Above winning (plus a per-candidate `null`):** [`bv215_26khr3_nota_wins`](../../01_STAR/none_of_the_above/bv215_26khr3_nota_wins.md)

## Related

The BetterVoting issues on this exact topic (abstain / blank / zero mislabels, export ambiguity, the `#884` "all-equal = abstain" policy, and the `#1421` NOTA case) are catalogued in [BV abstain / blank / zero — issue index](../tabulation_engines/BV/abstain_issues_index.md), cross-referenced to the test cases.

[Ballot voting styles](STAR_ballot_voting_styles.md) · ["Preference" — the word that causes half the confusion](../topics/preference.md) · [Quorum](../topics/quorum.md) · [GLOSSARY](../GLOSSARY.md) · [Curriculum](../CURRICULUM.md)
