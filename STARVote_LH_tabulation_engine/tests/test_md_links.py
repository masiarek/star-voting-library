"""
test_md_links.py
================
Every relative link in a tracked Markdown file must resolve to a real file or
folder. Folder reorganizations silently break these (a 2026-07 reorg left 85+
dangling links); this test makes that class of breakage impossible to commit.

The scan itself lives in STARVote_LH_tabulation_engine/tools_adam/scripts/check_repo_hygiene.py (`check_links`) so the
warn-only pre-commit report and this blocking test can never disagree.

Deliberate placeholders — link a screenshot you haven't captured yet as
`img/REPLACE_<what>.png` — are skipped by convention.
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
HYGIENE = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts" / "check_repo_hygiene.py"


def _load_hygiene():
    spec = importlib.util.spec_from_file_location("check_repo_hygiene", HYGIENE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_repo_hygiene"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_all_relative_md_links_resolve():
    mod = _load_hygiene()
    broken = mod.check_links()
    assert not broken, (
        f"{len(broken)} broken relative Markdown link(s):\n" +
        "\n".join(f"  {f}  ->  ({raw})" for f, raw in broken) +
        "\n(Fix the path, or use the img/REPLACE_*.png placeholder convention "
        "for screenshots not yet captured.)"
    )


def test_no_bare_folder_links():
    """`[label](folder/)` must name the README.md explicitly.

    The bare form resolves on GitHub and on the built site, so it reads as fine
    from two of the three surfaces — but MkDocs does not rewrite it ("left as
    is" in the build log), so the raw href ships and the published page 404s,
    and a local Markdown viewer can't open it either. 635 links were landing
    dead on the site before the 2026-08 sweep; this stops the next one.
    """
    mod = _load_hygiene()
    bare = mod.check_folder_links()
    assert not bare, (
        f"{len(bare)} bare folder link(s) — name the README.md:\n" +
        "\n".join(f"  {rel}  ->  ({raw})   use ({fixed})" for rel, raw, fixed in bare)
    )


def test_folder_link_check_is_not_vacuous():
    """Prove the gate above can actually fail.

    A checker that silently matches nothing passes forever and protects
    nothing — the same reason tests/test_harness_selfcheck.py exists. This
    writes each bad spelling into the repo, confirms it is caught, and confirms
    the correct spelling and a fenced example are NOT caught.
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "07_Concepts" / "topics" / "_folder_link_probe.md"
    probe.write_text(
        "# probe\n"
        "[a](../../04_Approval/)\n"
        "[b](../../04_Approval)\n"
        "[c](../../04_Approval/#x)\n"
        "[d](../../04_Approval/README.md)\n"
        "`[e](../../04_Approval/)`\n",
        encoding="utf-8",
    )
    try:
        hits = [(raw, fixed) for rel, raw, fixed in mod.check_folder_links()
                if rel.endswith("_folder_link_probe.md")]
    finally:
        probe.unlink()
    raws = sorted(r for r, _ in hits)
    assert raws == ["../../04_Approval", "../../04_Approval/", "../../04_Approval/#x"], (
        f"expected all three bare spellings caught and nothing else, got {raws}"
    )
    assert dict(hits)["../../04_Approval/#x"] == "../../04_Approval/README.md#x", (
        "the #anchor must survive the suggested rewrite"
    )


def test_no_repo_root_paths_in_code_text():
    """A repo path in backticks must be a link, not bare code text.

    ``07_Concepts/tips/TIPS_terminology.md`` in a page under
    06_Other/RCV_IRV/concepts/variants/ reads as "go look at this," but every
    reader resolves it from the page's own folder — the desktop app opens
    `…/variants/07_Concepts/tips/TIPS_terminology.md` and reports the file
    missing. On GitHub and the built site it is inert, which is why
    check_links never saw this class.

    The compounding cost is silent rot: not being links, these were invisible
    to migrate_concept_links.py during the 2026-08-02 reorganization, so four
    of them still named pre-reorg paths (`07_Concepts/residual_vote_splitting.md`,
    `split_voting/*.yaml`) weeks after those files moved.
    """
    mod = _load_hygiene()
    bad = mod.check_code_span_paths()
    assert not bad, (
        f"{len(bad)} repo-root path(s) written as bare code text:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in bad)
    )


def test_code_span_path_check_is_not_vacuous():
    """Prove the gate above fires, and only on the misleading spelling.

    Three things must NOT be caught: a path that resolves from the page (it is
    correct as written), a path belonging to some other codebase (what code
    text is legitimately for), and one already used as a link label.
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "07_Concepts" / "topics" / "_code_span_probe.md"
    probe.write_text(
        "# probe\n"
        "`07_Concepts/GLOSSARY.md`\n"                    # caught: root-relative
        "`../GLOSSARY.md`\n"                             # ok: resolves from here
        "`packages/frontend/src/i18n/en.yaml`\n"         # ok: another codebase
        "[`07_Concepts/GLOSSARY.md`](../GLOSSARY.md)\n"  # ok: already a link
        "`GLOSSARY.md`\n",                               # ok: bare name, no path
        encoding="utf-8",
    )
    try:
        hits = [msg for rel, msg in mod.check_code_span_paths()
                if rel.startswith("07_Concepts/topics/_code_span_probe.md")]
    finally:
        probe.unlink()
    assert len(hits) == 1, f"expected exactly the root-relative path caught, got {hits}"
    assert "](../GLOSSARY.md)" in hits[0], (
        f"the suggested fix must be relative to the page, got: {hits[0]}"
    )


def test_claude_md_paths_all_resolve():
    """Every path CLAUDE.md names must still exist somewhere.

    CLAUDE.md is the one file where a root-relative path in code text is
    already correct — it sits AT the repo root — so the gate above deliberately
    exempts it, and it is deliberately not a wall of links (it loads into
    context every session). That leaves ~41 real paths that nothing verified.

    Inert text rots silently, and this is the worst file for that: both the
    contributor docs and every agent session take their instructions from it,
    so a path that goes stale here is *followed* for weeks. The 2026-08-02
    reorganization is the precedent — the story CLAUDE.md itself tells a few
    lines above one of these very paths.

    Reachability, not form: this is the complement of the code-span gate, which
    checks form and skips this file.
    """
    mod = _load_hygiene()
    bad = mod.check_claude_md_paths()
    assert not bad, (
        f"{len(bad)} stale path(s) in CLAUDE.md:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in bad)
    )


def test_claude_md_path_check_is_not_vacuous():
    """Prove it fires — including on the case that actually happens.

    A path that rots to *nothing* is the easy catch. The one that matters is a
    file that still exists but MOVED, because that is what a reorganization
    does, and the finding has to say where it went or it isn't actionable.

    Four things must NOT fire: a live path, engine-dir shorthand like `tests/…`
    (correct to type from the engine dir, and exempt in the gate above for that
    reason), a bare filename with no slash — `README.md` appears 11 times in
    CLAUDE.md meaning "a folder's README", not one file — and the deliberate
    examples, which have to stay broken to keep being examples.

    The probe is passed in rather than written to the real CLAUDE.md on
    purpose: this checkout is often open in two sessions at once, and a probe
    left behind by a crashed run would corrupt the file both are following.
    """
    mod = _load_hygiene()
    hits = mod.check_claude_md_paths(source=(
        "`01_STAR/GLOSSARY.md`\n"                 # caught: moved (it is 07_Concepts/)
        "`07_Concepts/tips/TIPS_gone_away.md`\n"  # caught: gone entirely
        "`07_Concepts/GLOSSARY.md`\n"             # ok: live path
        "`tests/test_md_links.py`\n"              # ok: engine-dir shorthand
        "`README.md`\n"                           # ok: a name, not a location
        "`07_Concepts/residual_vote_splitting.md`\n"  # ok: deliberate example
    ))
    assert len(hits) == 2, f"expected exactly the two stale paths, got {hits}"
    moved = [m for _rel, m in hits if "01_STAR/GLOSSARY.md" in m]
    assert moved, f"the moved-file case must be caught, got {hits}"
    assert "07_Concepts/GLOSSARY.md" in moved[0], (
        f"a moved-file finding must say where it went, got: {moved[0]}"
    )


def test_no_new_hand_pasted_engine_reports():
    """A long engine report on a companion page must be embedded, not pasted.

    Pasted output has nothing behind it, so it silently stops matching the
    engine — which is how the BV1815 page ended up showing a report format the
    engine had stopped emitting. Embedding the `_tabulated` mirror tracks the
    engine for free; a deliberate compression is fine but has to say `abridged`
    on the fence so a reader knows it isn't verbatim.
    """
    mod = _load_hygiene()
    pasted = mod.check_pasted_reports()
    assert not pasted, (
        f"{len(pasted)} companion page(s) with a hand-pasted engine report:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in pasted)
    )


def test_grandfather_list_stays_empty():
    """The burn-down finished; the exemption list is not a parking lot.

    All 34 pre-existing pasted reports were converted, so there is no page this
    rule can't be applied to. Re-populating the list would mean a new page
    pasted a report and the exemption was widened instead of the report embedded.
    """
    mod = _load_hygiene()
    assert not mod.PASTED_REPORT_GRANDFATHERED, (
        "PASTED_REPORT_GRANDFATHERED is non-empty: "
        + ", ".join(sorted(mod.PASTED_REPORT_GRANDFATHERED))
    )


def test_candidate_names_survive_yaml_as_strings():
    """A candidate name must come back from the parser as a name.

    PyYAML resolves bare scalars with YAML 1.1 rules, so `No` arrives as False,
    `Yes` as True, `Off` as False, `null` as None, `1.10` as 1.1 and `12:30` as
    750. The corpus is mostly protected by accident — candidate names live
    inside the `ballots: |-` block literal, which YAML hands over as one opaque
    string for the engine's own parser — but `expected_winners` and
    `election_title` are real resolved scalars.

    The project used StrictYAML for exactly this reason and lost it (see the
    check's own comment). The trip-wire is not exotic: the natural way to add a
    ballot-measure case is a contest whose options are Yes and No, and then a
    CORRECT winner fails its own answer key and reads like an engine bug.
    """
    mod = _load_hygiene()
    bad = mod.check_yaml_name_types()
    assert not bad, (
        f"{len(bad)} name(s) retyped by YAML — quote them:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in bad)
    )


def test_yaml_name_type_check_is_not_vacuous():
    """Prove the gate fires on the coercions that matter and spares real names.

    The names that must stay clean are the ones a naive check would flag: an
    ordinary quoted string, and a name that merely *looks* typed (`Nan` is a
    string to PyYAML, unlike `null`).
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "01_STAR" / "02_Examples" / "cases" / "_yaml_type_probe.yaml"
    probe.write_text(
        "election_title: YAML type probe (delete me)\n"
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "scenario_description: >-\n"
        "  A probe for the YAML implicit-typing gate; it is never tabulated and\n"
        "  exists only so the check can be proven to fire on a real file.\n"
        "ballots: |-\n"
        "  Yes,No,Maybe\n"
        "  5,2,0\n"
        "expected_winners:\n"
        '  - "No"\n'          # ok: quoted, stays a string
        "  - Nan\n"           # ok: PyYAML leaves this a string
        "  - No\n"            # caught: -> False
        "  - Yes\n"           # caught: -> True
        "  - 12:30\n"         # caught: -> 750 (base 60)
        "  - null\n",         # caught: -> None
        encoding="utf-8",
    )
    try:
        hits = [msg for rel, msg in mod.check_yaml_name_types()
                if rel.endswith("_yaml_type_probe.yaml")]
    finally:
        probe.unlink()
    assert len(hits) == 4, f"expected the four retyped entries, got {hits}"
    assert any("boolean False" in m for m in hits), hits
    assert any("750" in m for m in hits), hits


def test_ballot_weights_come_before_the_scores():
    """One election is written one way: the bloc count comes first.

    The YAML schema puts it there (`Count:Ada,Ben,Cara` / `15:5,2,0`) and so
    does the engine's echo (`Count × Memphis,…` / `42 × 5,4,3,2`). A source file
    physically cannot drift — the parser only ever matches a *leading* weight —
    so the trailing form only ever appears in hand-authored Markdown, the one
    surface with neither a parser nor a generator holding the line. Eight pages
    had accumulated it by 2026-08-07, and a reader meeting both forms has to
    work out per page which number is the ballot and which is the bloc size.
    """
    mod = _load_hygiene()
    bad = mod.check_ballot_weight_side()
    assert not bad, (
        f"{len(bad)} ballot row(s) with the weight after the scores:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in bad)
    )


def test_ballot_weight_check_is_not_vacuous():
    """Prove the gate fires on the trailing form and spares everything else.

    The rows that must stay clean are the ones that make a naive regex noisy:
    the correct leading form, the `Count ×` header, the YAML colon spelling, and
    an annotated ballot whose note simply has no multiplier in it.
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "07_Concepts" / "topics" / "_ballot_weight_probe.md"
    probe.write_text(
        "# probe\n"
        "```\n"
        "Count × Ada,Ben,Cara\n"                  # ok: header
        "    3 × 5,2,0\n"                         # ok: leading weight
        "   15:5,2,0\n"                           # ok: YAML colon spelling
        "5,2,0   ← the majority bloc\n"           # ok: annotated, no multiplier
        "0,4,5   ×3\n"                            # caught: bare trailing
        "1,0   × 5   Andre\n"                     # caught: trailing + note
        "5,4,0   ← the 3-voter majority (×3)\n"   # caught: buried in the note
        "```\n",
        encoding="utf-8",
    )
    try:
        hits = [rel for rel, _msg in mod.check_ballot_weight_side()
                if rel.startswith("07_Concepts/topics/_ballot_weight_probe.md")]
    finally:
        probe.unlink()
    assert len(hits) == 3, f"expected the three trailing-weight rows, got {hits}"


def test_uncommitted_target_check_is_not_vacuous(tmp_path, monkeypatch):
    """Prove the uncommitted-target guard can fail, and that it clears.

    The breakage it exists for is invisible locally by construction — the target
    IS in the working tree, which is exactly why check_links() passes and CI
    still dies — so it can only be exercised against a real git repo. Build a
    throwaway one: commit a page linking to a file, leave the file uncommitted,
    and the link must be flagged; commit the file and the flag must clear.

    Deliberately NOT paired with a "must be empty on this repo" gate. The hook
    blocks commits on a failing test, and an in-progress draft that links to a
    case not yet committed is normal, legitimate work — failing the whole suite
    for it would make the guard something people switch off.
    """
    import subprocess
    mod = _load_hygiene()

    def git(*args):
        subprocess.run(["git", "-C", str(tmp_path), *args],
                       check=True, capture_output=True)

    git("init", "-q")
    git("config", "user.email", "t@example.com")
    git("config", "user.name", "t")

    (tmp_path / "page.md").write_text("# page\n[t](target.md)\n", encoding="utf-8")
    git("add", "page.md")
    git("commit", "-qm", "page")

    # On disk, so check_links() is perfectly happy — but never committed.
    (tmp_path / "target.md").write_text("# target\n", encoding="utf-8")

    monkeypatch.setattr(mod, "REPO", str(tmp_path))
    hits = [(rel, tgt) for rel, _raw, tgt in mod.check_untracked_link_targets()]
    assert hits == [("page.md", "target.md")], (
        "a committed page linking to an uncommitted file must be flagged "
        f"(this is the failure that reddened the docs build); got {hits}"
    )
    assert not mod.check_links(), (
        "check_links() must NOT catch it — if it did, this guard would be "
        "redundant and the docs build would never have gone red"
    )

    git("add", "target.md")
    git("commit", "-qm", "target")
    assert mod.check_untracked_link_targets() == [], (
        "committing the target must clear the flag"
    )


def test_untracked_report_is_capped_and_summarizes_by_target():
    """The finding list must stay bounded, and the overflow must be actionable.

    A concurrent session mid-rename produces one uncommitted case linked from a
    dozen generated pages; an uncapped list once printed 48 near-identical lines
    and buried every other hygiene check. What you act on is the set of DISTINCT
    uncommitted targets, so the overflow names those rather than just counting.
    """
    mod = _load_hygiene()
    cap = mod._MAX_LISTED
    # 14 hits, 3 distinct targets — i.e. more findings than the cap.
    hits = [(f"page{i:02d}.md", f"target{i % 3}.md", f"target{i % 3}.md")
            for i in range(14)]
    lines = mod.format_untracked_report(hits)

    bullets = [l for l in lines if l.lstrip().startswith("•")]
    assert len(bullets) == cap, f"expected the list capped at {cap}, got {len(bullets)}"
    assert any(f"and {14 - cap} more" in l for l in lines), lines
    assert any("Commit these 3 file(s)" in l for l in lines), (
        "the overflow must name how many distinct files actually need committing"
    )
    for t in ("target0.md", "target1.md", "target2.md"):
        assert any(l.strip() == f"- {t}" for l in lines), f"{t} missing from summary"

    # Under the cap, no summary at all — just the findings.
    few = mod.format_untracked_report(hits[:3])
    assert len(few) == 3 and not any("more" in l for l in few), few


def test_links_inside_html_comments_are_not_reported():
    """An HTML comment renders as nothing on GitHub, on the site, and in a local
    viewer, so a path inside one is not a link.

    This is load-bearing, not pedantic: the BV workflow tells you to comment out
    a screenshot slot you haven't captured yet rather than leave a REPLACE_
    placeholder. Before this, a commented-out `<img src=…>` in an abstain_bugs
    case was reported as a broken link and reddened the docs build (2026-08-06).
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "07_Concepts" / "topics" / "_html_comment_probe.md"
    probe.write_text(
        "# probe\n"
        "<!-- [a](no_such_commented.md) -->\n"
        "<!-- a multi-line slot, as the BV workflow prescribes:\n"
        '     <img src="no_such_slot.png" width="560"> -->\n'
        "[b](no_such_real.md)\n",
        encoding="utf-8",
    )
    try:
        raws = sorted(raw for rel, raw in mod.check_links()
                      if rel.endswith("_html_comment_probe.md"))
    finally:
        probe.unlink()
    assert raws == ["no_such_real.md"], (
        "only the uncommented link may be reported; commented-out paths are inert "
        f"on every surface. got {raws}"
    )


def test_proper_nouns_spelled_with_rcv_are_not_terminology_violations():
    """`rcv-lab.org` is a tool's NAME, not our sloppy terminology.

    The precision rule is `\\bRCV\\b` + an IRV-specific word on the same line,
    case-insensitive. A hyphen and a dot are both word boundaries, so the `rcv`
    in `rcv-lab.org` matched it, and every line naming that tool alongside
    "eliminated" was reported — a false positive the checker emitted forever
    (coombs_ex20_district1.yaml was the live one).

    Narrowing a checker is the dangerous direction: the fix must silence the
    NAME without silencing the rule. Both halves are asserted here.
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "07_Concepts" / "topics" / "_terminology_probe.md"
    probe.write_text(
        "# probe\n"
        "rcv-lab.org drops B, so that ballot is eliminated.\n"   # name only  -> clean
        "RCVis draws the eliminated rounds.\n"                   # mid-word   -> clean
        "RCV-IRV eliminates the centrist in round one.\n"        # correct    -> clean
        "RCV eliminates the centrist in round one.\n"            # violation  -> caught
        "Both rcv-lab.org and RCV exhaust ballots.\n",           # violation  -> caught
        encoding="utf-8",
    )
    try:
        lines = sorted(ln for rel, ln, _ in mod.check_terminology()
                       if rel.endswith("_terminology_probe.md"))
    finally:
        probe.unlink()
    assert lines == [5, 6], (
        "expected ONLY the two bare-RCV lines (5 and 6) to be reported: the name "
        "must be exempt, and scrubbing it must not swallow a real violation on the "
        f"same line. got lines {lines}"
    )


def test_redirect_maps_are_sound():
    """Every `redirect_maps` entry in mkdocs.yml must point at a page that
    exists, and no key may appear twice.

    A missing destination is a red docs deploy: `mkdocs-redirects` warns and
    `--strict` aborts on the warning, for every push until someone notices.
    A duplicate key is how the missing destination hides — PyYAML keeps the
    LAST value, so an old entry still pointing at a since-deleted page silently
    overrides the newer one that points somewhere live. That is the 2026-08-20
    story: 04a8eea deleted two generated pages and redirected both their URL
    forms to the folder README, two reorg-era entries with the same keys were
    left behind and won, and the deploy stayed red for 14 commits. CLAUDE.md
    said to assert every destination exists "by hand"; this is that assertion.
    """
    mod = _load_hygiene()
    bad = mod.check_redirect_maps()
    assert not bad, (
        f"{len(bad)} mkdocs.yml redirect problem(s):\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in bad)
    )


def test_redirect_map_check_is_not_vacuous():
    """Prove it fires on both halves, and only there.

    Must NOT fire: a live destination, a destination with an `#anchor` (the
    anchor is stripped before the file is looked up), an external URL, and a
    comment line inside the block. Must fire once each: a destination that does
    not exist, and a key that appears twice — and the duplicate finding has to
    say where the first one was, or it isn't actionable. The probe is passed
    in rather than written to the real mkdocs.yml: this checkout is shared.
    """
    mod = _load_hygiene()
    hits = mod.check_redirect_maps(source=(
        "plugins:\n"
        "  - redirects:\n"
        "      redirect_maps:\n"
        "        # a comment inside the block\n"
        "        old/a.md: 07_Concepts/GLOSSARY.md\n"            # ok: live
        "        old/b.md: 07_Concepts/GLOSSARY.md#some-anchor\n"  # ok: anchor
        "        old/e.md: https://example.org/elsewhere\n"       # ok: external
        "        old/c.md: 07_Concepts/no_such_page.md\n"         # caught: missing
        "        old/a.md: 07_Concepts/CURRICULUM.md\n"           # caught: duplicate
        "markdown_extensions:\n"
        "  - toc\n"
    ))
    assert len(hits) == 2, f"expected exactly two findings, got {hits}"
    missing = [m for _rel, m in hits if "no_such_page" in m]
    dup = [m for _rel, m in hits if "duplicate" in m]
    assert missing and dup, hits
    assert "first at line 5" in dup[0], (
        f"a duplicate finding must say where the first key was, got: {dup[0]}"
    )


def test_bv_backed_pages_link_their_live_election():
    """A BV-backed case page must link its own election's /results, clickably.

    CLAUDE.md and the `bettervoting` skill both require this — "not just the
    bare election id" — and for a long time nothing enforced it, which is how
    31 pages drifted: 17 with no link at all (build_yaml_pages.py guessed the
    bvid from the FILENAME with a regex that wants it in the middle, so every
    `<descriptor>_<bvid>` case matched nothing), and 14 hand-authored
    companions naming their bvid only in backticks.

    The check asks for the right ID, not merely for the presence of a link,
    because the worst instance had a link: the same filename guess read the
    descriptor word "verify" out of bv132_verify_votes_bloc and published
    https://bettervoting.com/verify, which 400s. A confident link to an
    election that does not exist is a wrong claim on a teaching page, and it
    survived precisely because it looked right — bold, in house form, and
    nobody had reason to click it.
    """
    mod = _load_hygiene()
    bad = mod.check_bv_results_links()
    assert not bad, (
        f"{len(bad)} BV-backed write-up(s) not linking their election:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in bad) +
        "\n(Add the house lead line under the page's case-meta block:\n"
        "  **▶ Live on BetterVoting:** [vote](https://bettervoting.com/<bvid>) · "
        "**[results ↗](https://bettervoting.com/<bvid>/results)** (election `<bvid>`).)"
    )


def test_bv_results_link_check_is_not_vacuous():
    """The gate must fail on both shapes it exists to catch.

    A check that only ever runs over a passing repo is indistinguishable from
    one that returns [] unconditionally — and this gate spent its first
    commit in exactly that state, warned-but-never-tested, which is the same
    rot it was written to end. So: plant a page with no link, and plant one
    linking the WRONG election, and require a finding for each.
    """
    mod = _load_hygiene()

    silent = mod.check_bv_results_links(
        source=("planted.md", "The election is `3494cb`.", "3494cb"))
    assert silent, "a page naming its bvid only in backticks must be caught"
    assert "no clickable link" in silent[0][1], silent

    wrong = mod.check_bv_results_links(
        source=("planted.md",
                "**[results ↗](https://bettervoting.com/verify/results)**", "3494cb"))
    assert wrong, "a page linking the WRONG election must be caught"
    assert "verify" in wrong[0][1] and "3494cb" in wrong[0][1], (
        f"the finding must name both the linked and the expected election: {wrong[0][1]}"
    )

    ok = mod.check_bv_results_links(
        source=("planted.md",
                "**[results ↗](https://bettervoting.com/3494cb/results)**", "3494cb"))
    assert not ok, f"a correct house lead line must pass, got {ok}"
