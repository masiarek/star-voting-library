# The `brief` option — with and without

**One line:** `brief: true` strips the repetitive **`[STAR Voting: …]`** prefix from every section header, because the method is already named in the top banner. It changes only the *display* — every number is identical.

→ Up: [LH reporting options](options.md) · [How the LH engine reports](README.md) · hub: [STAR Reporting](../)

## The same election, both ways

A tiny 3-voter STAR election (Bo wins either way). The **only** difference is the section headers.

### `brief: false` — verbose (every header repeats the method)

```
--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Ada,Bo,Cy
  5, 3, 0
  4, 5, 1
  0, 2, 5
[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bo            -- 10 -- First place
   Ada           --  9 -- Second place
   Cy            --  6
 Bo and Ada advance.
[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bo            -- 2 -- First place
   Ada           -- 1
   Equal Support -- 0
 Bo wins.
[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bo
```

### `brief: true` — compact (the house default)

```
--- STAR Voting Method (single winner) ---
 Tabulating 3 ballots.
Ada,Bo,Cy
  5, 3, 0
  4, 5, 1
  0, 2, 5
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Bo            -- 10 -- First place
   Ada           --  9 -- Second place
   Cy            --  6
 Bo and Ada advance.
Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Bo            -- 2 -- First place
   Ada           -- 1
   Equal Support -- 0
 Bo wins.
Winner — STAR Voting Method (single winner)
 Bo
```

## Exactly what `brief` does to each header

| `brief: false` | `brief: true` |
|---|---|
| `[STAR Voting]` (a bare repeat of the banner) | *dropped* |
| `[STAR Voting: Scoring Round]` | `Scoring Round` |
| `[STAR Voting: Automatic Runoff Round]` | `Automatic Runoff Round` |
| `[STAR Voting: Winner — …]` | `Winner — …` |

The `[STAR Voting:` prefix is noise once you know the method — so `brief` removes the brackets and the prefix and suppresses the bare `[STAR Voting]` line. The rounds, scores, ballots, and winner are untouched.

## Which to use

- **On-screen report → `brief: true`** is the [house default](../../../CLAUDE.md) ("less is more"). It reads cleaner, especially when several elections scroll past.
- **`brief: false`** is occasionally handy when you want the section markers to be unmistakable machine-parseable `[...]` tags, or when teaching what the raw sections are called.
- **The `_tabulated.txt` mirror** ignores `brief` entirely and always renders full detail — so the saved audit copy never depends on this flag.
