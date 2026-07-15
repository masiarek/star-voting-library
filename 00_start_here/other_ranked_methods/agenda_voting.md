# Agenda Voting — when the *order of the vote* picks the winner

*Same ranked ballots, different tabulation — taken to the extreme. In agenda voting the tabulation has a **parameter**: the order in which alternatives face each other. Change the agenda, change the winner — with the very same ballots. It is the cleanest illustration in the repo of why "the ballots" never decide anything by themselves; the procedure always co-decides.*

→ Companions: [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) (the *neutral* way to run the same pairwise matchups) · [Borda](borda.md) · Glossary: [`Condorcet`](../GLOSSARY.md)

**Source:** notes digested from Sherif El-Helaly, *The Mathematics of Voting and Apportionment* (§1.3.5–1.3.7), collected in Adam's [Tactical Voting doc](https://docs.google.com/document/d/1-xpTrD2TEaGCRp5iCd-Ao9cqu7sH2uXNTYF21gxCY00/edit). Paraphrased summary — see the book for the full text.

---

## What it is

Agenda voting is the parliamentary/committee procedure: list the alternatives in a fixed order (the **agenda**), then run **sequential pairwise majority votes** — the first two alternatives face off, the survivor meets the third, and so on down the list. The survivor of the last vote wins. A tie between the *i*-th and *j*-th agenda entries (*i* < *j*) goes to the **later** entry, so the procedure always produces exactly one winner.

Two things follow immediately:

- It is **not neutral** — alternatives are treated differently by construction (position in the agenda matters). That is why it is used for *policies* (motions vs. status quo), never for candidates.
- It runs only a **subset** of the pairwise matchups, in sequence. Contrast **Ranked Robin**, which runs *every* matchup symmetrically — the neutral, order-free way to consume the same ranked ballots.

## The agenda picks the winner (all four can win)

Nine voters, four alternatives:

| 4 voters | 3 voters | 2 voters |
|:-:|:-:|:-:|
| a | c | b |
| d | b | a |
| c | d | d |
| b | a | c |

With **these exact ballots**, the winner is whatever the agenda-setter wants it to be:

| Agenda | Winner |
|---|:-:|
| `c b a d` | **a** |
| `c a b d` | **b** |
| `d a b c` | **c** |
| `a b c d` | **d** |

(This profile has a Condorcet cycle, which is what gives the agenda its power — see below for when it *doesn't*.)

## Properties — a mixed report card

- **Condorcet winner criterion: PASS.** A Condorcet winner survives every matchup, so it wins under *every* agenda. Conversely, the **left-most** (first-listed) alternative wins if and only if it is the Condorcet winner — first position is the *worst* slot, having to survive every round.
- **Condorcet loser criterion: PASS.** A Condorcet loser loses its first matchup under any agenda.
- **Monotone: PASS.** Raising an alternative on some ballots never hurts it.
- **Weak Pareto efficiency: FAIL** — the interesting one, next section.
- An alternative that loses under **every** agenda need *not* be a Condorcet loser. Three voters, five alternatives:

  | Voter 1 | Voter 2 | Voter 3 |
  |:-:|:-:|:-:|
  | a | b | c |
  | b | c | e |
  | d | d | a |
  | e | a | d |
  | c | e | b |

  No Condorcet winner exists and *d* is not a Condorcet loser — yet no agenda makes *d* win.

## The Weak Pareto failure

**Pareto dominated** = some rival is ranked above you by *every single voter*. A method is *Weakly Pareto efficient* if it never elects a Pareto-dominated alternative — about the mildest quality bar imaginable. Agenda voting fails it. Three voters:

| Voter 1 | Voter 2 | Voter 3 |
|:-:|:-:|:-:|
| a | b | c |
| d | c | a |
| b | a | d |
| c | d | b |

Every voter ranks **a above d** — yet agenda `a c b d` elects **d**. (The trick: *a* gets used up beating others early, and *d*, sitting last in the agenda, only has to win its one final matchup.)

Keep the two "loser" notions distinct:

- **Condorcet loser** — loses *by a majority* to **every** opponent. Agenda voting protects against this.
- **Pareto dominated** — loses *unanimously* to **just one** opponent. Agenda voting does *not* protect against this.

Neither implies the other, and agenda voting passing the first while failing the second is the proof.

## The killer amendment (tactical *nomination*, not tactical voting)

In parliamentary practice the agenda is fixed by the bylaws: latest amendment first, status quo last (`motion b` vs. `status quo a` → agenda `b a`; amend the motion to *c* → agenda `c b a`). So you can't game the agenda order — but you *can* game **what gets nominated onto it**.

Setup: 11 voters, motion *b* vs. status quo *a*. Nine of the eleven prefer the motion — a straight vote kills the status quo 9–2. The two status-quo supporters rescue it by introducing a **killer amendment** (aka *poison pill*) *c*, engineered to split the pro-motion camp roughly in half — half love the amendment, half hate it worse than the status quo:

| 2 voters | 4 voters | 5 voters |
|:-:|:-:|:-:|
| a | c | b |
| c | b | a |
| b | a | c |

Agenda `c b a`: *c* beats *b* 6–5, then *a* beats *c* 7–4. **The status quo wins against the wishes of a 9-of-11 majority.** The amendment manufactured a Condorcet cycle, and the bylaws' agenda walks straight into it. Crucially, no voter changed their *a*-vs-*b* preference — nobody was persuaded; the *nomination* did all the work. That makes this a **tactical nomination**, a different animal from tactical voting (the ballots stay sincere).

The textbook's memorable version: five students, a standing order of vegetarian pizza (*a*), a motion to add pepperoni (*b*) that 4 of 5 support. The lone vegetarian, knowing two of the four pepperoni fans love hot pepper and two hate it, amends the motion to "pepperoni **and** hot pepper" (*c*). Profile 1×(a c b), 2×(c b a), 2×(b a c); agenda `c b a`: *c* beats *b* 3–2, *a* beats *c* 3–2 — **vegetarian pizza survives** with 4 of 5 voters against it.

### When does the poison pill work?

Generalize: *m* voters back the status quo (all ranking the amendment in the middle: a > c > b), and of the *n* pro-motion voters, *n₁* rank the amendment on top (c > b > a) and *n₂* rank it last (b > a > c), with *m* < *n*:

| m | n₁ | n₂ |
|:-:|:-:|:-:|
| a | c | b |
| c | b | a |
| b | a | c |

The kill needs *c* to beat *b* first, then lose to *a*: `m + n₁ > n₂` **and** `m + n₂ > n₁`. Both hold exactly when

> **|n₁ − n₂| < m — the killer amendment succeeds iff it splits the pro-motion camp more finely than the status-quo bloc's own size.**

Fail modes (from the book's 23-voter drill: 17 pro-motion, 6 status quo): let too many rank the amendment *last* and the motion becomes a Condorcet winner (pill ignored); let too many rank it *first* and the **amendment itself** becomes the Condorcet winner — the killer turns "monster" and passes. Two of the four drill scenarios succeed (splits 6/11 and 11/6 against m = 6), two fail (5/12 and 12/5).

## Why this earns a page in a STAR repo

1. **Procedure ≥ ballots.** The nine-voter example is the sharpest possible "same ballots, four different winners" demo — stronger than any STAR-vs-IRV divergence, because here even the *method* is fixed and only a sequencing parameter moves.
2. **Neutrality is a feature you can lose.** Ranked Robin = all pairwise matchups, order-free, neutral. Agenda voting = some pairwise matchups, in an order someone chose. Same ballot type, same majority-rule primitive, wildly different manipulability.
3. **Cycles are exploitable, not just curiosities.** The killer amendment is a Condorcet cycle *built on purpose*. When we flag a cycle in an RR report, this is what a cycle is worth to a motivated actor under a sequential procedure.
4. **Tactical nomination ≠ tactical voting.** Every ballot in the killer-amendment story is sincere. Manipulating the *choice set* is its own strategy family — worth keeping distinct in debate prep.

## Related

- [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) — the neutral round-robin over the same matchups
- [Cycle resolution](../RCV_Ranked_Robin/cycle_resolution.md) — what to do when the cycle isn't manufactured
- [Borda](borda.md) — the other classic "ranked but not Condorcet" method in this folder
- [Scoring methods vs. ranked voting](../topics/scoring-methods-vs-ranked-voting.md) — the ballot-type map
