# 🗳️ Electoral systems & proportional representation — the comparative and civic view

Most of this repo is about picking **one** winner well. This shelf zooms out: how *whole systems* compare across countries, how legislative **seats** get apportioned, and how a citizen is supposed to weigh the trade-offs. Essential once the conversation moves from "which single-winner method?" to "what should our elections look like?"

← Back to [Books on Voting Methods](README.md)

---

<table>
<tr>
<td width="150" valign="top"><img src="img/electoral_systems_farrell.jpg" width="130" alt="Cover of Electoral Systems by David Farrell"></td>
<td valign="top">

### Electoral Systems: A Comparative Introduction — David M. Farrell (2001; 2nd ed. 2011)

The standard survey course in a book: plurality, majority (including the alternative vote / IRV), list-PR, and the single transferable vote, each with real-country evidence and a fair accounting of consequences. If you want *one* book on how the world's actual systems work and differ, this is it.

**The lean:** Comparative-politics neutral — Farrell describes and assesses rather than campaigns. A political-science lens (party systems, governance), which usefully complements this repo's mechanism-and-ballot lens.

**In this repo:** [electing more than one](../topics/electing_more_than_one.md) · [two-party dominance](../topics/two_party_dominance.md) · [STV vs. proportional STAR](../../method_comparisons/stv_vs_star_pr/README.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/behind_the_ballot_box_amy.jpg" width="130" alt="Cover of Behind the Ballot Box by Douglas Amy"></td>
<td valign="top">

### Behind the Ballot Box: A Citizen's Guide to Voting Systems — Douglas J. Amy (2000)

Exactly what the subtitle says — the most accessible *civic* book on the shelf. Amy walks a general reader through how different systems shape representation, turnout, and fairness, in plain language and with a reformer's eye.

**The lean:** Amy is a **proportional-representation advocate**; the book makes the case that PR beats winner-take-all for representativeness. Read it for the clearest citizen-level argument *for* multi-winner PR — a lever this repo also points to (single-winner method choice can't fix what only proportionality can — see [two-party dominance](../topics/two_party_dominance.md)).

**In this repo:** [two-party dominance](../topics/two_party_dominance.md) · [wasted votes](../topics/wasted_votes.md) · [proportional representation](../../03_STAR_PR/01_Learn/README.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/fair_representation_balinski_young.jpg" width="130" alt="Cover of Fair Representation by Balinski and Young"></td>
<td valign="top">

### Fair Representation: Meeting the Ideal of One Man, One Vote — Michel L. Balinski & H. Peyton Young (1982; 2nd ed. 2001)

The definitive book on **apportionment** — how a fixed number of seats gets divided among states or parties by population — and the **readable** one, which is why it sits before Pukelsheim below rather than after him. Balinski and Young tell the story of how the United States argued about this for two centuries — Jefferson against Hamilton, Webster, the Alabama paradox of 1880, the Oklahoma paradox of 1907 — and build the mathematics out of that narrative rather than the other way round. It is the source of the **Balinski–Young impossibility theorem**: no apportionment rule can both stay within quota and avoid all the paradoxes. Pukelsheim, who cites it throughout, says it tells the tale "in a vivid and enlightening manner" — a generous verdict from the man who wrote the technical version instead.

**The lean:** Rigorous, and not advocacy about *ballots* — the apportionment problem is orthogonal to which ballot you use, making this the shelf's least partisan entry. Worth knowing that they do argue a position *within* apportionment: they favor Webster / Sainte-Laguë, and say so plainly.

**Why it matters here:** the impossibility result is the reason [STAR-PR's method choice](../../03_STAR_PR/01_Learn/STAR_PR/README.md) is a genuine trade rather than a solved problem — Allocated Score buys its quota guarantee from the family with the monotonicity problems, RRV buys monotonicity by giving up the guarantee. Read this before concluding either is simply right.

**In this repo:** [the math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md) · [what "proportional" actually means](../../03_STAR_PR/01_Learn/what_proportional_means.md) · [electing more than one](../topics/electing_more_than_one.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"></td>
<td valign="top">

### Proportional Representation: Apportionment Methods and Their Applications — Friedrich Pukelsheim (2nd ed. 2017)

The definitive mathematical treatment of the problem underneath every proportional system: given each group's claim, how do you turn fractions into whole seats *fairly*? Pukelsheim builds the whole apparatus — rounding rules, the split between **quota methods** ("divide and rank") and **divisor methods** ("divide and round"), seat bias, and the classical paradoxes (Alabama, population, new-states, no-show) — then applies it to real European Parliament and Bundestag elections. Chapter 16 is a biographical digest of the people whose names the vocabulary carries: Hare, Droop, Hagenbach-Bischoff, D'Hondt, Sainte-Laguë, Jefferson, Webster.

**The lean:** None to speak of — this is mathematics with worked legal applications, not advocacy. It is also genuinely technical; treat it as a reference to consult rather than a book to read front to back.

**Reading it for STAR-PR — and the caveat first.** Pukelsheim assumes **party vote totals** as input. STAR-PR has no parties: it takes a ballot matrix and reweights *sequentially*. So the vocabulary and the paradox analysis transfer; the axiomatic results do not transfer automatically, because they are proved for one-shot apportionment. With that said, the chapters that pay off directly:

| Chapter | Why it matters here |
|---|---|
| **5 — Quota methods** | Allocated Score *is* a quota method; §5.2's Hare-quota-with-greatest-remainders is the closest classical relative of fractional surplus handling |
| **7 — Seat biases** | The quantified version of "Hare favors small factions, Droop favors large" — a formula instead of a rule of thumb |
| **9 — Coherence and paradoxes** | Alabama, population and no-show paradoxes, with the formal apparatus. Whether Allocated Score exhibits them is untested here |
| **10 — Goodness-of-fit** | How to *measure* whether an outcome was proportional — the answer to "with no parties, how would you check?" |
| **3 — Rounding rules** | §3.12 "Simple Rounding Does Not Suffice!" — fractional surplus is a rounding problem |
| **4 — Divisor methods** | RRV's family (Jefferson/D'Hondt-style divisors), which is *why* it behaves unlike the quota methods |
| **2 §2.7–2.9** | Equality of voters' **success values** — the rigorous statement of what proportionality is trying to equalise |

Mostly skip chapters 1, 6, 12 and 13 (country-specific party-list law). Chapters 14–15 on **double proportionality** — being proportional across districts *and* parties simultaneously — are party-list machinery today, but they are the natural home for "proportional across geography *and* preference at once".

**In this repo:** [the math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md) · [what "proportional" actually means](../../03_STAR_PR/01_Learn/what_proportional_means.md) · [glossary — apportionment vocabulary](../GLOSSARY.md)

</td>
</tr>
</table>

---

## Where to go next

- The single-winner methods these systems are built from → **[Rated & score methods](rated_and_score_methods.md)** and [How to Learn About Voting Methods](../topics/how_to_learn_about_voting_methods.md).
- This repo's own proportional material → [proportional representation](../../03_STAR_PR/01_Learn/README.md).
- Back to the full shelf → **[Books on Voting Methods](README.md)**.
