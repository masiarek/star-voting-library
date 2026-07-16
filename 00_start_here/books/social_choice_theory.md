# 🎓 Social choice theory — the impossibility results and the paradoxes

These are the books the whole field cites: *why* no voting method is perfect, proved rigorously. When someone says "no voting system is fair, so why bother?" — this shelf is where that claim comes from, and it says something more precise and more interesting than the slogan. The real lesson isn't "give up," it's "every method is a **trade-off**, so choose deliberately." Denser than the [popular introductions](popular_introductions.md); worth the climb.

← Back to [Books on Voting Methods](README.md)

---

<table>
<tr>
<td width="150" valign="top"><img src="img/social_choice_individual_values_arrow.jpg" width="130" alt="Cover of Social Choice and Individual Values by Kenneth Arrow"></td>
<td valign="top">

### Social Choice and Individual Values — Kenneth J. Arrow (1951; 2nd ed. 1963; 3rd ed. 2012)

The book that founded modern social choice theory and won a Nobel Prize. Arrow's **impossibility theorem**: no *ranked* voting method can satisfy a short list of obviously-reasonable fairness conditions at once. Slim and formal — you can read the key argument in an afternoon, and everything else on this shelf is a response to it.

**The lean:** Neutral and foundational; it sells no method. Note the crucial fine print this repo leans on: Arrow's theorem is about **ranked** ballots — *rated* methods like [score](../Range_Voting/range_voting.md) and [STAR](../STAR_Voting/STAR_start_here.md) sidestep it (they fall under the later Gibbard–Satterthwaite manipulation result instead, not this one).

**In this repo:** [Arrow's theorem](../GLOSSARY.md) (glossary) · [Gibbard–Satterthwaite](../topics/gibbard_satterthwaite_theorem.md) · [what makes a voting method good](../topics/what_makes_a_voting_method_good.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/collective_choice_social_welfare_sen.jpg" width="130" alt="Cover of Collective Choice and Social Welfare by Amartya Sen"></td>
<td valign="top">

### Collective Choice and Social Welfare — Amartya Sen (1970; expanded ed. 2017)

Another Nobel laureate's classic, and the most *humane* book on the shelf — Sen connects the formal theory to welfare, rights, and what it even means for a group to "prefer" something. The 2017 expanded edition roughly doubles the original with newer chapters. Alternating formal/informal chapters let you read it at the depth you want.

**The lean:** Scholarly and neutral on voting *rules*; Sen's interest is the philosophy of collective choice, not promoting a ballot. The best book here for *why the questions matter*, not just how the math works.

**In this repo:** [what makes a good winner](../topics/what_makes_a_good_winner.md) · [preference](../topics/preference.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/decisions_and_elections_saari.jpg" width="130" alt="Cover of Decisions and Elections by Donald Saari"></td>
<td valign="top">

### Decisions and Elections: Explaining the Unexpected — Donald G. Saari (2001)

The deeper companion to Saari's popular [*Chaotic Elections!*](popular_introductions.md). Same geometric toolkit, more thoroughly developed: how paradoxes arise, why aggregation is so slippery, and a fresh look at Arrow's and Sen's theorems.

**The lean:** Same as Saari's other work — brilliant on *why methods disagree*, but carries his **pro-Borda** thesis. Take the diagnosis (paradoxes are structural) more readily than the prescription (Borda solves them).

**In this repo:** [voting paradoxes](../voting_paradoxes/README.md) · [Borda](../other_ranked_methods/borda.md) · [Condorcet](../topics/condorcet/)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/social_choice_manipulation_taylor.jpg" width="130" alt="Cover of Social Choice and the Mathematics of Manipulation by Alan Taylor"></td>
<td valign="top">

### Social Choice and the Mathematics of Manipulation — Alan D. Taylor (2005)

The clearest book-length treatment of **strategic voting** and the Gibbard–Satterthwaite theorem: *every* reasonable method can sometimes be gamed by insincere voting. Written as an accessible undergraduate text, so it's the friendliest rigorous entry point to the manipulation results that apply to score and STAR.

**The lean:** Neutral textbook — it proves what can be manipulated, it doesn't sell a fix. Essential background for reading any "method X is strategy-proof" claim skeptically (none fully is).

**In this repo:** [strategic voting](../topics/strategic_voting.md) · [Gibbard–Satterthwaite](../topics/gibbard_satterthwaite_theorem.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><!-- cover pending: img/mathematics_of_social_choice_borgers.jpg — Open Library candidate: https://covers.openlibrary.org/b/isbn/9780898716955-M.jpg --></td>
<td valign="top">

### Mathematics of Social Choice: Voting, Compensation, and Division — Christoph Börgers (2010)

The gentlest *rigorous* book on the shelf — an undergraduate text (SIAM, from a Tufts course) that actually proves the things the others cite, in short chapters with exercises. Part I is the voting theory: Condorcet winners and cycles, Borda, IRV, and one of the few textbook-level treatments of the **[Smith set](../topics/smith_set.md)** — Börgers builds it as the "**generalized Condorcet candidates**," proving existence and uniqueness via nested dominating sets in a couple of pages you can follow with a pencil. Parts II–III widen out to fair division and apportionment.

**The lean:** Neutral textbook — it teaches the mathematics and sells no method. Its voting coverage is classical (ranked methods and their theory); rated methods like score and STAR aren't its subject, so read it for the Condorcet-family foundations, not a method comparison.

**In this repo:** [The Smith set](../topics/smith_set.md) · [the math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md) · [Condorcet](../topics/condorcet/)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/voting_paradoxes_nurmi.jpg" width="130" alt="Cover of Voting Paradoxes and How to Deal with Them by Hannu Nurmi"></td>
<td valign="top">

### Voting Paradoxes and How to Deal with Them — Hannu Nurmi (1999)

A field guide to the paradoxes themselves: Condorcet cycles, monotonicity failures, no-show paradoxes, and more — catalogued, illustrated, and cross-referenced against which methods suffer which. The book to keep at hand when a specific paradox comes up and you want it stated precisely.

**The lean:** Reference-neutral; Nurmi surveys rather than advocates. Pairs naturally with this repo's own [paradoxes collection](../../method_comparisons/paradoxes_and_whoops/README.md).

**In this repo:** [voting paradoxes](../voting_paradoxes/README.md) · [monotonicity](../topics/monotonicity/) · [participation](../topics/participation/) · [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md)

</td>
</tr>
</table>

<table>
<tr>
<td width="150" valign="top"><img src="img/collective_decisions_voting_tideman.jpg" width="130" alt="Cover of Collective Decisions and Voting by Nicolaus Tideman"></td>
<td valign="top">

### Collective Decisions and Voting — Nicolaus Tideman (2006)

*The Potential for Public Choice.* The most comprehensive single-author survey on the shelf — Tideman works through criteria, methods, and the design of collective decision procedures with unusual care about *what we should want* from them before asking which method delivers it.

**The lean:** Tideman invented **Ranked Pairs** (a Condorcet method), and the book leans toward Condorcet-consistent, criterion-driven design — a different destination from this repo's STAR. That makes it a valuable *opposing-camp* read: the strongest careful case for "get the Condorcet winner right." See also [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md), this repo's Condorcet method.

**In this repo:** [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) · [Condorcet](../topics/condorcet/) · [criteria at a glance](../topics/criteria_at_a_glance.md)

</td>
</tr>
</table>

---

## Where to go next

- The paradoxes, worked as runnable elections → [this repo's paradoxes collection](../../method_comparisons/paradoxes_and_whoops/README.md).
- The cardinal methods that route *around* Arrow → **[Rated & score methods](rated_and_score_methods.md)**.
- Softer landing → **[Popular introductions](popular_introductions.md)**.
- Back to the full shelf → **[Books on Voting Methods](README.md)**.
