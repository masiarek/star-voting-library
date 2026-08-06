---
name: bettervoting
description: BetterVoting (BV) rules for this repo — minting/fetching BV elections via the API scripts, BV case-file and screenshot naming, the permanent-title/backlink/BV-number gotchas, the BV_registry, BV's voting-method strings and bloc multi-winner, and the end-to-end workflow for building a BV-backed test case. Use whenever a task touches BetterVoting, a bvid, create_bv_test_election.py, fetch_bv_export.py, bv_election_specs.py, or a _bv_export.json.
---

# BetterVoting (BV) — repo rules and workflow

Loaded on demand. The rest of the house style lives in `CLAUDE.md`; this file holds
only what is BV-specific, so non-BV sessions don't pay for it.

## BV conventions

- **BV screenshots live in the case folder's `img/` subfolder, prefixed with the
  BetterVoting election ID** — `img/<bv_id>_<what>.png` (e.g.
  `img/r2pvc9_result_bars.png`, `img/r2pvc9_runoff_pct.png`, `img/r2pvc9_runoff_pie.png`,
  `img/r2pvc9_race_details.png`). The id prefix keeps images traceable and collision-free;
  the `img/` subfolder keeps the lesson folder uncluttered. (PyCharm pastes generic
  `img_N.png` into the folder root; **move into `img/` and rename** to this convention
  when incorporating the case, and give each image a descriptive caption.)
  - **Don't screenshot by hand — use `tools_adam/bv_result_screenshot.py`** (headless
    Chrome over the DevTools Protocol; PEP 723, so `uv run` needs no venv). It clips to
    the actual result card, so the shot has no nav bar or footer and needs no cropping:
    `uv run …/bv_result_screenshot.py <bvid> --shot result -o <case>/img/<bvid>_result.png`.
    Presets: `result` (winner headline + chart), `race-details` (expands the accordion
    and grabs the table), `chart`, `page`; or pass your own `--clip` / `--prep`. The
    script's docstring documents the two traps (never `captureBeyondViewport` — it
    restarts the chart animation and shoots empty bars; a random-tiebreak result won't
    contradict the frozen export — BV's "random" rung is a **seeded** shuffle, so it
    re-tallies to the same order, see the tiebreak note in step 5).
  - **Embed with a sized `<img>`, not a bare `![]()`** — house style, so the picture
    doesn't render full-bleed: `<img alt="…" src="img/<bvid>_result.png" width="640">`.
    Rough widths: screenshot ≈640, panel ≈420, full ballot ≈460. Keep the PNG itself
    around 1400–1600 px wide (`magick shot.png -resize 1600x -strip shot.png`).
  - **Never leave a `REPLACE_*` placeholder pointing at an image you didn't capture** —
    it renders as a broken image on the website and warns on every docs build. Either
    take the shot or comment the reference out (a commented-out slot is inert).
- **BV-backed teaching cases (e.g. the Runoff Reversal set) → `Runoff_NN_<descriptor>_<bvid>`.**
  Zero-padded sequence (`Runoff_01`, `Runoff_02`, …) for sort order + the teaching
  progression, a short descriptor, and the BetterVoting election id as the final suffix
  for traceability. Each case is a trio: the **two-view lesson** `…_<bvid>.md` (View 1 =
  BetterVoting screenshots, View 2 = the LH text report, plus the ballots), the
  tabulatable `…_<bvid>.yaml`, and the frozen `…_<bvid>_bv_export.json`. Filenames carry
  the order/meaning; the BV id lives on the images, in the filename suffix, and in the
  YAML (`election_description` + the results URL).
- **Case-file naming.** Two accepted forms; the **bvid is the load-bearing id**
  (unique, stable, traceable by construction — no assignment step needed):
  - **If the election already has a sheet Test ID** (e.g. the older QA rows —
    `bv95a`, `bv130`, `bv1525`), lead with it: `bv<testid>_<bvid>_<descriptor>`
    (e.g. `bv95a_9m6rxr_favorite_survives.yaml`). It sorts with the (retained) QA
    sheet and is findable by ID.
  - **Otherwise (a fresh case with no pre-assigned Test ID)** — DON'T stop to
    assign one; lead with the bvid: `b<bvid>_<descriptor>` (e.g.
    `b26khr3_nota_wins`). The auto-generated repo registry indexes it either way.
  - **LH-only** reference (no BV election) → omit the bvid segment, descriptive name.
  - **One election backing SEVERAL cases (a multirace set) → descriptive names**
    (Adam, 2026-08-05). The bvid leads because it *discriminates*; when every
    file in the set would carry the same one it discriminates nothing, and it
    buries the reading order that makes the set legible. Put the linkage in the
    `bv_test_id` / `bv_election_id` / `bv_results_url` fields — what
    `build_bv_registry.py` actually reads — and the whole set still indexes and
    appears in `multirace_elections.md` correctly. Live example: the six cases of
    **BV2275** (`6mcgkq`) in `method_comparisons/kim_ordinal_vs_cardinal/`, one
    per race. **Don't re-align these to bvid prefixes.**

  Applies to the whole case group — `.yaml`, two-view `.md`, frozen
  `_bv_export.json`, `_tabulated` mirror. Older cases keep their names; re-align
  only if you're already touching them.
- **Every BV-backed case `.md` links the live BetterVoting results — clickably.**
  When a case has a real BV election, its page must carry a prominent, clickable
  link to the **results** page near the top (not just the bare election id, and
  not only the vote page). House form is a lead line right under the H1/summary:
  `**▶ Live on BetterVoting:** [vote](https://bettervoting.com/<bvid>) ·
  **[results ↗](https://bettervoting.com/<bvid>/results)** (election \`<bvid>\`).`
  Always link `/<bvid>/results` (the tabulated outcome), and mirror it in the YAML
  (`election_description` / a `Live results:` line pointing at the same
  `/results` URL). LH-only references with no BV election skip this.
- **The reverse link too — every NEW BV election's *description* points back at the
  repo teaching page (BV → repo).** The repo→BV direction (above) is only half the
  loop; a voter who lands on a public BV election should be able to click through to
  the lesson. So the `description` you pass to the create script must end with the
  case's **public site URL**:
  `Full lesson & tabulation: https://masiarek.github.io/star-voting-library/<page path>.html`
  where `<page path>` is the generated page's repo-relative path with `.md`→`.html`
  (the site is `use_directory_urls: false`, so paths map 1:1) — e.g.
  `…/06_Other/ballot_style_lab/cases/cases_pages/05_c3_b38_squeeze-survives.html`.
  **This MUST be set on the first create — BV descriptions are PERMANENT and CANNOT be
  edited via the API afterward** (verified 2026-07-24: `PUT /API/Election/<id>` 404,
  `POST …/edit` 502 — no owner-editable path; API-created elections aren't
  administrable). So cases minted *without* the backlink can't be retrofitted (the
  ballot_style_lab set BV2234–2247 is in that boat — repo→BV works, BV→repo doesn't).
- **Never choose a `BV<n>` by reading `BV_registry.md`'s "next free number."** That
  line is regenerated from *committed* files, so a concurrent session that has minted
  but not yet committed is invisible to it — and the number gets handed out twice. It
  happened (2026-07-25): BV2252 went to Goodberry's `6tthfv` while another session was
  building a case it believed was BV2252. A duplicate is **unrecoverable** — the number
  rides the permanent election title *and* every permanent race title, and neither can
  be edited or deleted. **`create_bv_test_election.py` now hard-stops on a reused Test
  ID** (`_preflight_test_id_collisions`, before any network call) and prints the next
  free number on every run; it reads minted numbers from the `BV<n> — ` title prefix of
  the saved exports in `06_Other/_demo_dropbox/`, which this script writes **at mint
  time** on the shared filesystem — so a concurrent session's election is visible the
  instant it exists, with no git operation needed. **Take the number from that printed
  line, not from the registry**, and don't disable the gate.
- **`BV<n>` in both artifacts — yes, keep it.** The human-readable Test ID belongs in
  *both* places so each side is findable from the other: on BV it rides the **election
  title** prefix (`BV<n> — <real title>`) **and every race title** (rule flipped by
  Adam 2026-07-25 — BV's `/vote` page leads with the *race* title in its big box, so
  a "clean" race title loses the cross-reference; BV2249 `c73pfw` is the example).
  `create_bv_test_election.py` auto-prepends it to each race via
  `_effective_race_title()` and the pre-check hard-stops if any race title would go
  out bare — don't hand-add the prefix in `bv_election_specs.py` race titles (the
  script adds it; elections up to BV2249 keep the old clean-race titles — permanent,
  can't be re-minted). In the repo it's the `bv_test_id:` field + the registry. The
  `<bvid>` (e.g. `td7jfy`) is the machine-stable link; `BV<n>` is the searchable
  cross-reference. Together with the two description/results links above, the BV
  election and its repo page fully point at each other.
- **Machine-readable BV fields + the repo registry.** A case `.yaml` may carry
  `bv_test_id`, `bv_election_id`, and `bv_results_url` as top-level fields — the
  tabulation engine ignores them; `tools_adam/scripts/build_bv_registry.py` reads
  them (falling back to the frozen `_bv_export.json` for the true election id, and
  the `bv…` filename for the Test ID) and regenerates
  `00_start_here/YAML_test_case_index/BV_registry.md` + `bv_cases.csv` — a
  sortable, repo-native index (method / winners / candidates / ballots / bvid /
  page / yaml). **The repo registry is canonical for tabulation cases** — the
  `.yaml` (source of truth) + `.md` (writeup) + the auto-generated
  `BV_registry.md` / `bv_cases.csv`. Regenerate it when adding a BV case.
  **No Google-Sheet sync is required for tabulation cases** (decided 2026-07 —
  the auto-registry already does the sheet's job at zero manual cost, and the bvid
  is the case id so there's no Test-ID to assign). The Google Sheet is retained
  **only** for the *extraordinary* non-tabulation QA that has no YAML home — UI,
  roles, archive, casting, "delete a race," video walkthroughs, pass/fail — which
  Adam maintains by hand when he wants to.
- **Creating BetterVoting elections — DON'T do it by hand.** No need to click
  through the BV builder UI (it's slow and fiddly). Use
  `STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py` — a
  uv-run (PEP 723) script that creates elections **and casts ballots** via the BV
  REST API (`POST /API/Elections`, `POST /API/Election/{id}/vote`). Define the
  election(s) — title, candidates, ballots, method, seats — in the **data module
  `bv_election_specs.py`** (the specs live there, separate from the ~520-line engine),
  point its `ELECTIONS` list at what you want to create (empty = create nothing), and
  run `uv run …/create_bv_test_election.py`; it prints the new
  `bettervoting.com/<id>` URLs. Auth is asymmetric **RS256** (the API requires a
  PEM public key in `auth_key`; the script mints a fresh keypair and signs the
  `custom_id_token` with the private key — no real account credential needed). It
  saves the election object to `06_Other/_demo_dropbox/` AND auto-freezes the full
  export beside it. **The UI "Download JSON" click is obsolete (2026-07-23):**
  sibling `fetch_bv_export.py` assembles the exact same
  `{Election, Ballots, Results}` JSON from three ANONYMOUS GETs —
  `/API/Election/{id}` + `/API/Election/{id}/anonymizedBallots` (public; the
  admin `/ballots` 401s) + `/API/ElectionResult/{id}` — verified byte-equivalent
  to the UI export on `vqyqkr` (ballot order may differ; that always varied).
  For any existing election: `uv run …/fetch_bv_export.py <bvid> -o
  <case>/cases/<yaml stem>_bv_export.json` (refuses to overwrite without
  `--force`; `--without-results` freezes crash-case elections whose
  ElectionResult 500s). Proven end-to-end (BV95a `9m6rxr`,
  BV95b `7pdq3r`). The old API doc's HS256 "secret == user id" trick is **stale** —
  the backend now demands RS256.
  - **BV methods & multi-winner (correction — 2026-07).** BV's seven
    `voting_method` strings are `STAR | STAR_PR | Approval | RankedRobin | IRV |
    Plurality | STV`. There is **no separate "Bloc STAR" string**, but BV *does*
    do bloc multi-winner: its `runBlocTabulator` drives **STAR, Approval,
    Plurality and Ranked Robin** whenever `num_winners > 1`. So **Bloc STAR =
    `STAR` + `num_winners: 3`** and **Bloc Approval = `Approval` +
    `num_winners: 2`**. (An earlier claim that BV couldn't do Bloc STAR /
    multi-winner Approval was WRONG — it can; the pets-governance set is fully
    BV-backable.) Ballot encoding per method: STAR/STAR_PR = scores 0-5;
    Approval/Plurality = 0/1; ranked (IRV/STV/RankedRobin) = **ranks** in the
    score slot (1 = top … 0 = unranked), validated `0..max_rankings`. Multi-race
    elections carry several `races[]`; each voter votes every race — grouped in
    `00_start_here/YAML_test_case_index/multirace_elections.md`.
  - **BV titles are PERMANENT and PUBLIC.** API-created elections can't be
    renamed, closed, or deleted (only a BV admin with DB access can purge them),
    and the title shows on the public results page — so give a real, meaningful
    title on the FIRST create (no "trash/delete/test" junk). The script prepends
    only the `BV<n>` Test ID and runs a pre-check that blocks junk/placeholder
    titles. See `bv_api_election_creation_notes.md` (orphan list included).
  - **Set `owner_id` to your real BV account** (the script default is Adam's
    `ea09e7c7-…`/Admin1) so the elections show up in `/manage`. **But** API-created
    elections are public, listable, and exportable **only** — they are **NOT
    UI-administrable** (you can't edit/close/**delete** them from `/admin`): BV
    authorizes admin off a server-side role binding written only by the
    authenticated create flow, not off `owner_id`/`admin_ids` (setting `admin_ids`
    is a proven no-op). Full write-up + a ready-to-file BV issue:
    `00_start_here/tabulation_engines/BV/bv_api_election_creation_notes.md`.

## Workflow — building a BV-backed test case

The loop that's working well (**Adam** = human, **AI** = assistant):

1. **Brainstorm in `trash_delete.yaml`** (AI + Adam). Draft the scenario —
   candidates, ballots, method, seats — in the scratch file and tabulate it with
   the LH engine until it demonstrates the intended behavior (a tie rung, a
   method divergence, a criterion failure…). Nothing here is permanent; iterate
   freely, keep examples small. **Ready-to-paste scratch skeleton** (the two
   gotchas: there is **no separate `candidates:` key** — the **first line of the
   `ballots:` block is the candidate header**, comma-separated; and weighted rows
   use a `Count:` header — `Count:Ada,Ben,Cara` then `15:5,2,0` per bloc):

   ```yaml
   title: Scratch (delete me)
   voting_method: STAR
   num_winners: 1
   options:            # house minimal block — see "Repo conventions"
     show_runoff_percent: true
     brief: true
   ballots: |-
     Ada,Ben,Cara
     5,2,0
     0,4,5
     2,5,4
   expected_winners: [Ben]
   ```

   Tabulate with `.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py trash_delete.yaml`.
   The run writes `_tabulated` mirrors into a sibling `<parentdir>_tabulated/`
   folder — for a scratch file at the repo root that's a junk `YAML_tabulated/`
   directory; **delete it (and the scratch files) when done, never commit them.**
2. **Go / no-go** (Adam decides). If the scenario earns its keep, promote it to a
   real case; otherwise it stays scratch / gets discarded.
   - **LOCK THE SMALLEST BALLOT SET *before* creating BV — BV elections are
     PERMANENT and undeletable, so the ballot count has to be right the first
     time.** Apply the house voter-count rules (fewest ballots that make the
     point; weighted `Count`s **≥ 6**; prefer a handful of blocs) *at the scratch
     stage*, not after minting. A demonstration that needs proportions (e.g. a
     center-squeeze ratio) can still usually be shown in ~30 ballots across 3
     clean blocs — don't reach for 100. Getting this wrong mints orphan public
     elections you can't take back.
3. **Create the BV election** (AI runs it; Adam must be signed in to BV). Add the
   election spec to the data module `bv_election_specs.py`, set its `ELECTIONS`
   list to that spec, then **dry-run first** — `uv run …/create_bv_test_election.py
   --dry-run` prints the exact title, every race title, candidates, ballot count and
   description that would be sent, and **pings the description's backlink URL** (a
   404 there is permanent — that's how BV2249 got one); it creates nothing. If the
   case will be printed on paper, `bv_ballot_sheet.py --spec <SPEC_NAME> --copies 1`
   shows the ballot itself before the election exists. Then run it for real:
   `uv run …/create_bv_test_election.py` creates the election **and casts the
   ballots** via the API and prints `bettervoting.com/<id>`. Never build it by
   hand in the UI. (Auth is asymmetric RS256; no real credential is stored.)
4. **Freeze the full JSON** (AI — automated since 2026-07-23). The create script
   now auto-freezes the full **Election + Ballots + Results** export into
   `06_Other/_demo_dropbox/`; for any election it can also be fetched on demand
   with `uv run …/fetch_bv_export.py <bvid> -o <path>` (three anonymous GETs —
   no UI click, no login; Adam is out of this step entirely).
5. **Reproduce in LH** (AI). Convert/import the export into a `.yaml` (converter:
   `YAML_library/1_positive/01_convert_json_yaml.py`); for a random tie-break, pin
   `lot_numbers` to BV's `perm`. Confirm LH's winner(s) match — or characterize the
   divergence. Freeze the export as `_bv_export.json`.
   - **Tie-breaks: the export records the whole sequence — don't say it "can't be
     frozen"** (corrected 2026-07-29). BV's `tieBreakType: "random"` is a **seeded**
     shuffle (`seed = (rawVoteCount + hash(raceId)) >>> 0`, TinyRand, shuffled once),
     deliberately deterministic per its own source. The export publishes **`perm`**
     (ids in tiebreak order), per-candidate **`tieBreakOrder`**, `tied[]`/`other[]`
     sorted by it, plus `tieBreakType` and a `logs` line — so winner *and* runners-up
     survive and a re-tally reproduces them. Pinning `lot_numbers` to `perm` makes LH
     replay the draw **exactly**. Recompute the shuffle independently with
     `uv run …/bv_replay_tiebreak.py <frozen export>` (or plain `python3` — stdlib
     only). Verified at 3 candidates (**BV2261** `y2fbpc`) and 9 (**BV2262**
     `2gvwr9`). **The real limit is narrower:** the order is *recorded* but not
     *derivable* — it depends on the ballot **count** and the race id, never on how
     anyone voted. So a case whose **winner** turns on the tiebreak stays **LH-only**
     (only LH's published lot lets a reader derive the result from the file); minting
     one on BV is fine only when the *recording mechanism* is the subject and the page
     says to ignore who won.
   - **Ranked Robin → also run the third-party cross-check.** `uv run
     …/pref_voting_tabulation_engine/ranked_robin_report.py <yaml>` tabulates Copeland
     with a library nobody here wrote; on a tie it returns the whole **leader set**,
     declines to pick, and reports whether LH's winner is inside it (`CONSISTENT ✓`).
     Run it on every RR case — it is what makes an RR result trustworthy rather than
     self-confirming. Full ladder + divergences:
     `05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md`.
6. **Build the case files** (AI). Name `bv<testid>_<bvid>_<descriptor>.{yaml,md,
   _bv_export.json}` (see naming rule above). The `.md` is the per-election page:
   the clickable `▶ … /results` lead line, ballots, the **inline LH tabulation
   on-screen report**, why the winner wins, and the BV-vs-LH agreement/divergence.
   `expected_winners` goes in the yaml.
7. **Regenerate indexes + mirrors** (AI). Run the yaml through the engine (writes
   its `_tabulated` mirror), then `tools_adam/scripts/build_yaml_index.py`, the
   folder `README.md` table, and `build_divergence_index.py` if it diverges.
8. **Verify + commit + push** (AI). The pre-commit hook runs the STAR suite + repo-hygiene;
   commit with a descriptive message, then **push** — Adam granted standing
   authorization (2026-07-20: *"feel free to push always — we can always undo... these
   are test cases and some descriptions"*), and pushing works from the sandbox:
   `git push https://github.com/masiarek/star-voting-library.git master`. (No need to
   hand Adam the push line anymore; just push and report the new SHA. The repo was
   renamed from `masiarek/YAML` on 2026-07-16; old URLs redirect. NEVER create a new
   repo named `YAML` — that would sever the redirects.)
9. **Registry regenerates itself** (AI). `build_bv_registry.py` writes
   `BV_registry.md` + `bv_cases.csv` from the case's `bv_*` fields — that's the
   canonical tracker. **No Google-Sheet update is required for tabulation cases**
   (decided 2026-07). Only ding Adam to touch the sheet for an *extraordinary*
   non-tabulation QA case (UI / roles / archive / casting / video) that has no YAML.

**LH-only cases** (no BetterVoting election — e.g. a reproduction of a Larry
`starvote` test file) skip steps 3–4 and the `<bvid>` filename segment; everything
else is the same.
