# Expansive sincerity — tactical maximization, up-voting, the hedge

**Level: 201 · for voters**

*One of [the four kinds of insincere vote](README.md). Expansive sincerity is the **upward** erasure: you keep your favorite at the top and raise someone else to join them — usually a front-runner you can tolerate, as insurance against one you can't.*

It is the insincere vote that looks generous, which is why almost nobody warns you about it. You betrayed nobody. You buried nobody. You lowered nobody. You just gave the acceptable front-runner a 5 as well, *"to be safe."*

What you actually said on that ballot was: **"I have no preference between these two."** If they turn out to be the two who matter, the count will believe you.

## Where it can even happen

Expansive sincerity needs a ballot with a **volume knob** — somewhere to put support that isn't ordering. That narrows it sharply:

| Ballot | Up-voting available? |
|---|---|
| **Score / STAR (0–5)** | ✅ raise any candidate to any level, independently |
| **Approval (yes/no)** | ✅ this is *the* Approval strategy — approve one more than you mean |
| **Ranked** (IRV, Ranked Robin, STV) | ❌ order is zero-sum — raising one candidate lowers another, which makes it [compromising](../../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) or [burial](../burial/README.md), not up-voting |
| **Choose-One** | ❌ one mark, nothing to raise |

So this is a strategy that exists *because* rated ballots let you support two people at once — the same feature that makes [equal-top scoring free](../../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) and lets you avoid favorite betrayal in the first place. It is worth being precise about that trade rather than pretending rated ballots removed strategy: they removed the *forced* strategy and left an optional one whose costs you can see and reason about.

## In STAR: your hedge is loud in round one and silent in round two

A STAR score does two different jobs. In the **scoring round** it decides who the two finalists are — there, a 5 is worth five times a 1. In the **automatic runoff** only *order* is read — there, a 5-vs-4 and a 5-vs-0 count exactly the same, and a 5-vs-5 counts as **[Equal Support](../../GLOSSARY.md)**: you sit the runoff out.

Put those together and the hedge has a precise failure mode. You spend real points helping your hedge reach the final two, and then have nothing left to say if they get there *against your favorite*.

Nine voters, worked in full — a neighborhood association picking a chair between **Alma**, **Bruno** and **Celia**. Alma's four core members honestly score Bruno a 3 and Celia a 0. Honest ballots elect **Alma**, 5–4 in the runoff, with all nine voters expressing a preference. Then the four hedge — Bruno 3 → 5, nothing else changed, Alma still at 5:

<!-- report:tactical_max_c3_b9_hedged -->
```text
[Divergence from STAR]
  STAR                   = Bruno
  Choose-One (Plurality) = Alma   (differs from STAR)
  RCV-IRV                = Alma   (differs from STAR)
  Note: 4 of 9 ballots (44%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/tactical_max_c3_b9_hedged_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Alma,Bruno,Celia
    4 ×    5,    5,    0
    3 ×    1,    5,    3
    1 ×    4,    2,    1
    1 ×    0,    2,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 39 -- First place
   Alma          -- 27 -- Second place
   Celia         -- 15
 Bruno and Alma advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 4 -- First place
   Alma          -- 1
   Equal Support -- 4
 Bruno wins.
   Runoff math:
     9  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Bruno 4 (80%)  ·  Alma 1 (20%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```
<!-- /report -->

**Bruno wins.** `Voters with a preference: 5 of 9 (4 Equal Support)` — the four hedgers removed themselves from the only comparison they cared about, and Alma's 5–4 win became a 4–1 loss. Celia, the candidate they were insuring against, finished third on 15 points and never reached the runoff in either version.

Both halves, the ballot table, and the general rule: [the worked STAR up-voting pair](../../../01_STAR/03_Criteria/tactical_maximization/README.md).

## In Approval: the other half of the threshold dilemma

Approval has no volume, only a line — so up-voting means **approving one more candidate than you honestly endorse**, typically the tolerable front-runner. This is the exact mirror of [bullet voting](restrictive_sincerity.md), and Approval's central critique is that a voter must choose between them with no honest guidance:

- Approve only your favorite → you may fail to stop the candidate you can't stand.
- Approve the front-runner too → **your two marks cancel each other** in the only matchup that was ever in doubt.

Approval can't split the difference, because there is nothing between yes and no. That's the dilemma stated fairly — and the reason the [approval threshold](../../../04_Approval/01_Learn/approval_honest_limits.md) is called Approval's free parameter rather than its flaw: on one reading of what a checkmark *means*, no Approval ballot is insincere at all ([the three readings, and what each does to the strategy question](../../../04_Approval/01_Learn/approval_in_the_literature.md)).

Watch it decide an election: [Exercise 13 — where do you draw the line?](../../../01_STAR/05_Practice/ex13_draw_the_line.md) runs one set of honest opinions at three different thresholds and gets three different winners.

## The fix is one point, and it's honest

STAR's answer to the hedging instinct isn't "don't hedge" — it's **hedge with a 4**:

- **5 for your favorite, 4 for the hedge.** The hedge gets 80% of the score support a 5 would have given them, so your insurance is nearly intact — and your ballot still carries a full vote for your favorite if the two of them meet in the runoff.
- **Equal scores stay available for real indifference.** If you genuinely don't care which of two candidates wins, saying so is correct, and the runoff line reports your Equal Support instead of inventing a preference. See [runoff percentages](../../../01_STAR/01_Learn/the_count/runoff_percentages.md).

That's the practical shape of "use the whole scale," and it is why STAR's honest advice fits in a sentence: **show your real order, and use every level you've got.**

## Reading this fairly

This is a mistake voters make against themselves, not a defect the count introduced — STAR counted a stated indifference as indifference, which is the only thing it could honestly do. But it belongs on the honest-limits ledger anyway, for one reason: **it means a rated ballot has a wrong way to fill it in that feels generous.** A voter who hedges to a 5 out of anxiety has given up something real, and nothing on the ballot tells them so. That's an argument for [teaching the runoff](../../../01_STAR/01_Learn/the_count/README.md), not an argument against the method — the same way "rank all the candidates" is the thing ranked-ballot advocates have to teach.

The mirror-image mistake — flattening people *downward* to 0 — is [restrictive sincerity](restrictive_sincerity.md), and it fails for the same structural reason: erasing a preference you actually hold leaves you mute in the round where it mattered.

---

**See also:** [the four kinds of insincere vote](README.md) · [the worked STAR pair](../../../01_STAR/03_Criteria/tactical_maximization/README.md) · [restrictive sincerity](restrictive_sincerity.md) · [strategic voting across the Equal Vote methods](../strategic_voting.md) · [STAR's honest limits](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Approval's honest limits](../../../04_Approval/01_Learn/approval_honest_limits.md).

# file: expansive_sincerity.md
