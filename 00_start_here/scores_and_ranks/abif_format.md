# ABIF — the all-in-one ballot format (and why this library authors in a grid instead)

*You may run into **ABIF** — the Aggregated Ballot Interchange Format — in the election-methods world. It's an ambitious, genuinely clever format: **one grammar** that writes a [score ballot](score_ballot.md) (STAR), a [ranked ballot](ranked_ballot.md) (RCV-IRV), an approval ballot, and everything in between. It also looks, on first read, like line noise — `Allie/5 =Billy/5 >Candace/4`. This page decodes the beast, shows the exact same election in ABIF and in this library's YAML grid, and weighs the two honestly. Short version: ABIF is a superb **interchange** format and an awkward **authoring** one — which is why we teach in a grid and would only ever meet ABIF at the import/export door.*

→ Companions: [The score ballot](score_ballot.md) · [The ranked ballot](ranked_ballot.md) · [Scores vs. ranks](scores_vs_ranks.md) · the notation table in [score_ballot.md](score_ballot.md#writing-it-down-the-grid-and-why-not-to-read-it-by-columns).

---

## What it is, and where it comes from

ABIF was designed by **Rob Lanphier** (`robla`) under the [electorama](https://electorama.com) umbrella, with a published spec ([electowiki](https://electowiki.org/wiki/ABIF)), a reference toolchain (`abiftool`), and a live editor at [abif.electorama.com](https://abif.electorama.com). Its stated job: *"a concise, aggregated, text-based document to describe the ballots cast in range-based or ranked elections, as well as approval-based and choose-one balloting systems."*

That "as well as" is the whole point. The **same** set of voter opinions can be tabulated by STAR, RCV-IRV, [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md), Approval, or Condorcet — and ABIF's ambition is to be the one file all of those tools read, so you can hold the voters constant and swap the method. (That is exactly Lanphier's [Tennessee example](https://abif.electorama.com/id/TNexampleSTAR), the same "three methods, three winners" puzzle this repo tells in [BV2155](../../method_comparisons/paradoxes_and_whoops/bv2155_cphxpt_tennessee_four_ways.md).)

## The grammar, decoded

A `.abif` file is a few kinds of line:

- **`#`** starts a comment; **`{ … }`** carries metadata (title, candidate list) in a JSON-ish block.
- A **vote line** is one ballot pattern: an optional **count prefix** — an integer then `:` or `*` — followed by candidate **tokens** joined by **operators**.
- A **token** is a candidate name with an optional **rating**: `Allie/5`. Names with spaces get `[square brackets]` or `"quotes"`.
- The **operators between tokens** are the load-bearing idea:
  - **`>`** — the previous candidate is *preferred over* the next (a strict rank step).
  - **`=`** — the previous candidate is ranked *equal to* the next.
  - **`,`** — the candidates are simply *listed*, no order asserted (used for pure score/approval ballots).

Here is the file from the screenshot, `testfiles/test003.abif`, line by line:

```abif
# Case 3 — Scores using = and > as delimiters
12: Allie/5 =Billy/5 >Candace/4 >Dennis/3 =Edith/3 >Frank/2 >Georgie/1 >Harold/0
 7: Georgie/5 >Allie/4 >Dennis/3 =Harold/3 >Candace/2 >Edith/1 >Billy/0 =Frank/0
 5: Frank/5 >Edith/4 =Harold/4 >Billy/3 =Dennis/3 =Georgie/3 >Candace/2 >Allie/0
```

Read the first vote line as a sentence:

> **12** voters cast this ballot: **Allie** a 5, **Billy** a 5 *and tied with Allie* (`=`), **Candace** a 4 *and below Billy* (`>`), Dennis a 3, Edith a 3 *tied with Dennis* (`=`), Frank a 2, Georgie a 1, Harold a 0.

Notice what's happening: **the operator sits in front of the candidate it introduces and states that candidate's relation to the one before it.** `Allie/5 =Billy/5` means "Billy, equal to Allie." `Billy/5 >Candace/4` means "Candace, ranked below Billy."

## The three faces — and the confusing one

Because ranks and scores are both first-class, ABIF has three registers:

| Register | Looks like | This is a… |
|---|---|---|
| **Ranked** (order only) | `Allie > Billy = Candace > Dennis` | [RCV-IRV](../RCV_IRV/RCV-IRV-Hare.md) / Ranked Robin ballot |
| **Rated** (strength only) | `Allie/5, Billy/5, Candace/4, Dennis/3` | [STAR](../STAR_Voting/STAR_start_here.md) / Score / Approval ballot |
| **Hybrid** (both at once) | `Allie/5 =Billy/5 >Candace/4` | scores **and** explicit operators — `test003` above |

The first two are clean. The **hybrid** is what tripped you up, and the confusion is legitimate: it encodes the ordering **twice** — once in the numbers (`5`, `5`, `4`) and again in the operators (`=`, `>`). In `test003` the two agree by construction (every `=` sits between equal scores, every `>` between descending ones), so it's a tidy belt-and-suspenders demo. But nothing in the *syntax* forces agreement — `Allie/5 >Billy/6` is writable, and now the operator says "Allie beats Billy" while the scores say the opposite. A reader (or parser) has to know which wins. **Two sources of truth for one fact is a footgun**, and the hybrid form is where ABIF looks most like line noise for the least added information.

## The same election, both ways

Here is `test003` exactly, rewritten in this library's YAML grid — the [format you're proposing as the house standard](score_ballot.md#writing-it-down-the-grid-and-why-not-to-read-it-by-columns):

```yaml
ballots: |
  Allie, Billy, Candace, Dennis, Edith, Frank, Georgie, Harold
  12 × 5, 5, 4, 3, 3, 2, 1, 0
   7 × 4, 0, 2, 3, 1, 0, 5, 3
   5 × 0, 3, 2, 3, 4, 5, 3, 4
```

Same 24 ballots, same scores, same everything — it tabulates identically. Put the two side by side and the trade is visible at a glance:

- **ABIF** repeats the candidate names on every line and threads `>`/`=`/`/` through them; each line is a self-contained sentence.
- **The grid** names the candidates **once** in a header and lets every ballot be a plain row of numbers you could type in a spreadsheet.

## Pros and cons, honestly

**Where ABIF wins**

- **Self-describing lines.** The candidate's name rides *with* its score, so there's no header-to-row coupling — you cannot silently corrupt a ballot by reordering or misaligning a column. (That's precisely the "don't read the grid by columns" trap the grid *can* fall into.)
- **One grammar for every method.** Ranks, scores, equal-ranks, approval — all in a single file, so you can hold the voters fixed and run STAR, RCV-IRV, Ranked Robin, and Condorcet off the *same* source. For method *comparison*, that's the dream.
- **Order is explicit.** For ranked methods, `>` and `=` state the preference directly; you never infer it by doing arithmetic on scores.
- **It's a real standard.** A spec, a reference parser, a web tool, and community use — it round-trips between third-party programs. That's what "interchange" buys you.
- **Equal ranks are native.** `=` handles ties cleanly, a chronic sore spot in other ranked formats.

**Where ABIF hurts**

- **Punctuation density.** `/`, `>`, `=`, `:` all in one line is a steep first read — your reaction is the common one, and the hybrid form is the worst offender.
- **Redundancy you can contradict.** As above: scores *and* operators encode order twice, so a file can disagree with itself and a parser must define who wins.
- **Not spreadsheet-native.** You can't open it as columns, sort it, or eyeball one candidate's column. Editing is text-surgery, not grid-editing.
- **Names repeat on every distinct line** — more to type, more to fat-finger (weighting mitigates it, not eliminates it).
- **A learning curve** for exactly the audience this library serves — voters and students already fluent in spreadsheets, not in a mini-language.

**Where the YAML grid wins (and where it doesn't)**

- **Spreadsheet-native and low-punctuation.** Header names the cast once; each row is one ballot; anyone who's used Sheets can read and edit it. Scores need only commas. YAML wraps the method, seats, and reporting options around it cleanly.
- **But it's positional.** The header and the rows are *coupled* — a misaligned or reordered row is silently wrong, the one failure mode ABIF's self-describing lines don't have.
- **And it's two sub-notations**, not one: a grid for scores, `A>B>C` for ranks. ABIF unifies both under a single grammar; the grid keeps them separate (which is arguably *clearer* for teaching, at the cost of universality).
- **It's a house convention, not a community interchange spec.** YAML itself is universal; the ballot-grid *semantics* are ours.

## The verdict

They're optimized for **different jobs**, and "which is better" is really "better at what":

- **ABIF is an interchange format** — tool-to-tool, one grammar for all methods, self-describing, order-explicit. Its density is the *price of universality*, and for holding voters constant across methods it's excellent. The hybrid `/` + `>`/`=` form, though, is a genuine design smell, not just unfamiliarity — avoid authoring in it.
- **The grid is an authoring and teaching format** — spreadsheet-native, minimal punctuation, human-first. Its positional coupling is the *price of simplicity*.

So: keep the grid as this library's authoring standard, and treat ABIF the way we already treat [BetterVoting's JSON](../tabulation_engines/bettervoting_and_the_engine.md) — a format to **import from and export to**, not to hand-write lessons in. An ABIF↔grid converter would be a natural companion to the [JSON→YAML converter](../../STARVote_LH_tabulation_engine/tools_adam) the repo already ships; it would let us pull in the electorama test corpus and re-tabulate it with the LH engine. "Getting used to" ABIF is real and worth doing if you work across tools — but your instinct that the grid reads more easily for *teaching* is also correct. Different beast, different pasture.

## Related

- [The score ballot](score_ballot.md) — the grid, and the equivalent notations (`{A:5}`, `A=5`, `A[5]`), including where ABIF's slash fits
- [The ranked ballot](ranked_ballot.md) — order-only ballots, the `A>B>C` half of ABIF
- [Scores vs. ranks](scores_vs_ranks.md) — why order and strength are different data, the distinction ABIF spans
- [BetterVoting and the LH engine](../tabulation_engines/bettervoting_and_the_engine.md) — the other real-world ballot format the repo imports from
