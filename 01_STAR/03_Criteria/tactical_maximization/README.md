# 01_STAR/03_Criteria/tactical_maximization — the worked STAR up-voting pair

**Level: 201 · for voters**

The strategy nobody warns you about, because it doesn't *feel* like a strategy: you keep your favorite at 5, you lower nobody, you just **raise** a candidate you're lukewarm about — insurance, in case your favorite can't win. In the [Equal Vote taxonomy](../../../07_Concepts/topics/insincere_votes/README.md) that's **expansive sincerity**, also called *tactical maximization* or *up-voting*, and it is the one insincere vote that looks generous.

In STAR it has a specific, countable price. A score does two jobs — it picks the **finalists** in the scoring round, and it sets your **preference order** in the automatic runoff. Give two candidates the same 5 and you have voted for both in the first job and for *neither* in the second: your ballot registers **[Equal Support](../../../07_Concepts/GLOSSARY.md)** and sits out the runoff. Hedge onto a candidate who then reaches the final two against your favorite, and you have spent your vote helping them get there and kept nothing back to stop them.

This pair shows exactly that, on nine ballots.

## The electorate

A neighborhood association of nine elects a chair: **Alma**, **Bruno**, **Celia**.

| Count | Alma | Bruno | Celia | who they are |
|:---:|:---:|:---:|:---:|---|
| 4 | **5** | 3 | 0 | Alma's core — they honestly like Bruno *fine*, and don't want Celia — **the hedgers-to-be** |
| 1 | 4 | 2 | 1 | an independent, leaning Alma |
| 3 | 1 | **5** | 3 | the Bruno bloc |
| 1 | 0 | 2 | **5** | Celia's one loyalist |

Two facts to hold onto: **Bruno leads on points** (31 to Alma's 27), and **Celia is nowhere** (15 — she cannot reach the runoff from there, and never does in either half).

## Half 1 — honest ballots elect Alma

<!-- report:tactical_max_c3_b9_honest -->
```text
[Divergence from STAR]
  STAR     = Alma
  Approval = Bruno   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Bruno)
 - Runoff Round Winner   = (Alma)
  Candidate Bruno earned the highest total score, but
  Candidate Alma won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Alma,Bruno,Celia
    4 ×    5,    3,    0
    3 ×    1,    5,    3
    1 ×    4,    2,    1
    1 ×    0,    2,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 31 -- First place
   Alma          -- 27 -- Second place
   Celia         -- 15
 Bruno and Alma advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alma          -- 5 -- First place
   Bruno         -- 4
   Equal Support -- 0
 Alma wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Alma 5 (56%)  ·  Bruno 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alma
```
<!-- /report -->

Bruno wins the scoring round and loses the runoff — the ordinary [runoff reversal](../../02_Examples/runoff_overturns_leader/README.md), STAR working as designed. Read the last line: **9 of 9 voters had a preference.** Alma's 5–4 margin *is* the four hedgers plus the independent. Their honest 3 for Bruno was worth real points to him and cost them nothing, because in the runoff a 5 over a 3 is a full vote for Alma.

## Half 2 — the same four raise Bruno to a 5, and Bruno wins

Nothing else changes. Alma keeps her four 5s and her total of 27. The four simply move Bruno 3 → 5, hedging against a Celia win.

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

Three things happened at once, and only the first was intended:

- **Bruno's total went 31 → 39.** The hedge worked *in the scoring round* — which was the round he was already winning.
- **The finalists didn't change.** Bruno and Alma, both halves. The insurance bought nothing, because Celia was never the risk.
- **Four of nine voters left the runoff.** `Voters with a preference: 5 of 9 (4 Equal Support)` — the hedgers scored both finalists 5, so STAR reads them as having no preference between them. Alma's 5–4 win becomes a 4–1 loss.

They insured against Celia and paid the premium to Bruno.

## The rule this yields

**A 5 you give a rival is loud in the scoring round and silent in the runoff.** So hedge only against a candidate who can realistically *reach the final two* — and never against someone you'd want to beat there. Concretely, on a STAR ballot:

- **Equal scores are free when you truly don't care** which of the two wins. That's the feature: Equal Support is an honest answer, and [the runoff percentage line](../../01_Learn/the_count/runoff_percentages.md) reports it rather than burying it.
- **Equal scores are expensive when you do care.** One point of daylight — 5 and 4 — keeps your full vote in the runoff while giving your hedge nearly all the score support a 5 would have. That is almost always the right move, and it is *honest*, which is what makes STAR's advice easy: **show your real order, use the whole scale.**

## Reading this fairly

This is a self-inflicted wound, not a criterion failure. STAR did nothing unexpected: it counted a stated indifference as indifference. The four voters got a worse result than honesty would have given them — which is the [1:1 strategy ratio](../../../07_Concepts/topics/strategic_voting.md#what-the-simulations-say) doing its job, since a strategy that backfires this plainly isn't worth attempting. Compare the two directions:

- **Up-voting** (here) → you lose your say in the runoff.
- **[Down-voting / bullet voting](../../05_Practice/ex06_bullet_backfire.md)** → you lose your say among everyone you flattened to 0, and can knock your own compromise out of the finals.

Both fail for the same structural reason, which is the honest case for STAR's two-round count: **exaggeration in either direction costs you information you might have needed.** The one place STAR genuinely *fails* on paper is the top of the ballot — see [the favorite-betrayal pair](../favorite_betrayal/README.md), the repo's concession case.

## Run it yourself

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/03_Criteria/tactical_maximization/cases/tactical_max_c3_b9_honest.yaml
```

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/03_Criteria/tactical_maximization/cases/tactical_max_c3_b9_hedged.yaml
```

Pages: [honest](cases/cases_pages/tactical_max_c3_b9_honest.md) · [hedged](cases/cases_pages/tactical_max_c3_b9_hedged.md). Sources: [tactical_max_c3_b9_honest.yaml](cases/tactical_max_c3_b9_honest.yaml) · [tactical_max_c3_b9_hedged.yaml](cases/tactical_max_c3_b9_hedged.yaml). Full mirrors: [honest](cases/cases_tabulated/tactical_max_c3_b9_honest_tabulated.txt) · [hedged](cases/cases_tabulated/tactical_max_c3_b9_hedged_tabulated.txt).

**LH-only, deliberately.** The ballots in half 2 are a counterfactual — nobody cast them — so there is no BetterVoting election to link; the pair is reproducible from these files instead.

---

**Related:** [the four kinds of insincere vote](../../../07_Concepts/topics/insincere_votes/README.md) (the taxonomy hub) · [expansive sincerity, across methods](../../../07_Concepts/topics/insincere_votes/expansive_sincerity.md) · [restrictive sincerity — the mirror image](../../../07_Concepts/topics/insincere_votes/restrictive_sincerity.md) · [STAR's honest limits](../../01_Learn/properties_and_limits/STAR_honest_limits.md) · [strategic voting](../../../07_Concepts/topics/strategic_voting.md).

# file: README.md
