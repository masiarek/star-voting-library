# Tips — Terminology: RCV vs IRV vs RCV-IRV (and friends)

Which word to use when. The whole thing untangles once you separate **the ballot** from **the tabulation** — the same distinction that matters everywhere else in STAR.

## The one idea that fixes it

> **RCV names a BALLOT. IRV names a TABULATION.**

- **RCV (Ranked-Choice Voting)** = a *ballot type*: the voter ranks candidates (1st, 2nd, 3rd…). It's a **family**, not a single method.
- **IRV (Instant-Runoff Voting)** = *one way to count* a ranked ballot: eliminate the lowest, transfer, repeat. The single-winner method people usually mean.
- The **same ranked ballot** can be counted other ways:
  - **Ranked Robin** — a Condorcet / "consensus" tabulation (most head-to-head wins). Sometimes written **RCV-RR** or "Consensus Voting."
  - **STV (Single Transferable Vote)** — the *proportional, multi-winner* tabulation.

So when someone says "RCV," they've named the *ballot* but implied a *count*. In the US, "RCV" has been hijacked to mean **IRV specifically** — that's the abuse.

## The ranked-method family tree

The ranked ballot ("RCV") is counted by a whole family of *methods*, which split into two branches. Knowing which is which keeps you precise — and keeps you from lumping a Condorcet method in with IRV.

```mermaid
flowchart LR
    %% LR, not TD: the 9 leaves stack vertically, keeping the diagram ~3 node-columns
    %% wide — a TD layout is ~2000px wide and gets shrunk to unreadable on the site.
    R["<b>RANKED ballot</b><br/>('RCV' names the BALLOT,<br/>not any one method)"]
    R --> COND["<b>Condorcet</b> / round-robin / pairwise<br/><i>elects the head-to-head winner<br/>when one exists · precinct-summable</i>"]
    R --> ELIM["<b>Sequential elimination</b><br/><i>eliminate &amp; transfer ·<br/>order-dependent · NOT summable</i>"]
    R --> POS["<b>Positional</b><br/><i>points by rank position</i>"]

    COND --> RR["<b>Ranked Robin</b> (RCV-RR)<br/>aka 'Consensus Voting'<br/>= Copeland + margin tiebreak"]
    COND --> RP["Ranked Pairs · aka Tideman"]
    COND --> SZ["Schulze · aka Beatpath"]
    COND --> MM["Minimax · aka Simpson–Kramer"]

    ELIM --> IRV["<b>RCV-IRV</b> (single-winner)<br/>aka IRV · Hare · Alternative Vote ·<br/>'instant runoff' — and 'RCV' in US usage"]
    ELIM --> STV["STV (multi-winner, proportional)"]
    ELIM --> CB["Coombs"]

    POS --> BO["Borda count"]
    POS --> BU["Bucklin · aka Grand Junction"]
```

*(**Copeland** is the algorithm under Ranked Robin, so it's folded into that node. A Condorcet **cousin**: "**Consensus Choice**" — Better Choices for Democracy's variant, same family but a different cycle-resolution rule. Plain-text version of this tree is in the `git log` if a viewer can't render Mermaid.)*

True statements that follow (and good ways to test your own precision):
- "Ranked Robin, Ranked Pairs, Schulze, and Minimax are forms of **Condorcet** RCV." ✅
- "Condorcet [methods], Borda, Bucklin, and RCV-IRV are forms of **RCV**." ✅ (All ranked ballots — though *Condorcet* is a family, the others are specific methods, so they sit at slightly different levels.)
- "Borda / Bucklin are Condorcet methods." ❌ — ranked, yes; Condorcet, no.

Spelling/naming watch: it's **Bucklin** (not "Buckling"); **Hare ≈ IRV** for single-winner, but "Hare" strictly usually means **STV** / the Hare quota.

## Aliases — same thing, different name

The single biggest source of confusion is that one method has many names. This table maps what you'll *hear* to what it *is*:

| You'll hear… | What it actually is | Precise name here |
|---|---|---|
| "RCV" (US / FairVote usage) | the eliminate-and-transfer single-winner method | **RCV-IRV** |
| "Instant runoff", "Alternative Vote", "Hare" (single-winner) | the same eliminate-and-transfer method | **RCV-IRV** |
| "Round-robin voting", "pairwise voting", "Condorcet" (used as *a* method) | the *family* that elects the head-to-head winner | **Condorcet methods** (a family, not one method) |
| "Ranked Robin", "RCV-RR", "Consensus Voting" | Equal Vote's Copeland-plus-margin-tiebreak | **Ranked Robin** |
| "Consensus Choice" | Better Choices for Democracy's Condorcet variant (different cycle rule) | a **Condorcet cousin** — *not* identical to Ranked Robin |
| "Copeland" | the win-minus-loss algorithm underneath Ranked Robin | **Copeland** |
| "Beatpath" → Schulze · "Tideman" → Ranked Pairs · "Grand Junction" → Bucklin | older / academic names | as named |

Rule of thumb: when you mean the **family**, say "Condorcet" or "round-robin"; when you mean the **specific Equal-Vote method**, say "Ranked Robin." Reserve bare "**RCV**" for the *ballot*.

## Why the precision actually matters

Several of the strongest criticisms are **IRV-specific, not ranked-ballot-wide**:

- **Center squeeze**, **exhausted ballots**, **non-monotonicity** → these are failures of **IRV's elimination tabulation**.
- **Ranked Robin** (Condorcet) uses the *same ranked ballot* and does **not** have center squeeze.

So if you say *"RCV has center squeeze,"* a sharp opponent can correctly reply *"Ranked Robin is RCV and doesn't."* If you say *"IRV has center squeeze,"* you're exactly right. Precision protects your credibility — and it's the same reason you insist STAR critics distinguish "the ballot" from "the runoff."

## When to use which word

| Situation | Use | Why |
|-----------|-----|-----|
| US public audience, naming the thing they know | **[RCV-IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md)** (or "IRV — what's usually called RCV") | familiar *and* precise; signals you mean the eliminate-and-transfer method, not the ballot family |
| Technical / comparison / criticism of the method | **[IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md)** | the exact, defensible name; criticisms like center squeeze are IRV's, not all ranked ballots' |
| Naming the elimination *rule* itself | **[Hare](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md)** (fewest-first-choices elimination; single-winner = IRV) | precise for the rule — but note "Hare" *also* names the STV quota, so single-winner "Hare" ≈ IRV |
| Talking about the *ballot* / the ranked family | **[ranked ballots](../scores_and_ranks/strict_vs_weak_ranks.md)** / **[ranked methods](../../06_Other/RCV_IRV/concepts/RCV-IRV-confusing-name.md)** / **RCV ballot** | reserve bare "RCV" for the ballot, and say so |
| A Condorcet count of a ranked ballot | **[Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md)** (RCV-RR / "consensus") | a different RCV tabulation; do NOT lump it with IRV |
| Proportional multi-winner ranked | **[STV](../../03_STAR_PR/concepts/stv/proportional_stv_vs_star.md)** | the proportional RCV tabulation |

## House style for this repo

1. **Default to `RCV-IRV`** in STAR-vs-method comparisons (the engine's `[Divergence from STAR]` block and the conversation scripts already do this). It's unambiguous to a US reader and makes clear you mean the method.
2. **Use `IRV`** in tight technical passages where you've already established you're talking about the eliminate-and-transfer count.
3. **Reserve bare `RCV`** for "the ranked-ballot family," and when you use it that way, make it explicit (e.g. "RCV ballots can be counted as IRV, Ranked Robin, or STV").
4. **Name `Ranked Robin` and `STV` explicitly** — never fold them into "RCV" meaning IRV.
5. When quoting how others (mis)use "RCV," keep their word but add the correction once.

## The mirror image — STAR's own ballot vs tabulation

The same split applies to STAR, which is why this framing is so useful:

- **The ballot:** a 0–5 **score** ballot (cardinal).
- **The tabulation:** **Score Then Automatic Runoff.**
- The same score ballot can also be counted as **Approval** (threshold), **Score** (pure total), or **Proportional STAR** (multi-winner). "STAR" is one tabulation of a score ballot, just as "IRV" is one tabulation of a ranked ballot.

Teaching tip: once your audience holds "ballot vs tabulation," the whole nomenclature snaps into place — and so does why "RCV" alone is ambiguous.

## One level up — "preference profile" and its silent default

Theory papers draw an election as a **preference profile**: one column of preferences per voter (≻₁, ≻₂, …). The term is correct — but unqualified it carries a **silent default**: **strict, complete rankings** (linear orders — no ties, no truncation, order only). The default is inherited, not argued: in the Arrow tradition, "preference" is a *technical* term for a complete, transitive relation — which just *is* a ranking — so social-choice writing uses "preference" and "ranking" interchangeably. Nothing about voters' actual opinions requires that (the economists' baseline preference relation happily allows indifference); it's the same capture as "RCV" collapsing to IRV — a family word swallowed by its most-studied member. It even shares the etymology: IRV's traditional name is **"preferential voting,"** which is how *preference* came to mean *rank* in everyday usage.

So keep **three layers** apart: the voter's **opinion** (in their head), the **ballot** the method lets them file (the *method's* constraint, not the voter's), and the technical **"preference"** (a ranking, by Arrow-era definition). A ballot of any type is a constrained *report* of the opinion — never the opinion itself. This care has top-tier precedent: the Stanford Encyclopedia's [Voting Methods entry](https://plato.stanford.edu/entries/voting-methods/) deliberately says *ranking* rather than *preference* where only order is meant, precisely because the technical word misleads.

House style, mirroring the RCV rules above:

1. **Citing or quoting a paper → keep its "preference profile,"** with a one-time gloss — e.g. *"every voter's ranking (a 'preference profile' — here, strict rankings)."* The [Alaska 201 page](../../method_comparisons/alaska_2022/alaska_201.md) does exactly this.
2. **When the ballot type matters, name what the profile carries:** a **ranked profile** — [strict](../scores_and_ranks/strict_ranks.md) or [with ties](../scores_and_ranks/weak_ranks.md) (weak orders) — a **score profile** (0–5; theory akas *utility* / *grade* profile), an **approval profile** (0/1).
3. **Three axes, not one:** *strict vs weak* (are ties allowed?), *complete vs truncated* (is everyone ranked?), and *ordinal vs cardinal* (is strength carried?). The first two are literally [PrefLib's](https://www.preflib.org/format) file extensions — **SOC / SOI / TOC / TOI** = {Strict, Ties} × {Complete, Incomplete}; the Burlington 2009 ballots in this repo come from its TOI files — and cardinal data fits none of the four, which is the third axis showing up as a format boundary. The theory default sits at (strict, complete, ordinal) — it simultaneously **demands** resolution voters may not have (ties must be broken) and **discards** information they do have (intensity). A score profile allows the ties and carries the strength.
4. **Don't cede "preference" to ranked ballots.** A score ballot also reports preferences — a weak order *plus* strength ("rank your preferences" is marketing, not a definition). STAR's **Equal Support** voters are precisely the ones whose preference between two finalists is a genuine tie: expressible on a score ballot, [rejected by most strict-rank IRV rules](../scores_and_ranks/strict_vs_weak_ranks.md).

The distinction is even load-bearing in this repo's tooling: our `pref_voting` cross-check loads linear orders as `Profile` but must switch to `ProfileWithTies` the moment ballots tie or truncate.

And the ladder extends in both directions. *Below* the strict ranking sits the theory's **"order zoo"** — total → top-truncated → weak → partial orders ([arXiv:1907.00752](https://arxiv.org/abs/1907.00752), Fig. 1) — cataloguing how much less than a complete strict ranking a real preference can be (their split of *why* is useful too: **intrinsic** incompleteness = the voter doesn't have a full ranking, vs **epistemic** = they have one but it wasn't captured). *Above* the score ballot sits electowiki's [rated pairwise preference ballot](https://electowiki.org/wiki/Rated_pairwise_preference_ballot) — a strength for every head-to-head matchup, generalizing every common ballot type (so expressive a single voter can submit their own Condorcet cycle, i.e. it stops being an "order" at all). Every ballot design is a choice of rung on this ladder — and "preference profile," unqualified, silently names just one of them.

See also: [GLOSSARY.md](../GLOSSARY.md) (precise definitions) · [CURRICULUM.md](../CURRICULUM.md) · the nomenclature episode ["Is It RCV or IRV? Why Do You Keep Saying RCV-IRV?"](../../06_Other/RCV_IRV/concepts/RCV_or_IRV_whats_the_right_word.md).
