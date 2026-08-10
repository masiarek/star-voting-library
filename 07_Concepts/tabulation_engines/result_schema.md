# The result contract — running your own engine against this library

**Level: reference · deep dive**

**One line:** every case file in this library can be counted into one versioned JSON object, so checking a second implementation is a `diff` rather than a reading exercise.

This page is addressed to **implementers** — someone writing a tabulator in Rust, TypeScript, Go, or Python who wants to know whether it is right. Everything else in this repo is written for learners; this is the door for the other audience. If you are here to understand STAR itself, start at [01_STAR](../../01_STAR/README.md) instead.

## What this library gives you

**615 election files, 567 of them carrying a machine-checkable answer key**, already cross-verified across six independent engines — [the LH `starvote` fork](LH_starvote/README.md), [BetterVoting](BV/README.md), [`pref_voting`](cross_checking_with_pref_voting.md), [`pyrankvote`](RCV_IRV/README.md), [RCTab](rctab.md), and [rcv-lab.org](rcv_lab_irv_crosscheck.md). As far as this repo knows, that is the largest cross-verified STAR corpus anywhere.

Until now it was only usable from inside: the answer keys pin the **winner and nothing else**, and every cross-check was wired here by hand against printed text. An engine could get all 567 winners right by the wrong path — right answer, wrong scoring round, wrong finalists, a tie broken at a rung it should never have reached — and nothing would catch it. The result contract is what closes that.

## Emitting a result

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py <case.yaml> --json
```

JSON on stdout and nothing else — no report, no `_tabulated` mirror written as a side effect. From Python, `result_json.build(path)` returns the same object as a dict.

Here is a whole result, for the [Tennessee capital](../../01_STAR/02_Examples/cases/cases_pages/09_c4_b100_tennessee-capital.md) case. The `pairwise` block is the only thing cut, for length:

```json title="Abridged for the lesson — the pairwise matrix is omitted"
{
  "$schema": "https://masiarek.github.io/star-voting-library/STARVote_LH_tabulation_engine/star_result.schema.json",
  "schema_version": "1.0.0",
  "source": {
    "file": "09_c4_b100_tennessee-capital.yaml",
    "sha256": "356c519bd232dc0484f1574dffc3be3342083c30ad8b4ddc9d026df82f4c58e1"
  },
  "election": {
    "title": "Tennessee Capital — classic STAR example",
    "declared_method": "STAR",
    "method": "star",
    "family": "score",
    "seats": 1,
    "candidates": ["Memphis", "Nashville", "Chattanooga", "Knoxville"],
    "ballots_cast": 100,
    "max_score": 5,
    "lot_order": null
  },
  "result": {
    "winners": ["Nashville"],
    "expected_winners": ["Nashville"],
    "matches_expected": true
  },
  "rounds": {
    "scoring": [
      { "candidate": "Nashville", "value": 394 },
      { "candidate": "Chattanooga", "value": 373 },
      { "candidate": "Memphis", "value": 326 },
      { "candidate": "Knoxville", "value": 307 }
    ],
    "finalists": ["Nashville", "Chattanooga"],
    "runoff": {
      "finalists": [
        { "candidate": "Nashville", "preferred_by": 68 },
        { "candidate": "Chattanooga", "preferred_by": 32 }
      ],
      "equal_support": 0,
      "decided_voters": 100,
      "ballots_cast": 100,
      "majority": 51,
      "tied": false
    }
  },
  "tiebreaks": [],
  "engine": { "name": "starvote_larry_hastings", "starvote_version": "2.1.6" }
}
```

The machine-readable schema is [`star_result.schema.json`](../../STARVote_LH_tabulation_engine/star_result.schema.json) (JSON Schema draft 2020-12), and the builder is [`result_json.py`](../../STARVote_LH_tabulation_engine/result_json.py).

## What a pass means

An implementation **conforms on a case** when its result:

1. **validates** against the published schema;
2. agrees on `result.winners`, in order;
3. agrees on every `rounds` value the method actually uses;
4. agrees on `tiebreaks` — including its being **empty**.

Point 4 is the one that does the work the answer keys could not. An empty `tiebreaks` array is a positive claim: *the ballots alone decided this, no rung fired.* An engine that reaches for a tie-break where the reference did not has a bug even when it lands on the same winner — and that is precisely the bug a winner-only comparison cannot see.

Point 3 is scoped to the method on purpose. A Bloc STAR count has no Automatic Runoff, so `rounds.runoff` is absent rather than zero: reporting a number the method never computed is worse than reporting nothing.

## The six families

`election.family` fixes which `rounds` keys are present. The alias table that maps a file's `voting_method:` onto a family lives in **one** place — `classify_method()` in [`starvote_larry_hastings.py`](../../STARVote_LH_tabulation_engine/starvote_larry_hastings.py) — and both the CLI's dispatch and this contract read it, so they cannot drift apart.

| `family` | Methods | `rounds` keys |
|---|---|---|
| `score` | STAR, Bloc STAR, `sss`, `rrv`, `allocated` | `scoring`; plus `finalists` + `runoff` for single-winner STAR |
| `approval` | Approval, Approval_Multi_Winner | `approval`, `abstentions` |
| `plurality` | Choose-One, SNTV, Block, Limited | `votes`, `variant`, `votes_per_voter`, `overvotes` / `abstentions` |
| `ranked_robin` | Ranked Robin / RCV-RR / Copeland | `record`, `smith_set` |
| `irv` | RCV-IRV | `irv_rounds`, `elimination_order`, `ballot_source` |
| `stv` | STV | the above, plus `quota` |

## Five places implementations legitimately differ

These are the ones worth reading before you conclude your engine is wrong. Each is a real divergence this library has hit.

**The runoff denominator.** `majority` is a strict majority of the **decided voters** — those who expressed a preference between the two finalists — not of ballots cast. `decided_voters + equal_support == ballots_cast` always holds, so the arithmetic reconciles on the page. Quoting a winner's share of *all* ballots is the standard way to overstate a STAR result.

**Single- versus multi-winner Choose-One are different rules.** Single-winner spoils an overvote: a ballot marking two candidates counts for nobody. Multi-winner counts every mark, because the paper is a block or limited ballot. Deriving one from the other elects the wrong slate — it did, on five block-voting cases here, until this contract was built off the engine's own tallies.

**Copeland is `wins + ½·draws`.** Not raw wins. The two agree whenever every head-to-head is decided and come apart the moment one is drawn; ranking on raw wins can elect a candidate the table shows in third.

**Tie-break ladders differ by engine, and that is data.** The LH engine breaks a Copeland tie by total margin, then by the published lot; BetterVoting breaks it head-to-head, then by a seeded shuffle. Both are defensible. `tiebreaks[].rung` is free text for exactly this reason — a conformance run should compare the *tied set* and the *outcome*, and treat a differing rung name as a documented divergence rather than a failure.

**Two Droop quotas.** STV here uses the exact `votes/(seats+1)`; the Irish/Scottish hand-count rule is `floor(votes/(seats+1)) + 1`, one vote higher. `rounds.quota` names which one produced the count.

## Versioning

`schema_version` is the version of **this contract**, not of any engine. Patch means wording. Minor means a field was **added** — a stored fixture must keep validating across a minor bump, which is the whole point of publishing the number. Major means a field was removed or its meaning changed, and your reader breaks.

`source.sha256` hashes the exact bytes counted. Two results are comparable only when it matches; it is what stops a stale fixture from being read as a disagreement.

## What is still missing

Stated plainly, because a conformance suite that oversells itself is worse than none:

- **48 ballot-carrying cases have no answer key** (615 total, 567 answered). They emit results; `result.matches_expected` is `null` rather than `false` — *we did not check* must not read as *we checked and it passed*.
- **Six methods in the repo are out of scope for this engine** — Range at 0–9, CAV, 3-2-1, and the [grade methods](../../06_Other/Majority_Judgment/README.md) — and are refused with an `UnsupportedMethod` error rather than answered. They are counted elsewhere in the repo; they are not part of this contract yet.
- **There is no executable specification.** The rules are still distributed across concept pages and engine source, so an implementation currently has to be written from the cases plus prose. That is [D1 of the reference package](star_reference_package.md), and it is the next thing that matters.
- **The input format has no published schema.** This contract covers the *result*; the *case file* is still validated by hand-rolled checks — including a [genuine YAML typing hazard](star_reference_package.md#3-but-yamls-implicit-typing-is-a-genuine-certification-context-hazard) where an unquoted `No` on a ballot measure parses as `False`. Pydantic models would close that and emit the input schema, and it is the same day's work.

## What checks this page

[`tests/test_result_json.py`](../../STARVote_LH_tabulation_engine/tests/test_result_json.py) runs the whole corpus through the builder on every commit: every case validates against the published schema, every answer key is met through the JSON path specifically, the runoff funnel reconciles, `--json` stays pure, and an unsupported method is refused rather than guessed at. A schema nothing checks is documentation, not a contract.

*Up: [Tabulation engines](README.md) · the wider plan: [the STAR reference package](star_reference_package.md) · why this is the highest-leverage piece: [Rust kernel requirements, G6](rust_kernel_requirements.md).*
