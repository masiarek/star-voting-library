# Claim check — FairVote's "Why the Condorcet Criterion Is Less Important Than It Seems"

*A worked example of reading advocacy literature critically. FairVote's article ([fairvote.org, Alec Slatky, August 10, 2010](https://fairvote.org/why-the-condorcet-criterion-is-less-important-than-it-seems/)) argues that the [Condorcet criterion](README.md) matters less than voting theorists claim. The article contains one genuinely good point — and several claims that are checkably false. This page quotes each claim verbatim, checks it, and tabulates the article's own hypothetical with the LH engine. The errors are FairVote's, not "RCV's" — this is about one article's reasoning, not a verdict on ranked ballots.*

**Why this page exists.** Comparison and criteria pages are usually written by [advocacy organizations](../advocacy_organizations.md), and each leans toward the method it champions — that cuts in every direction, including pro-STAR pages (see the sources note in [RCV-IRV vs STAR](../rcv_irv_vs_star.md)). The skill being taught here is not "FairVote is wrong"; it's *how to check a voting-method claim against a countable election*. Every check below is a small YAML you can re-run.

## First, the honest framing: is the Condorcet winner the "best" choice?

**No single ideal of a "best" winner exists — that's a theorem, not an opinion.** The Condorcet winner (the *consensus candidate* — beats every rival head-to-head) is one of several defensible ideals, alongside the majority winner, the plurality leader, and the utilitarian (highest-total-support) winner. They usually agree; when they don't, *that disagreement is the whole subject*. The full treatment is [What makes a "good" winner?](../what_makes_a_good_winner.md) — read that first if this vocabulary is new.

So an article arguing "Condorcet isn't everything" *could* be making a legitimate point — the utilitarian critique of pure majoritarianism is real, and this repo makes it too ([STAR's honest limits](../../STAR_Voting/STAR_honest_limits.md) runs the same candor in the other direction). The problem with *this* article is that its load-bearing claims are definitionally false, and the method it defends fails the criterion in exactly the scenario it constructs.

## The claims, checked

### Claim 1 — "Agreeing that the Condorcet criterion is desirable is equivalent to saying that moderate candidates should always win."

**False, and it's the foundation of the piece.** The criterion says only: *when* a candidate is majority-preferred to every alternative, elect them. Who that candidate is depends entirely on the electorate. A candidate ranked first by an outright majority is *automatically* the Condorcet winner — so every landslide winner in history (a Reagan '84, an FDR '36) satisfies the criterion trivially, moderate or not. The criterion is compatible with electing transformative, off-center candidates whenever a majority actually prefers them.

**The countable check:** [same three candidates, electorate shifts left](../../../method_comparisons/fairvote_condorcet_claims/fairvote_condorcet_claims_pages/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.md) — the "strong liberal" pole candidate takes 56% of first choices and *is* the Condorcet winner (56–44 over the moderate, 62–38 over the conservative). Every method agrees. Live on BetterVoting as BV2169: **[results ↗](https://bettervoting.com/2jrfpg/results)**.

```
--- Runoff (Preference) Matrix ---
Legend: For - Equal Support - Against
                     |    * Liberal     |   * Moderate    |   Conservative  |
-----------------------------------------------------------------------------
         * Liberal > |       ---        |  56 -  0 - 44   |  62 -  0 - 38   |
        * Moderate > |   44 -  0 - 56   |      ---        |  68 -  0 - 32   |
      Conservative > |   38 -  0 - 62   |  32 -  0 - 68   |      ---        |

[Condorcet Winner]
  Condorcet Winner: Liberal — matches the STAR winner
```

### Claim 2 — "Condorcet winners are centrist by nature, regardless of the preferences of the electorate."

**Self-contradictory as written.** The Condorcet winner is *defined by* the preferences of the electorate — there is nothing else in the definition. The defensible version of this claim is the median voter theorem: under single-peaked preferences on one dimension, the Condorcet winner sits at the *median voter's* position. But the median moves with the electorate — if the electorate shifts left, so does the Condorcet winner (the demo above). "Centrist relative to the actual distribution of voters" is not "centrist in absolute political terms," and "regardless of preferences" is exactly backwards.

### Claim 3 — "…the impossibility of victory under Condorcet methods" (for the 80–90% who "lean clearly to one side")

Verbatim: *"Wouldn't the 80% to 90% of voters who lean clearly to one side prefer that their candidate have a nonzero chance of winning, as opposed to the impossibility of victory under Condorcet methods?"*

**False.** Non-moderate candidates win under Condorcet methods whenever a majority prefers them pairwise — which happens routinely whenever the electorate leans their way (again, the shifted-electorate demo). The rhetorical move also conflates *first-choice counts* with *majority preference*: in the article's own scenario a 55-voter majority prefers the moderate to the liberal, and a 57-voter majority prefers the moderate to the conservative. Those majorities — not the moderate's 12% first-choice base — are who elects the moderate. That's [claim 6](#claim-6--the-401540-hypothetical-proves-the-opposite-of-what-its-cited-for), counted.

**The mechanism, in a symmetric textbook case:** [the symmetric 47/47/3/3 centrist](../../../method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_symmetric_centrist.md) isolates exactly what's at stake. A centrist (Casey) whom a majority prefers to each pole (53–47) but who holds only 6 first choices, counted **four ways**: the method that elects the Condorcet winner *by construction* — **Ranked Robin** — and STAR (by strength of support) both elect Casey; RCV-IRV and Choose-One eliminate the compromise on first choices and then, because the two poles are a mirror image, deadlock in an exact tie that BetterVoting breaks at random. It is not that the poles face "the impossibility of victory" — it is that the *compromise* faces it under the first-choice methods. Live as BV2170: **[results ↗](https://bettervoting.com/pp2q4q/results)**.

### Claim 4 — "choosing the centrist candidate every time is just falling into the fallacy of the middle ground"

**Category error.** The middle-ground fallacy (*argumentum ad temperantiam*) is about the truth of *propositions*: "the truth must lie between two opposing claims" is fallacious reasoning about facts. Electing the candidate whom a majority prefers over each alternative isn't an assumption that the middle is *correct* — it's an aggregation of actual expressed preferences. If a majority genuinely prefers the compromise candidate to each rival, electing that candidate isn't a fallacy; it's counting.

### Claim 5 — the football analogy points the wrong way

Verbatim: *"If the New Orleans Saints win every single football game on their schedule, they're considered the best team, and the same standard should apply to elections. Indeed, if elections were held like football playoffs, then a Condorcet candidate would always win."* — followed by the objection that *"in football, each game is inherently a one-on-one contest – not the case with elections."*

A minor structural slip: an undefeated *schedule* is a round-robin argument (every matchup played — exactly what a [pairwise matrix](README.md) computes from ranked or scored ballots), while *playoffs* are single-elimination. The analogy actually supports the criterion better than the article wants: the whole point of collecting full rankings or scores is that every "game" (pairwise matchup) *is* counted, from one ballot. The article also asserts *"quite often a Condorcet winner might actually never have a chance to be win a one-on-one race against other candidates"* — read literally, that's incoherent (winning every one-on-one race is the *definition* of a Condorcet winner); the sentence's own explanation ("lacks enough support to keep other candidates from running") is a point about candidate entry and campaign viability, not about the criterion.

### Claim 6 — the 40/15/40 hypothetical proves the opposite of what it's cited for

The article's scenario: *"a strong liberal who commands between 40% to 50% of the vote, a moderate with about 10% to 15%, and a strong conservative between 40% and 50%."* We tabulated exactly that — Liberal 45, Moderate 12, Conservative 43, poles ranking the moderate second: [FairVote's own hypothetical, counted](../../../method_comparisons/fairvote_condorcet_claims/fairvote_condorcet_claims_pages/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md). It's also **live on BetterVoting as BV2168** — the same 100 voters, a STAR race *and* an RCV-IRV race: **[results ↗](https://bettervoting.com/6w2gq7/results)**.

```
--- Runoff (Preference) Matrix ---
Legend: For - Equal Support - Against
                     |    * Liberal     |   * Moderate    |   Conservative  |
-----------------------------------------------------------------------------
         * Liberal > |       ---        |  45 -  0 - 55   |  51 -  0 - 49   |
        * Moderate > |   55 -  0 - 45   |      ---        |  57 -  0 - 43   |
      Conservative > |   49 -  0 - 51   |  43 -  0 - 57   |      ---        |

[Condorcet Winner]
  Condorcet Winner: Moderate — matches the STAR winner

[Divergence from STAR]
  STAR                   = Moderate
  Choose-One (Plurality) = Liberal   (differs from STAR)
  RCV-IRV                = Liberal   (differs from STAR)
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
```

Two things the article doesn't mention:

1. **The moderate is elected by majorities, not by the 12%.** 55 of 100 voters prefer Moderate over Liberal; 57 of 100 prefer Moderate over Conservative. "The moderate with 10–15%" wins *because most voters said so, twice.*
2. **The method the article defends eliminates that moderate.** RCV-IRV drops the Moderate in round one — fewest first choices — and elects the Liberal. This is [center squeeze](../center_squeeze/), and it is precisely the scenario where RCV-IRV *fails* the Condorcet criterion:

```
ROUND 1
Candidate       Votes  Status
------------  -------  --------
Liberal            45  Hopeful
Conservative       43  Hopeful
Moderate           12  Rejected      ← the Condorcet winner, eliminated first

FINAL RESULT
Liberal            51  Elected
Conservative       49  Rejected
```

This isn't hypothetical-only: Burlington 2009 and Alaska's August 2022 special election are the standard real cases of RCV-IRV eliminating the Condorcet winner — both worked through in [What makes a "good" winner?](../what_makes_a_good_winner.md) An article defending RCV-IRV by attacking the Condorcet criterion is, structurally, an argument that the scenario where its method misfires shouldn't count against it.

### Claim 7 — the Lieberman example is speculation stated as fact

Verbatim: *"Joe Lieberman won a near-majority in 2006 in his re-election for U.S. Senator after losing the Democratic Party primary, and would have cruised under IRV."* Plausible — he won ~50% in a three-way race and likely picks up transfers — but "would have cruised" asserts unexpressed lower preferences that were never collected. It's a reasonable guess presented with the confidence of a count. (Compare the honest hedge required in the Burlington case: with only rankings, we *can't tell* how strongly Republican voters preferred the Democrat over the Progressive.)

### Claim 8 — the one legitimate point: "hated the least" ≠ "liked the most"

Verbatim: *"Just because a candidate is hated the least doesn't mean he or she is liked the most."* **This is true, and it's a real critique.** The Condorcet criterion is purely *ordinal* — it reads only preference *order* and is blind to preference *intensity*. A lukewarm consensus candidate can beat everyone pairwise while being nobody's genuine favorite. Our tabulation makes the point visible: the poles score the Moderate only 2 of 5, so the Liberal actually *tops the score sum, 237 to 236* — the utilitarian and the Condorcet ideals split on this very election.

```
Scoring Round
   Liberal       -- 237 -- First place   ← "liked the most" (score sum)
   Moderate      -- 236 -- Second place
   Conservative  -- 227

Automatic Runoff Round
   Moderate      -- 55 -- First place    ← "majority's pairwise choice"
   Liberal       -- 45
```

But notice what this argument is: it's the **cardinal** (score-ballot) critique of ordinal methods — the case for methods that measure *level of support*, not just order (see [scoring methods vs ranked](../scoring-methods-vs-ranked-voting.md)). It is **not** an argument for RCV-IRV, which is exactly as ordinal and intensity-blind as any Condorcet method — while *also* failing the Condorcet criterion in the center-squeeze case above. The article's best point argues against its own conclusion.

## Net assessment

The article's honest core — "majority-pairwise preference isn't the only defensible standard, because it ignores intensity" — is true, and this repo agrees with it ([the majoritarian/utilitarian split](../what_makes_a_good_winner.md)). But the core is wrapped in a definitional error (Condorcet ≠ "moderates always win"), a false claim ("impossibility of victory" for non-moderates), a fallacy mislabel, and a hypothetical that — when actually counted — shows majorities electing the moderate and the article's own method squeezing them out. Read advocacy literature, from every camp, with the ballots in hand.

## The demo elections — live on BetterVoting

All three are **live BetterVoting elections** (BV2168 / BV2169 / BV2170) on the same 100-voter, three-candidate frame, so every number below is independently checkable on a public site, not just in this repo's engine. BV2168 and BV2169 each run two races (STAR + RCV-IRV); BV2170 runs four (STAR, RCV-IRV, Ranked Robin, Choose-One). BetterVoting's frozen results (the `*_bv_export.json` beside each yaml) **agree with the LH tabulation** on every deterministic race — including the round-one elimination of the Moderate in BV2168's IRV race and Casey's Condorcet win under STAR and Ranked Robin in BV2170. (BV2170's RCV-IRV and Choose-One races end in an exact pole tie that BetterVoting breaks at random — a coin flip, not a freezable result.)

| Page (start here) | What it shows | Live results | Source | Full report |
|---|---|---|---|---|
| [BV2168 — FairVote's own hypothetical](../../../method_comparisons/fairvote_condorcet_claims/fairvote_condorcet_claims_pages/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md) | Moderate = Condorcet winner by 55- and 57-voter majorities; the live RCV-IRV race eliminates them (center squeeze); score sum says Liberal — the intensity nuance, honestly | **[results ↗](https://bettervoting.com/6w2gq7/results)** | [yaml](../../../method_comparisons/fairvote_condorcet_claims/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml) | [tabulated](../../../method_comparisons/fairvote_condorcet_claims/fairvote_condorcet_claims_tabulated/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw_tabulated.txt) |
| [BV2169 — electorate shifts left](../../../method_comparisons/fairvote_condorcet_claims/fairvote_condorcet_claims_pages/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.md) | The "strong liberal" pole candidate is the Condorcet winner — the criterion follows the electorate, it doesn't pin the center | **[results ↗](https://bettervoting.com/2jrfpg/results)** | [yaml](../../../method_comparisons/fairvote_condorcet_claims/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.yaml) | [tabulated](../../../method_comparisons/fairvote_condorcet_claims/fairvote_condorcet_claims_tabulated/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw_tabulated.txt) |
| [BV2170 — the symmetric centrist, four ways](../../../method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_symmetric_centrist.md) | The pure center-squeeze mechanism: centrist Casey is the Condorcet winner (53–47 each) with only 6 first choices. STAR & **Ranked Robin** (the Condorcet method) elect Casey; RCV-IRV & Choose-One squeeze them out and deadlock the poles at random. The only four-method demo here | **[results ↗](https://bettervoting.com/pp2q4q/results)** | [yaml](../../../method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_star.yaml) | [tabulated](../../../method_comparisons/symmetric_centrist_bv2170/symmetric_centrist_bv2170_tabulated/bv2170_pp2q4q_star_tabulated.txt) |

Related: [Condorcet topic hub](README.md) · [Edelman's "Myth of the Condorcet Winner" — the steelman version of this argument, tabulated](edelman_condorcet_myth.md) · [Center squeeze](../center_squeeze/) · [What makes a "good" winner?](../what_makes_a_good_winner.md) · [Advocacy organizations](../advocacy_organizations.md) · [RCV-IRV vs STAR](../rcv_irv_vs_star.md) · [STAR's honest limits](../../STAR_Voting/STAR_honest_limits.md)

# file: fairvote_condorcet_claim_check.md
