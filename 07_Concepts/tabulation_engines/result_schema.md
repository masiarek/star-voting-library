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
  "schema_version": "1.1.0",
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

**What a fired rung looks like.** The lot is the rung this engine can always name, because `LotNumberTiebreaker` is the object that broke the tie and the builder reads its log rather than recomputing anything:

```json
{ "stage": "finalists", "tied": ["Arden", "Blythe", "Corin"], "at": 12,
  "rung": "lot", "advanced": ["Blythe", "Arden"], "eliminated": ["Corin"], "round": 1 }
```

That is [`b484mbm`](../../02_STAR_Bloc/02_Examples/cases/cases_pages/b484mbm_tie_every_rung.md) — three candidates, two seats, 12 = 12 = 12 and every deterministic rung level, so the lot filled both seats. `stage` says what the tie was *for*: `finalists` for a slot in the Automatic Runoff of a STAR round, `winner` for the seat itself — a runoff that tied, or, in the PR family, the round's weighted score total, which has no runoff anywhere on its path. `round` names the selection round for the methods that fill one seat per round (Bloc STAR, `allocated`, `sss`, `rrv`) and is absent for single-winner STAR, which has only one. `at` is the value they tied on wherever the builder holds that number and `null` where it does not: a PR round's weighted total is not recoverable without re-deriving the count, and inventing it would be worse than saying nothing.

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

**Copeland is `wins + ½·draws`.** Not raw wins. The two agree whenever every head-to-head is decided and come apart the moment one is drawn; ranking on raw wins can elect a candidate the table shows in third. **Know that this one is contested, though** — Ranked Robin's published definition is "elect the candidate who pairwise beats the greatest number of candidates," which counts wins alone, and its own worked example scores a three-wins-and-a-draw candidate as 3 rather than 3.5. Every implementation (this engine, BetterVoting, `pref_voting`) uses the half-point anyway, and so does this contract — but a conformance run against a spec-literal implementation would differ on who is *tied for the top*, before any tie-break rung is reached. The open question: [what counts as a win](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md#the-rung-below-the-ladder-what-counts-as-a-win).

**Tie-break ladders differ by engine, and that is data — but check yours against the published one first.** Ranked Robin has a tie-break protocol of its own, four rungs deep, and this engine follows the two rungs it recommends: a Copeland tie goes to the **1st Degree** (greatest sum of win margins over the *other finalists*), then the **2nd Degree** (the same sum over the whole field), then the published lot. BetterVoting implements the 1st Degree only when exactly two candidates are tied and sends any larger tie to a seeded shuffle. `tiebreaks[].rung` is free text for exactly this reason — a conformance run should compare the *tied set* and the *outcome*, and treat a differing rung name as a documented divergence rather than a failure. **A caution about stored fixtures:** until 2026-08-19 this engine had no 1st Degree rung at all and ranked ties by total margin over the whole field — the 2nd Degree applied in place of the first. Correcting it changed the winner on 11 of this library's 100 Ranked Robin cases, so any result captured before that date is stale rather than divergent. The ladder, both bugs, and the eleven cases: [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md). And Ranked Robin is only the worked example — every method's ladder, on every engine this library reaches, is stated side by side in [tiebreak_ladders.md](tiebreak_ladders.md).

**Two Droop quotas.** STV here uses the exact `votes/(seats+1)`; the Irish/Scottish hand-count rule is `floor(votes/(seats+1)) + 1`, one vote higher. `rounds.quota` names which one produced the count.

## Versioning

`schema_version` is the version of **this contract**, not of any engine. Patch means wording. Minor means a field was **added** — a stored fixture must keep validating across a minor bump, which is the whole point of publishing the number. Major means a field was removed or its meaning changed, and your reader breaks.

**1.1.0 (2026-08-21)** is so far the only bump. `tiebreaks[]` gained the optional `round` field — the additive half — and, the half that matters, the score path began reporting the **lot** rung at all. Before it, the only tie the builder could see was the finalists ladder that `resolve_finalists()` replays for single-winner STAR, so a Bloc or PR seat bought by lot, and a single-winner Automatic Runoff bought by lot, both emitted `tiebreaks: []` — which point 4 above defines as the positive claim that the ballots alone decided. **23 cases in this library made that claim falsely**, among them `lot_tiebreak_published_order.yaml` and the whole [dead-rung set](../../01_STAR/03_Criteria/tie_break_dead_rung/README.md), whose entire subject is the lot. Any result captured before that date is stale rather than divergent, exactly like the Ranked Robin fixtures above: re-emit it before reading a difference as a disagreement.

`source.sha256` hashes the exact bytes counted. Two results are comparable only when it matches; it is what stops a stale fixture from being read as a disagreement.

## What is still missing

Stated plainly, because a conformance suite that oversells itself is worse than none:

- **48 ballot-carrying cases have no answer key** (615 total, 567 answered). They emit results; `result.matches_expected` is `null` rather than `false` — *we did not check* must not read as *we checked and it passed*.
- **Six methods in the repo are out of scope for this engine** — Range at 0–9, CAV, 3-2-1, and the [grade methods](../../06_Other/Majority_Judgment/README.md) — and are refused with an `UnsupportedMethod` error rather than answered. They are counted elsewhere in the repo; they are not part of this contract yet.
- **Below the lot, a multi-winner count's ladder is invisible.** `tiebreaks` names every tie the *lot* settled, on every seat; for single-winner STAR it also names the rung that settled the finalists — `head-to-head` or `five-star` — because `resolve_finalists()` replays that ladder against starvote's own round functions. There is no equivalent replay for a Bloc STAR round or a PR round: those rungs run inside starvote's counting functions, which report nothing back, and rebuilding them in the builder would mean re-deriving the count, which this contract does not do anywhere. So a Bloc seat settled at the five-star rung still reads here as a seat nothing was broken for. It is the one remaining way the array can understate what happened.
- **There is no executable specification.** The rules are still distributed across concept pages and engine source, so an implementation currently has to be written from the cases plus prose. That is [D1 of the reference package](star_reference_package.md), and it is the next thing that matters.
- **The input format has no published schema.** This contract covers the *result*; the *case file* is still validated by hand-rolled checks — including a [genuine YAML typing hazard](star_reference_package.md#3-but-yamls-implicit-typing-is-a-genuine-certification-context-hazard) where an unquoted `No` on a ballot measure parses as `False`. Pydantic models would close that and emit the input schema, and it is the same day's work.

## What checks this page

[`tests/test_result_json.py`](../../STARVote_LH_tabulation_engine/tests/test_result_json.py) runs the whole corpus through the builder on every commit: every case validates against the published schema, every answer key is met through the JSON path specifically, the runoff funnel reconciles, every `[Tiebreaker: Lot Number Priority]` banner the printed report shows has exactly one matching `rung: "lot"` entry in the JSON — no more, so the finalists replay cannot double-count a banner it shares, and no fewer — `--json` stays pure, and an unsupported method is refused rather than guessed at. A schema nothing checks is documentation, not a contract.

*Up: [Tabulation engines](README.md) · the wider plan: [the STAR reference package](star_reference_package.md) · why this is the highest-leverage piece: [Rust kernel requirements, G6](rust_kernel_requirements.md).*
