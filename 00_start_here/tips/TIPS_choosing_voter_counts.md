# Tips — Choosing the Number of Voters in STAR Examples

How many ballots should a teaching example use? It matters more than it looks, because of one collision: voter **counts** and star **scores** are both small numbers.

## The collision to avoid

It only happens in the **weighted** (`Count × scores`) form. With a small count, a row like:

```
5 × 5,4,3
```

makes the reader pause — *is that 5 voters, or a 5-star score?* That's the mental gymnastics. It does **not** happen with individual ballots (one row = one voter, no `Count` column), where every small number is unambiguously a score.

## The one rule that prevents it

- **Individual ballots** (one voter per row): any size is fine — small is great.
- **Weighted ballots** (a `Count:` column): keep **every count ≥ 6**, clear of the 0–5 ceiling. Then a count can never be mistaken for a score.

## Pick the magnitude by the lesson

| Goal | Voter count | Why |
|------|-------------|-----|
| First mechanics — one ballot, the two rounds | **1**, individual | nothing competes; no count column to confuse |
| Show ballot variety / how to vote | **3–7** individual ballots | each row is one voter; scores stay unambiguous |
| An effect you can add up by hand | **tens, counts ≥ 6** (e.g. 12/10/14, 30/25/35) | big enough to avoid the collision, small enough to verify the sums |
| A proportions / majority story | **a round total: 100** (or 18, 36, 90, 360) | percentages read straight off the counts ("61% majority") |

## The percentages-vs-arithmetic trade-off

- **100 voters** → percentages are free, but the scoring-round totals get large (e.g. `A -- 375`) and the audience can't check them in their head.
- **Tens of voters** → totals are addable live, but you have to compute the percentages yourself.
- If the lesson is *"a 61% majority got spoiled,"* favor 100 (or a clean multiple). If the lesson is *"watch the two rounds add up,"* favor tens.

## Keep the built-in disambiguators on

- The **`×` count separator** (`40 × 5,5,0`) reads as "times" — leave it on (`count_separator: "×"`).
- The **`Count:` header** labels the weight column explicitly.
- The **runoff** and **score-distribution** numbers are vote *counts*; keep the total small enough that those stay checkable if you'll narrate them.

## Automation changed one cost, not the other three

Ballots used to be typed into the BetterVoting builder by hand, so "keep it small" felt like a labor rule. It wasn't. Since `create_bv_test_election.py` casts ballots through the API, the typing cost is gone — and the three costs that actually mattered are all still there:

| Cost | Who pays | Removed by automation? |
|------|----------|------------------------|
| Entering the ballots | the author, once | **yes** |
| Holding the example in your head | every reader, forever | no |
| Hand-auditing the tally | every skeptic | no |
| A permanent, undeletable public election | BetterVoting's servers | no |

The audit cost is the important one. A reader who can recount ten ballots and confirm "b beats c, 7–3" *believes* the result; at 204–100 they can only take our word for it. Small examples are what keep a demonstration falsifiable — which is the whole point of a claim-check library. And BV elections can't be deleted, so 300 ballots for a 10-ballot lesson is a permanent footprint on someone else's public infrastructure.

**So the honest post-automation shift is toward *individual* ballots, not bigger ones.** The `Count ≥ 6` rule above exists because weighted blocs were the cheap way to get scale by hand, at the price of the count-vs-score collision. Now that the script does the casting, ten individual rows cost the same as one weighted bloc and read better. Reach for a `Count:` column when the lesson genuinely needs *proportions* — not to save keystrokes.

### Lifting a profile out of a paper

Academic social-choice papers print electorate-sized profiles (102 / 101 / 100 / 1) largely by convention; the numbers are usually decorative and shrink without loss. Check before copying: scale all blocs down and confirm the pairwise winners, the cycle (if any), and the method rankings survive. They normally do — only lessons that turn on a **ratio** (center-squeeze thresholds, proportional seat shares, "a 61% majority") actually need the voters.

> **The scaling rule has a name, and it isn't free.** Replacing every voter with `k` identical copies and expecting the same winner is the **homogeneity** axiom — `f(ks) = f(s)` — the weakest member of the [reinforcement / consistency](../../method_comparisons/reinforcement_paradox/README.md) family. Every method in this repo satisfies it, which is why "scale all blocs ×N" is a safe habit here. But it is an *axiom*, not arithmetic: any rule with an absolute voter threshold ("elect X if at least 100 people approve", a fixed quorum in raw votes rather than a fraction) is **not** homogeneous, and scaling such a profile silently changes the lesson. Worth a moment's check whenever a rule mentions a raw count. → [quorum](../topics/quorum.md), where this repo does use an absolute threshold.

When the source's exact numbers are worth preserving for reproducibility, **don't mint two BetterVoting elections.** Keep:

- the **small version on BV** — permanent, public, linked from the lesson;
- the **paper-exact version as an LH-only sibling `.yaml`** (no `<bvid>` segment, skips steps 3–4 of the workflow) — fully tabulatable, zero permanent footprint, and the page can note "the source prints this at N ballots; same winner, same structure."

A deliberate large/small **pair** earns its own page only when scale-invariance *is* the lesson — answering "would this still hold in a real election?" That's one page, not a policy.

## Rules of thumb

1. **Never put a weighted count in 1–5.** Either switch to individual ballots, or use counts ≥ 6.
2. **Match the total to the story** — round numbers for percentages, small numbers for live arithmetic.
3. **Keep the scoring-round product easy** if you want the audience to verify it (count × top score should be a number they can do in their head).
4. **Be consistent within a lesson sequence**, so the *magnitude* doesn't become an extra variable the audience has to track from one example to the next.
5. **Size for the reader and the auditor, never for the author.** Automated casting is not a licence to scale up — the ballot count still has to be locked at its smallest *before* a BV election is created, because BV elections are permanent.

## Worked feel for each style

- `01_Single_winner/00a_c2_b1_two-candidates.yaml` — **1 ballot**, individual. The gears, nothing else.
- `split_voting/01_political_left_split.yaml` — **100 voters**, weighted, counts 24/22/20/34 (all ≥ 6). Percentages are obvious; the spoiler story needs them.
- `01_Single_winner/equal_support_runoff_demo.yaml` — **100 voters** (40/35/25). Easy percentages; the trade-off is the `375` scoring total you don't ask the audience to verify.
- `split_voting/00_plurality_vs_majority.yaml` — **100 voters** (40/35/25). The textbook "proportions / majority story": the whole lesson is "40% wins the plurality but a 60% majority opposed," so the counts *are* the percentages. Large scoring totals (`Blake 275`) you read past — the point is the divergence, not the sums.

See also: [CURRICULUM.md](../CURRICULUM.md) · [GLOSSARY.md](../GLOSSARY.md).
