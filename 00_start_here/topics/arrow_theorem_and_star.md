# Does Arrow's Impossibility Theorem apply to STAR? — ranked vs. rated

*A recurring debate move: "Arrow proved no voting method can be fair, so STAR can't escape it either." The precise answer is more interesting than the slogan. **Arrow's theorem is about *ranked* (ordinal) methods — and cardinal methods like STAR, Score, and Approval genuinely fall outside its scope.** But escaping Arrow is not escaping *all* impossibility: cardinal methods still run into Gibbard's manipulability theorem. This page draws that line honestly — the real pro-STAR point, and its real bound.*

→ Related: [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) · [what makes a voting method good](what_makes_a_voting_method_good.md) · [strategic voting](strategic_voting.md) · [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).

---

## What Arrow actually says

Kenneth Arrow's Impossibility Theorem (1951) is a statement about aggregating individual **rankings** into a social **ranking**. For three or more candidates, no such *ranked* rule can satisfy all of a short list of reasonable-sounding conditions at once:

- **Unanimity (Pareto)** — if every voter ranks A over B, the result does too.
- **Independence of Irrelevant Alternatives (IIA)** — whether A finishes above B shouldn't flip because of some third candidate C. (Violating this is exactly the [spoiler effect](spoiler_effect.md).)
- **Non-dictatorship** — no single voter's ranking simply *is* the outcome.
- …over an unrestricted domain of possible rankings.

The load-bearing word is **rankings**. Arrow's theorem is a theorem about *ordinal* input — ballots that carry only order, never degree. (That [ordinal-vs-cardinal line](../scores_and_ranks/scores_vs_ranks.md) is the whole hinge of this page.)

## Why cardinal methods fall outside it

Score, Approval, and STAR use **rated** ballots: you say *how much* you support each candidate (0–5), not merely an order. That extra information puts them **outside Arrow's assumptions** — the theorem doesn't range over cardinal aggregation at all. So the blanket "Arrow proved every method is unfair" is imprecise: Arrow proved it for **ranked** methods.

This isn't a fringe reading. Arrow himself, late in life, favored score-style methods and acknowledged his theorem was built for the ordinal information economists assumed voters could give — rated ballots give more (a 2012 Center for Election Science interview). As **AcanthisittaIcy130** put it crisply in the r/EndFPTP thread that prompted this page: *"Arrow's theorem applies to all ranked methods but not rated methods, i.e. methods with score or approval ballots."* That's correct.

## The honest bound — escaping Arrow ≠ escaping impossibility

Here is where cardinal advocates sometimes overreach, and where staying precise keeps the point winning. Escaping Arrow does **not** make STAR strategy-proof or paradox-free:

- **Gibbard's theorem still applies.** Gibbard (1973), extended by Gibbard (1978) to cardinal and game-form methods, proves that *every* non-dictatorial deterministic method with 3+ outcomes is **manipulable** — some situation always exists where a voter gains by voting insincerely. STAR is no exception ([strategic voting](strategic_voting.md); the worked [5-1-0 challenge](../../method_comparisons/star_5_1_0_challenge/)). So "STAR escapes **Arrow**" is true; "STAR escapes **every** impossibility theorem" is not. The one it doesn't escape is Gibbard.
- **IIA isn't free either.** The pure score *sum* is IIA-clean — adding a hopeless candidate doesn't change anyone else's total (unless voters renormalize). But STAR's *runoff* is IIA-sensitive inside a [Condorcet cycle](../RCV_Ranked_Robin/cycle_resolution.md): a candidate who can't win can still change *which two* reach the runoff, and flip the result — worked, on sincere ballots, in [the cycle spoiler (BV2212)](../../01_STAR/iia_cycle_spoiler/).
- **Strategic normalization pulls cardinal back toward ordinal.** If voters min/max (bullet-vote all 0s and 5s), a rated ballot collapses into an essentially ordinal one — and some Arrow-flavored tensions creep back in. The clean escape assumes reasonably sincere scoring.
- **Interpersonal comparison.** Summing scores across voters leans on comparing one person's "5" to another's — a genuine philosophical wrinkle Arrow's ordinal framework deliberately sidestepped. It's a feature (it lets intensity count) with a cost worth naming.

## The fair takeaway

**Does Arrow apply to STAR? No — not the theorem itself.** STAR's rated ballot puts it outside Arrow's ordinal framework, and that's a real advantage of expressiveness, not a rhetorical trick. But it's a **bounded** advantage: STAR still faces Gibbard's manipulability, its runoff isn't perfectly IIA in cycles, and the escape is cleanest under sincere scoring.

The honest one-liner: **STAR escapes Arrow, not Gibbard** — richer ballots dodge the *ordinal* impossibility, but no method dodges strategy entirely. Say the first half proudly; keep the second half attached, and the claim stays unassailable.

## Sources

- Kenneth J. Arrow, *Social Choice and Individual Values* (1951) — the theorem (see the [book note](../books/social_choice_theory.md)).
- Allan Gibbard, "Manipulation of voting schemes" (1973) and "Straightforwardness of game forms with lotteries as outcomes" (1978) — manipulability, including cardinal methods. See [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md).
- Arrow's 2012 interview with the Center for Election Science on score/range voting.
