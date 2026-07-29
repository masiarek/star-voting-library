# A blank is ranked LAST — and rank *numbers* don't matter

*The single most common Ranked Robin misconception, and the ballot-instruction ambiguity that feeds it. If you take one thing from this page: **Ranked Robin reads the preference ORDER on each ballot, never the numeric rank label.** A candidate you leave blank sits below everyone you ranked; whether you wrote your worst choice in the "last tier" or left them blank changes nothing.*

---

## The question (a real one)

It comes up every time a newcomer meets a Ranked Robin ballot with, say, five ranking bubbles:

> *"If I leave a candidate blank, are they ranked 5th, or 6th? The instructions say 'ranked last' — but which place is last?"*

And close behind it, the deeper worry:

> *"If one voter ranks a candidate 5th and another leaves them blank (6th), doesn't that give the 5th-place candidate a win over the blank one — just from the rank numbers?"*

Both questions dissolve once you see how the count actually works. (This is not hypothetical — it's the exact confusion, and its resolution, from an Equal Vote community thread. Worth teaching because *three* experienced advocates in that thread first assumed the ballot always has exactly five tiers. It doesn't.)

---

## Answer, part 1 — a blank is ranked below everything you ranked

A Ranked Robin ballot is just an instrument for capturing **one voter's order of preference**. "Ranked last" doesn't point at a specific bubble (5th, 6th, 100th) — it means *placed after every candidate you did rank*. Leave Cara and Dan blank, rank Ada and Ben, and your ballot says:

```
Ada = Ben  >  (everyone I ranked)  >  Cara = Dan
```

So a blank is a real signal: it ranks that candidate **below** all your ranked choices. The number on the last bubble is irrelevant — 5 tiers or 6 or as many as there are candidates, "blank" always means *under all of them*.

## Answer, part 2 — the count uses order, not rank numbers (this is **not** Borda)

Here's the misconception worth killing on sight. Ranked Robin is **not** [Borda](glossary_ranked_robin.md) — it does **not** add up rank *values*. A candidate does not earn "points" for sitting in a higher-numbered tier, and rank numbers **never** transfer between ballots.

What Ranked Robin actually does: for every **pair** of candidates, count how many voters rank A above B and how many rank B above A. Most head-to-head wins takes the seat (that's [Copeland](glossary_ranked_robin.md); ties broken by margin, then lot). See [Ranked Robin (the method)](ranked_robin.md).

So the "5th vs 6th" fear is a category error. Whether voter 1 writes their worst choice in the last tier or leaves them blank, that candidate lands **last on voter 1's ballot** either way — and contributes *identically* to every pairwise tally. The numeric gap between "5th" and "blank" is a distinction without a difference.

---

## See it run

Four candidates — **Ada, Ben, Cara, Dan** — three voters. **Dan is ranked explicitly last by voter 1, and left blank by voters 2 and 3.** Watch Dan get treated identically (dead last) either way:

- `Ada > Ben > Cara > Dan`   *(Dan written last)*
- `Ada > Cara > Ben`         *(Dan blank)*
- `Ben > Ada > Cara`         *(Dan blank)*

```
Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    2 – 1
   Ada   beats Cara   3 – 0
   Ada   beats Dan    3 – 0
   Ben   beats Cara   2 – 1
   Ben   beats Dan    3 – 0
   Cara  beats Dan    3 – 0

Win–loss record — Copeland score = wins + ½·ties:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        3–0–0         3      +7  Ben, Cara, Dan
    2  Ben        2–1–0         2      +3  Cara, Dan
    3  Cara       1–2–0         1      -1  Dan
    4  Dan        0–3–0         0      -9  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

Look at Dan's column: **"Ada beats Dan 3 – 0"** — *all three* voters are counted as preferring Ada to Dan, including the two who left Dan blank. Blank = below every ranked candidate, exactly as if written last. Dan loses every pairwise 3–0 and finishes last; Ada beats everyone (the [Condorcet winner](../../07_Concepts/GLOSSARY.md#properties-criteria)) and wins outright. The rank *numbers* never entered the arithmetic.

> Want the whole count? Full LH report → [`rr_blank_is_last_c4_b3_tabulated.txt`](../_main/cases/cases_tabulated/rr_blank_is_last_c4_b3_tabulated.txt) · source → [`rr_blank_is_last_c4_b3.yaml`](../_main/cases/rr_blank_is_last_c4_b3.yaml). Independently cross-checked with `pref_voting`'s Copeland (AGREE, unique winner).

---

## The one subtlety that *is* real — multiple blanks are **tied**

Ranking your single worst choice "last" and leaving them "blank" are the same. But leaving **two or more** candidates blank is **not** the same as ranking them in some order — the blanks are all **tied for last** with each other. Two blanks means neither beats the other; you cast a pairwise *tie* between them (an [Equal Support](../../07_Concepts/GLOSSARY.md) contest), not a preference. If you actually prefer one of your bottom two, you must rank them to say so.

That's the honest thing a ballot instruction has to convey: *blanks rank below everyone you ranked, and blanks tie each other.*

---

## So what should the ballot say?

The trap wording is anything tier-specific — **"ranked last (i.e. 6th)"** bakes in an assumption that the ballot has exactly five tiers. It doesn't have to: five bubbles is a common, tested default, but a Ranked Robin contest can offer four, six, or as many tiers as there are candidates. The moment the tier count differs, "6th" is wrong.

The universally-correct instruction is order-based, matching how the count works and how this repo already frames the no-preference bucket as **[Equal Support](../../07_Concepts/GLOSSARY.md)**:

> **Candidates left blank are ranked below all others (and tie one another).**

No tier number, so it survives any ballot and any contest — the same discipline that keeps our Equal Support legend from hard-coding a candidate count. (Equal Vote's own preference is poll-testing the exact public wording before adopting it; the principle above is what the wording needs to preserve.)

---

*See also: [Ranked Robin (the method)](ranked_robin.md) · [why it isn't Borda — the glossary](glossary_ranked_robin.md) · [Strict vs. weak ranks](../../07_Concepts/scores_and_ranks/strict_vs_weak_ranks.md) (why equal ranks / ties are first-class here) · [Summability](RCV_RR_summability.md). Up: [Ranked Robin concept pages](README.md).*

# file: rr_blank_means_last.md
