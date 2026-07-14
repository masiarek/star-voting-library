# Are Equal-Score Votes "Discounted"?

*The objection, in its strongest form: in STAR, a ballot that scores both finalists the same (a 5/5, a 0/0) is tagged "no preference" and moves nothing in the Automatic Runoff. Sometimes that's a lot of ballots. Isn't that just a discounted vote? This page answers honestly: it concedes the mechanical fact, shows why "discounted" is the wrong word, proves with a runnable election that these ballots do real work, and names the one version of the criticism that genuinely lands.*

→ Companions: [Equal Support in both rounds (the demo)](../../01_STAR/_main/_main_pages/equal_support_runoff_demo.md) · [the Automatic Runoff](STAR_Automatic_Runoff.md) · ["exhausted ballots," untangled](../RCV_IRV/exhausted_ballots_301.md) · [common misunderstandings](common_misunderstandings.md) · Glossary: [`Equal Support`](glossary_STAR.md)

---

## What actually happens to an equal-score ballot

The mechanical claim is true, and there is no point denying it: if you score both finalists the same, your ballot does not move the margin between them. Concede that up front — it buys credibility for what follows.

Where the criticism goes wrong is the word **"discounted."** Discounted implies the voter tried to say something and the system threw it away. That is not what happened. The voter looked at the two finalists and said, explicitly, "these two are equal to me" — and the system recorded exactly that. A tie vote cannot break a tie, but it wasn't ignored; it was counted as what it was: **Equal Support**, neutral between those two.

Two details make this concrete:

- **One label, two honest opposites inside it.** Some Equal Support voters scored *both* finalists high ("I'd be glad with either"); some scored *both* low ("I wanted neither of these two"). Either way it is no preference *between these two* — and either way the ballot was counted in full in the Scoring Round that chose them. On a results pie, Equal Support is the thin slice that makes the finalists' shares add to a bit under 100% — present voters, not missing ones.
- **The ballot instruction says exactly this.** *"Equal scores indicate no preference"* is a statement about the **runoff**. In the Scoring Round, those scores counted at full weight.

## The key contrast: a declared tie is not a lost voice

The sharpest way to see why "discounted" fails is to compare the thing critics never call discounted. In RCV-IRV, if your ballot doesn't rank the two finalists — you ran out of rankings, or the ballot only allowed three — it is **exhausted**: set aside because the system *doesn't know* what you think about A versus B. A STAR equal-score ballot is the opposite: the system knows *exactly* what you think about A versus B, because you told it — they're equal.

> **In RCV-IRV, an exhausted ballot is a voter who lost their voice. In STAR, an equal-score ballot is a voter who declared a tie.**

One is missing data; the other is present data that happens to be neutral. Treating "I am equally happy with either winner" as a *failure to be counted* is the part of the criticism that doesn't survive contact. The full taxonomy of what "exhausted" hides is its own page: [exhausted ballots, untangled](../RCV_IRV/exhausted_ballots_301.md).

## Proof they're counted: an election where equal-score ballots pick the finalists

Run [`equal_support_runoff_demo.yaml`](../../01_STAR/_main/equal_support_runoff_demo.yaml) ([reader page](../../01_STAR/_main/_main_pages/equal_support_runoff_demo.md)). 100 voters: 40 score **both A and B a 5** (love both, C = 0), 35 prefer A over B (5 vs 3), 25 want only C.

```text
--- STAR Voting Method (single winner) ---
 Tabulating 100 ballots.
Count × A,B,C
   40 × 5,5,0
   35 × 5,3,0
   25 × 0,0,5

Scoring Round
 The two highest-scoring candidates advance to the next round.
   A             -- 375 -- First place
   B             -- 305 -- Second place
   C             -- 125
 A and B advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 35 -- First place
   B             --  0
   Equal Support -- 65
 A wins.
```

Read the two rounds against the objection:

- **Scoring Round:** A and B top the totals *because of* the 40 equal-A-B ballots — those 5/5s are what pushed both finalists past C. The "ignored" ballots literally chose who is in the final.
- **Automatic Runoff:** A beats B 35–0, decided by the voters who *had* a preference between them. The 65 Equal Support ballots (the 40 both-5s and the 25 both-0s) are neutral — because their voters *are* neutral between A and B.

Counted in both rounds, decisive in neither tie they had no stake in — a very different story from "discounted."

## The honest concession: coarse scales can swallow a faint preference

There is one version of this criticism that is legitimate, and pretending otherwise would cost more than it saves. Suppose you like A a *tiny* bit more than B, but you think both are excellent and you want them both to beat C. On a 0–5 scale you might give both a 5 to keep them strong — and now a preference you really had is recorded as a tie. The ballot's resolution failed to capture it. In one Oregon Independent Party race, nearly 30% of runoff ballots landed as "no preference," and some of those voters surely had a faint lean they maxed out of existence.

That is a fair, objective criticism of *cardinal ballots with few levels* — a self-inflicted discount the scale makes easy. The practical answer is voter education, and it's one sentence: **show the gap you feel between the front-runners — if you like A more, give A the 5 and B a 4.** Your 4 still supports B strongly in the Scoring Round, and your preference now counts in the runoff. (STAR's design rewards exactly this honesty; see [the ways to fill out a STAR ballot](STAR_ballot_voting_styles.md).)

## The asymmetry: compare it to how ranked-IRV ballots get wasted

Does the concession mean STAR "wastes" votes just like the thing it criticizes? No — the two failure modes are not symmetric. A STAR equal-score ballot is *voluntary neutrality*; the worst case is a voter who maxed out two candidates they both love. RCV-IRV's wasted votes are *involuntary*, and they hit voters who had explicit preferences:

- **Voided ballots** — equal or skipped rankings can spoil the whole ballot, and that error rate falls hardest on the voters with the least support navigating the format.
- **Favorite in the final, and loses** — if your favorite reaches the last round and loses, your backup rankings are never read at all.
- **Your next choice is already gone** — by the time your vote is ready to transfer, the candidate it would have gone to may already be eliminated.

In every one of those cases the voter *supplied* a preference and the count never used it. So the debate move is: concede the equal-score mechanic, then ask the critic to account for those. See [exhausted ballots, untangled](../RCV_IRV/exhausted_ballots_301.md) and [Why STAR Voting](../Why_STAR_Voting.md) (usability / exhausted ballots).

## The takeaway

An equal-score ballot isn't a discounted vote — it's a voter who said, in their own hand, that they're equally happy with either finalist. It was counted in full in the round that picked the finalists, and it stayed neutral in the one contest it had no stake in. And if you *do* have a preference, STAR rewards you for showing it — so show it.

---

## Where this fits in the teaching

This is **objection-handling material for skeptics and the RCV-advocate audience** — don't raise "discounted votes" with a first-contact audience; you'd plant a doubt they didn't have. It hangs off two 101 moments: where [Equal Support](glossary_STAR.md) is first introduced, and the STAR-vs-RCV-IRV comparison. Presenters: the matching slides are indexed by short name in [LINKS.md](../LINKS.md) ("No-preference votes in the STAR runoff"; "Combatting strategic voting"; the exhausted-ballot slides), and the episode roadmap lives in [conversation scripts](../conversation_scripts.md).
