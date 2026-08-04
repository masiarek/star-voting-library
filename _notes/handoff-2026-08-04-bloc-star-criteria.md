# Handoff — Bloc STAR criteria session, 2026-08-04

Written at a machine switch. Everything below is **committed and pushed**; nothing of
this work lives only in a scratch directory. Not site content (`/_notes` is excluded in
`mkdocs.yml`). Delete this file once the open items are picked up.

## What shipped

**A new folder, [`02_STAR_Bloc/03_Criteria/`](../02_STAR_Bloc/03_Criteria/README.md)**, mirroring `01_STAR/03_Criteria` — three criteria the Bloc folder had prose about but no runnable elections for:

| Set | Elections | The finding |
|---|---|---|
| [participation](../02_STAR_Bloc/03_Criteria/participation/README.md) | BV2264 [`j3hqvb`](https://bettervoting.com/j3hqvb/results) · BV2265 [`th3pbp`](https://bettervoting.com/th3pbp/results) | A seventh voter votes honestly and gets a council worth **3** on their own ballot where staying home was worth **5** — their support pushed their favourite into the seat-2 runoff, and the candidate they scored 0 won it. |
| [seat order](../02_STAR_Bloc/03_Criteria/seat_order/README.md) | BV2266 [`k7pfqt`](https://bettervoting.com/k7pfqt/results) | Anika beats every rival head to head (4–2, 5–2, 4–3) and is seated **second**. At one seat these same ballots elect Dev outright, so the second seat is what rescues her — that honest half is on the page. |
| [committee spoiler](../02_STAR_Bloc/03_Criteria/committee_spoiler/README.md) | BV2267 [`my9jd9`](https://bettervoting.com/my9jd9/results) · BV2268 [`6m3gxq`](https://bettervoting.com/6m3gxq/results) | Adding Dane, who wins nothing, swaps Ari off the council for Bea. No Condorcet cycle needed, unlike the single-winner IIA case. |

**All five BV elections reproduce the LH count exactly** — same winners, same seat order, every ballot counted, `tieBreakType: none` at every seat. Frozen exports sit beside each yaml; the tabulations were re-verified against the live `/API/ElectionResult` endpoint after minting.

Also pushed: the scenario list this came from ([`todo-bloc-star-scenarios.md`](todo-bloc-star-scenarios.md), items §2.1–2.3 now closed out), the search tool behind it ([`find_bloc_criteria_profiles.py`](../STARVote_LH_tabulation_engine/tools_adam/find_bloc_criteria_profiles.py)), regenerated `BV_registry` / `PARADOX_index` / `bv_cases.csv`, and a link to the new folder from the Bloc README's learning path.

## Open, in the order I'd take them

1. **§2.4 of the scenario list — the degenerate seat-count probe, deliberately NOT minted.** 3 candidates / 3 seats: the LH engine refuses it, and the open question is whether BetterVoting accepts a race nobody can lose. Asking it means creating a permanent, undeletable public election whose title has to describe a degenerate contest — **your call, not a default.** Everything else about the item is settled; only the mint is pending.
2. **§3.1 monotonicity — settle it rather than search it.** ~377,000 tie-free profiles produced no failure, and the two-seat case looks provable; the argument is written out in the tool's docstring. What is missing is the N-seat half. A proof turns this from a gap into a property the folder can *state*, which is worth more than another case.
3. **Tag the older Bloc yamls with `paradoxes:`.** The four new cases carry `no-show` / `spoiler-scc` (168 tagged cases now, up from 164), but BV1525 and BV1835 are still bare. Vocabulary is hyphenated — `condorcet-loser`, `absolute-loser`. BV2266 is untagged on purpose: `condorcet-winner` means the Condorcet winner is *not elected*, and Anika is elected, just second.
4. **`01_Learn/README.md` does not link the new folder yet** (the folder README and the Bloc README both do), and the prose page the criteria imply — *"what Bloc STAR keeps and what it drops"* — is still owed.

## Two things worth knowing before you touch this again

- **Another Claude session was working in this same clone all afternoon** (Ranked Robin pages, the `starvote` engine, the vote-splitting page, and its own BV mint BV2263 `xw23m9`). Its work is committed too, and the tree was clean at handoff — but that is why my mint ran from a standalone driver instead of the shared `bv_election_specs.ELECTIONS` list, and why the indexes were regenerated in a throwaway `git worktree` at HEAD. A crossed `ELECTIONS` pointer creates permanent elections nobody asked for, and regenerating indexes over someone else's untracked case links the site at a page that does not exist.
- **The mint order is not optional.** BV descriptions are permanent and cannot be edited, and the house rule is that each election's description backlinks to its lesson page. So the pages went up *first*, I waited for the Pages deploy, and `--dry-run` confirmed every backlink at HTTP 200 before anything was created. The backlinks point at each criterion folder's `index.html` (mkdocs maps `README.md` → `index.html`), **not** at a case page — case filenames carry the bvid, which does not exist until after the mint, so a case-page backlink would have been a chicken-and-egg 404.

## Reproducing the profiles

Stdlib only, no venv:

```bash
python3 STARVote_LH_tabulation_engine/tools_adam/find_bloc_criteria_profiles.py participation -v 6 --seed 2 --hits 1
```

The tool re-derives the shipped ballots exactly (the candidates were renamed on promotion from letters). Its docstring carries the other two commands and the monotonicity argument.
