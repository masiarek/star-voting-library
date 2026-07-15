# Thiele methods — the one dial that turns AV into CC (and where STAR-PR fits)

*Advanced (301). AV and CC (from the [ABC-rules spectrum](abc_rules_spectrum.md)) aren't two unrelated rules — they're the two ends of **one** parameterised family, the **Thiele methods**, and **PAV** sits in the middle. The single dial is a satisfaction function `w`. This page defines the family, works the book's PAV example, and answers the question STAR learners actually ask: **do I need this to understand STAR-PR?** (Short answer: not to *use* it, but it's the clearest place to see *why* proportionality works — and RRV is the direct bridge.) All committees verified with Lackner's [`abcvoting`](https://github.com/martinlackner/abcvoting).*

Source: Lackner & Skowron, [*Multi-Winner Voting with Approval Preferences*](https://link.springer.com/book/10.1007/978-3-031-09016-5), §2.2. Prereqs: the [ABC-rules intro (101)](abc_rules_intro.md) and [spectrum (301)](abc_rules_spectrum.md).

## The one idea: satisfaction with diminishing returns

Assume a voter's happiness with a committee `W` depends only on **how many of her approved candidates got in** — call it `x = |W ∩ A(i)|`. A **Thiele method** picks a non-decreasing function `w : ℕ → ℝ` with `w(0) = 0`, scores a committee by the total satisfaction, and returns the maximiser:

```
score_w(A, W) = Σ_i  w( |W ∩ A(i)| )        →  the w-Thiele rule elects argmax_W score_w
```

Everything is in the *shape of `w`* — specifically, how fast satisfaction grows as a voter gets a 2nd, 3rd, … representative:

| Rule | `w(x)` | shape | meaning |
|------|--------|-------|---------|
| **AV** | `w(x) = x` | straight line | every extra approved winner is worth the same → maximise total approvals (**utilitarian**) |
| **PAV** | `w(x) = 1 + ½ + ⅓ + … + 1/x` (harmonic) | concave, diminishing | the 2nd winner is worth ½, the 3rd ⅓ … → **diminishing returns** → **proportional** |
| **CC** | `w(x) = min(1, x)` | flat at 1 after the first | only *whether* you have ≥1 winner matters → maximise voters covered (**egalitarian**) |

That's the whole spectrum in one picture (the book's Fig 2.2): AV's line climbs forever, CC flattens immediately at 1, and **PAV's harmonic curve lies between them**. Turning the `w` dial from "straight line" to "flat" walks you continuously from utilitarian AV to egalitarian CC.

## Why the harmonic makes PAV proportional

The harmonic weights `1, ½, ⅓, …` are the "law of diminishing returns" made precise: a voter who *already* has representation counts for less when deciding the next seat, so the rule stops piling seats onto an already-satisfied majority and starts serving the next group. That's proportionality — and it's why PAV, unlike AV, rescues a faction the majority left out.

**Worked example (the book's Ex 2.4), on our running profile.** PAV elects `W = {a,b,c,f}`. Group the 12 voters by how many of their approved candidates are in `W`:

- the `{b,c,f}` voter → **3** approved → `w(3) = 1 + ½ + ⅓ = 11/6`
- the six `{a,b}`/`{a,c}` voters → **2** each → `6 · w(2) = 6 · 3/2 = 9`
- the two `{a,d}` + one `{f}` voters → **1** each → `3 · w(1) = 3`
- the `{e}` and `{g}` voters → **0** → `0`

`score_PAV = 11/6 + 9 + 3 = 83/6`, and no other size-4 committee beats it. Note `{a,b,c,f}` is *also* one of AV's two tied committees — the one with fewer unrepresented voters. As the book puts it, **PAV strives for a compromise between AV and CC**.

## Welfarist rules (why all of this is "just" a welfare function)

Define a committee's **welfare vector** as each voter's satisfaction: `welf(W) = (|A(1)∩W|, …, |A(n)∩W|)`. A rule is **welfarist** if it maximises some function `f` of that vector. Thiele methods are welfarist with `f = Σ_i w(welf_i)` — AV sums the raw vector, CC counts its non-zero entries, PAV sums the harmonic-transformed entries. Same data, three aggregations.

## Two footnotes worth knowing

- **Sequential variants.** Optimising a Thiele score exactly is NP-hard for PAV, so in practice one goes **greedy**: **seq-PAV** adds, one seat at a time, the candidate that raises the PAV score most; **rev-seq-PAV** starts from all candidates and *removes* the least valuable. On our profile all three (PAV, seq-PAV, rev-seq-PAV) agree on `{a,b,c,f}` — but they *can* differ (Janson gives an example), and rev-seq-PAV can even do surprising things: in the book's Ex 2.6 it removes the **highest-approval** candidate first. So "PAV" names an objective; "seq-PAV" names an algorithm.
- **Beyond Thiele.** Not every proportional idea is a Thiele method — **Monroe's rule** assigns each winner a disjoint quota of voters, and **Phragmén's** rules balance "load," neither of which is a `w`-Thiele optimisation. (On our profile seq-Phragmén gives `{a,b,c,d}`, siding with the majority where PAV sides with coverage.)

## Does any of this apply to STAR-PR?

This is the question STAR learners really want answered. **Directly, no; by analogy, yes — and the analogy is exact for one rule.**

- **Different ballots.** Thiele methods are defined for **approval** ballots (`x = number of approved winners`). STAR-PR runs on **0–5 score** ballots — there's no "number approved," so the Thiele score formula doesn't apply as-is.
- **Different machinery.** STAR's **Allocated Score** (BetterVoting's `STAR_PR`) and **SSS** are **quota/reweighting** rules — a faction that helps elect a candidate has its ballots *spent* against a Droop-style quota — which is mechanically the **STV** lineage, *not* Thiele's "maximise Σ w(satisfaction)."
- **But RRV is score-PAV.** **Reweighted Range Voting** reweights each ballot by a harmonic-style divisor `1 / (1 + (score already awarded to winners)/max)` before each seat. On **0/1** ballots that divisor *is* the seq-PAV weight — which is exactly why, in the [shadow STAR](../../../04_Approval/multiwinner/lackner_skowron_shadow_star.md), **RRV recovered PAV's `{A,B,C,F}`** while Allocated/SSS stayed at `{A,B,C,D}`. RRV is the **score-ballot generalisation of sequential PAV**; the harmonic "diminishing returns" idea is the same, lifted from *counts* to *scores*.

So the honest map:

| STAR-PR rule | family | approval cousin |
|--------------|--------|-----------------|
| **RRV** | reweighted-score (Thiele-style) | **≈ seq-PAV** (a Thiele method) |
| **Allocated Score / SSS** | quota-spending (STV lineage) | ≈ Phragmén / STV, *not* Thiele |

**Do you need Thiele to learn STAR-PR?** To *operate* STAR-PR — no; it's fully defined by quotas and reweighting. But to understand **why** a proportional rule behaves as it does, the approval Thiele family is the cleanest lens: it isolates proportionality into a single knob (the `w` curve = diminishing returns), with no scores or quotas in the way. Learn AV → PAV → CC first, *then* STAR-PR reads as "the same diminishing-returns idea, but on 0–5 scores, with RRV as the closest match and Allocated/SSS taking the STV route instead." That's genuinely the fastest path in — even coming from a pure STAR direction.

## Reproduce

```bash
pip install abcvoting
python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
  04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml \
  --rules av,pav,seqpav,revseqpav,cc,seqphragmen
# pav = seqpav = revseqpav -> {A,B,C,F} ; cc -> {A,E,F,G} ; av -> {A,B,C,D}|{A,B,C,F}
```

## See also

- [ABC rules & the utilitarian–egalitarian spectrum (301)](abc_rules_spectrum.md) · [gentle intro (101)](abc_rules_intro.md).
- [Shadow STAR of the same profile](../../../04_Approval/multiwinner/lackner_skowron_shadow_star.md) — where RRV = PAV shows up concretely.
- [Proportional STAR (STAR-PR) methods](../../proportional_representation/) — Allocated Score, SSS, RRV, and the STV comparison.
- Glossary: [Thiele method, PAV, Chamberlin–Courant, welfare vector](../../GLOSSARY.md).
