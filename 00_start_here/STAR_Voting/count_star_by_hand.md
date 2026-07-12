# Count a STAR election by hand

*One of STAR's quiet superpowers: you can tally it with a pencil, paper, and grade-school arithmetic — no computer required. This page walks you through counting a real STAR election by hand, start to finish, so "STAR is simple and hand-countable" stops being a claim and becomes something you've actually done.*

**Level: 101.** You'll need only the [two rounds](STAR_start_here.md): add the stars, then count the runoff.

## What you're counting

A stack of ballots. Each ballot has a **0–5 score for every candidate** (blank counts as 0). That's it. We'll use the [team-lunch election](../../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md) — 5 voters choosing **Sushi, Tacos, or Pizza**:

```text
              Sushi  Tacos  Pizza
  Ballot 1      5      0      3
  Ballot 2      5      0      3
  Ballot 3      0      5      3
  Ballot 4      0      5      3
  Ballot 5      3      1      5
```

## Round 1 — the Scoring Round: add up the stars

Go **down each column** and add. That's the whole first round.

```text
              Sushi  Tacos  Pizza
  add the      5+5+   0+0+   3+3+
  column   =   0+0+   5+5+   3+3+
               3      1      5
  ─────────   ────   ────   ────
  TOTAL         13     11     17
```

- Sushi **13**, Tacos **11**, Pizza **17**.
- **Circle the two highest totals** — those are the **finalists**: **Pizza (17)** and **Sushi (13)**. Tacos is out.

That's it for Round 1: addition and picking the top two.

## Round 2 — the Automatic Runoff: one vote per ballot

Now look **only at the two finalists** (Pizza and Sushi) and go **ballot by ballot**. On each ballot, whichever finalist got the **higher score** earns **one tally mark**. (If a ballot scored both finalists the *same*, it's **[Equal Support](are_equal_score_votes_discounted.md)** — no mark for either; it still counted in Round 1.)

```text
            Sushi  Pizza   higher?        mark
  Ballot 1    5      3      Sushi          Sushi ✓
  Ballot 2    5      3      Sushi          Sushi ✓
  Ballot 3    0      3      Pizza          Pizza ✓
  Ballot 4    0      3      Pizza          Pizza ✓
  Ballot 5    3      5      Pizza          Pizza ✓
  ─────────────────────────────────────────────
  TALLY:                   Pizza 3  ·  Sushi 2
```

**Pizza 3, Sushi 2 — Pizza wins.** More voters preferred Pizza head-to-head, so Pizza takes it. Done — you just hand-counted a STAR election.

*(Cross-check: this matches the [live BetterVoting result](https://bettervoting.com/fyy886/results) and the engine exactly — Pizza 17 in scoring, Pizza 3–2 in the runoff.)*

## The whole recipe, on one card

1. **Add each candidate's column** of scores → totals.
2. **Top two totals = the finalists.**
3. **For each ballot, one mark** to whichever finalist it scored higher (equal = no mark).
4. **Most marks wins.** (Exact tie → the [tie-break rules](Tie_Breaking_STAR/tie_breaking.md).)

## Why this scales — the part that matters for real elections

For one room, count it directly as above. For a *big* election across many precincts, STAR has a property IRV lacks: it's **[summable](STAR_summability.md)**. Each precinct can report two small, fixed-size tables —

- the **score totals** per candidate, and
- the **preference matrix** (for each *pair* of candidates, how many voters preferred each) —

and those tables simply **add up** across precincts to give the national result. You never have to ship every ballot to one place. That's why STAR can be hand-counted and **risk-limiting-audited** at scale.

Contrast **[RCV-IRV](../RCV_IRV/RCV_IRV_is_simple.md)**: because it eliminates candidates round by round and *transfers* votes, a precinct can't publish a subtotal that adds up — every ballot has to reach a central count, and a single changed ballot can cascade. STAR's "add, then compare the top two" is genuinely a pencil-and-paper method; IRV's is not.

## A faster runoff for a big stack: sort into three piles

Instead of marking each ballot one by one, **sort the whole stack into three piles** — *prefers finalist A*, *prefers finalist B*, and *Equal Support* (scored them the same) — then just count the two preference piles. That's the method the Equal Vote Coalition's official procedure uses, along with role assignments (a caller, a verifier, one tallier per star-level) and practical tips (train on test ballots, use a straight-edge to keep tally rows aligned): [**BetterVoting — Hand Counting STAR**](https://docs.bettervoting.com/help/hand_count.html). Teaching it to a group? See [Teaching STAR Voting](teaching_star_voting.md).

## Try it yourself

- Grab the [ballot styles](STAR_ballot_voting_styles.md) and make up your own 3-voter election — count it by hand, then run it on [bettervoting.com](https://bettervoting.com) and check you agree.
- Or run the file: `python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/bv2184_fyy886_lunch_vote.yaml` and compare its Scoring Round and Automatic Runoff to your hand tally.

## See also

- [STAR — start here](STAR_start_here.md) · [the Scoring Round](STAR_Scoring_Round.md) · [the Automatic Runoff](STAR_Automatic_Runoff.md)
- [Summability](STAR_summability.md) — why the precinct tables add up · [Equal Support](are_equal_score_votes_discounted.md) — the "no preference" case
- [Reading the runoff percentages](runoff_percentages.md) — the two denominators, once you have the tally
