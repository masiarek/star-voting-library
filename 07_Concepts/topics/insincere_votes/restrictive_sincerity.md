# Restrictive sincerity — bullet voting, truncation, down-voting

**Level: 201 · for voters**

*One of [the four kinds of insincere vote](README.md). Restrictive sincerity is the **downward** erasure: you keep your favorite where they belong and push everyone else lower than you honestly rate them — usually all the way to zero, or off the ballot entirely.*

You have probably done it. It's the most common insincere vote in the world, and it rarely feels like strategy:

- **Bullet voting** — score or approve only your favorite, everyone else 0.
- **Truncation** — on a ranked ballot, rank one or two and stop.
- **Down-voting** — the milder version: your honest 3 becomes a 1, so the rival gets "less oxygen."

All three say the same false thing: *"I am indifferent among everyone who isn't my favorite."* You aren't. You'd much rather have your friendly second choice than the candidate you can't stand, and a restricted ballot hides exactly that.

## Why voters do it — the fear is real, so start by conceding it

The reasoning is sound as far as it goes: **scoring your second choice supports them, and they might beat your favorite with it.** That's not paranoia — it's a named criterion failure. STAR, Approval, Score, and Ranked Robin all fail **later-no-harm**: a mark you make lower down *can* cost your favorite the win. (RCV-IRV is the method that keeps later-no-harm, and it pays for that by [not reading your lower ranks at all](../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md) until your higher ones are gone — the same property from the other side.)

So the honest question isn't "could scoring my second choice ever hurt?" It's **"which risk is bigger — my second choice beating my favorite, or my last choice beating both?"** For almost every voter in almost every race, the second risk is much bigger, and restrictive sincerity is aimed at the smaller one.

## What it costs, worked: four fans bullet-vote and elect the candidate they scored 0

A club books a speaker. Ari's four fans genuinely like Bree too — honest ballot **Ari 5, Bree 3, Cash 0**. The night before, one of them argues: *scoring Bree helps Ari's rival — zero her, and Ari walks in.* All four bullet vote.

Honest ballots elect **Bree**, the compromise — a result Ari's fans rate a 3:

<!-- report:ex06_bullet_honest -->
```text
[Divergence from STAR]
  STAR                   = Bree
  Choose-One (Plurality) = Ari   (differs from STAR)
  RCV-IRV                = Cash   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/ex06_bullet_honest_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Ari,Bree,Cash
    4 ×   5,   3,   0
    4 ×   0,   2,   5
    1 ×   0,   5,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bree          -- 25 -- First place
   Cash          -- 21 -- Second place
   Ari           -- 20
 Bree and Cash advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bree          -- 5 -- First place
   Cash          -- 4
   Equal Support -- 0
 Bree wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Bree 5 (56%)  ·  Cash 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bree
```
<!-- /report -->

Now the four fans zero Bree out. Nothing else changes:

<!-- report:ex06_bullet_backfire -->
```text
[Divergence from STAR]
  STAR                   = Cash
  Choose-One (Plurality) = Ari   (differs from STAR)
  Approval               = Ari   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Ari,Bree,Cash
    4 ×   5,   0,   0
    4 ×   0,   2,   5
    1 ×   0,   5,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cash          -- 21 -- First place
   Ari           -- 20 -- Second place
   Bree          -- 13
 Cash and Ari advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cash          -- 5 -- First place
   Ari           -- 4
   Equal Support -- 0
 Cash wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Cash 5 (56%)  ·  Ari 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cash
```
<!-- /report -->

**Cash wins** — the candidate all four scored **0**. Their 12 points of honest support were the only thing holding Bree above Cash in the scoring round; withdrawing it didn't promote Ari, it promoted the person they liked least into the runoff, where Ari lost. The plan had a hidden precondition — *Ari must actually be able to reach the top two* — and it was false.

Full exercise, with the parts worked one at a time: [Exercise 6 — Bullet voting backfires](../../../01_STAR/05_Practice/ex06_bullet_backfire.md) (both halves are live on BetterVoting, and each also carries RCV-IRV and Ranked Robin races).

## The same move, by method

| Method | What restricting looks like | What it costs you |
|---|---|---|
| **STAR** | score only your favorite | you keep your full voice in the runoff *only if* your favorite is in it; otherwise you've flattened the two people the runoff is actually between — the case above |
| **Score / Range** | same | strictly worse: there is no runoff to rescue you, so a bullet vote is simply a smaller ballot |
| **Approval** | approve only your favorite | the sharpest version, because Approval has **no canonical sincere ballot** — the threshold is a free parameter, so "insincere" is genuinely arguable. See [Approval's honest limits §3](../../../04_Approval/01_Learn/approval_honest_limits.md) and [is Approval's outcome arbitrary?](../../../04_Approval/01_Learn/approval_indeterminacy.md) |
| **RCV-IRV** | rank one and stop | your ballot **exhausts** when your candidate is eliminated and stops counting entirely — [exhausted ballots](../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md) |
| **Ranked Robin** | rank one and stop | you sit out every pairwise matchup among the candidates you didn't rank — the matchups most likely to decide the race |
| **Proportional STAR** | bullet-vote your slate | it doesn't protect your share — [the PR FAQ answers this directly](../../../03_STAR_PR/01_Learn/star_pr_faq.md) |

## The version that hurts a whole side: a coalition bullet-votes itself apart

STAR ends *forced* vote-splitting — it can't stop a coalition from splitting **itself** by refusing to use the scale. Ada and Ben are on the same side (60 of 100 voters); Cara is the opposition (40). Ada's fans give Ben a 0, Ben's fans give Ada a 0, purely tribally. Scores: Ada 175, Ben 125, **Cara 200** — Cara takes a finalist slot off a split field and wins the runoff, against a 60% majority that preferred her side.

The cure is entirely in the voters' hands, and it's small: [scoring the ally even a 3 elects the majority side](../../../method_comparisons/split_voting/_main/_main_pages/05b_residual_split_expressive-fix.md). Both halves, with the full write-up: [residual vote-splitting](../../../01_STAR/01_Learn/properties_and_limits/residual_vote_splitting.md) · [the bullet-voting half](../../../method_comparisons/split_voting/_main/_main_pages/05a_residual_split_bullet-voting.md).

## When restricting *is* honest

Two cases, both real:

- **You genuinely don't support anyone else.** A 0 that reflects a real 0 is not a strategy, it's an opinion, and STAR is built to record it. Same for leaving a candidate blank — see [abstention vs. zero vs. NOTA](../../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md).
- **Two candidates really are equal to you.** Equal scores are a feature; the runoff reports them as [Equal Support](../../GLOSSARY.md) rather than inventing a preference you never stated.

What makes a restricted ballot *insincere* is flattening people you can actually rank — and the price of that is paid in the round where your flattening leaves you with nothing to say.

## The rule of thumb

**Use the whole scale, top to bottom.** A 5 for your favorite and a 3 for the ally you can live with is a stronger ballot than a lone 5 — it keeps your favorite's support intact *and* keeps you in the runoff if your favorite doesn't make it. The mirror-image mistake, flattening people *upward*, is [expansive sincerity](expansive_sincerity.md), and it fails for the same structural reason.

---

**See also:** [the four kinds of insincere vote](README.md) · [strategic voting across the Equal Vote methods](../strategic_voting.md) · [burial](../burial/README.md) · [favorite betrayal](../../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) · [STAR's honest limits](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Exercise 13 — where do you draw the line?](../../../01_STAR/05_Practice/ex13_draw_the_line.md).

# file: restrictive_sincerity.md
