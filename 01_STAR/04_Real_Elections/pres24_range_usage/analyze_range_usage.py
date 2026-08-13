#!/usr/bin/env python3
"""Measure scale-utilization on the pres24 STAR ballots, and test whether it matters.

Answers the question raised about https://bettervoting.com/pres24 : 14% of ballots
never used both ends of the 0-5 scale -- does that change who wins?

Reproduce from scratch (no repo data needed; the export is public):

    uv run STARVote_LH_tabulation_engine/tools_adam/fetch_bv_export.py pres24 -o /tmp/pres24.json
    python3 01_STAR/04_Real_Elections/pres24_range_usage/analyze_range_usage.py /tmp/pres24.json

The 13 MB export is deliberately NOT committed -- the command above regenerates it,
and cases/pres24_star_range_usage.yaml holds the 2,772 ballots in engine form (50 KB).
"""
import json, sys, collections, random

STAR_RACE = '9c909d7c-536b-403e-b711-0973b4d0392c'

def load(path):
    d = json.load(open(path))
    race = [r for r in d['Election']['races'] if r['race_id'] == STAR_RACE][0]
    cands = [c['candidate_id'] for c in race['candidates']]
    names = [c['candidate_name'].split('(')[0].strip() for c in race['candidates']]
    raw = []
    for b in d['Ballots']:
        for v in b['votes']:
            if v['race_id'] == STAR_RACE:
                m = {s['candidate_id']: s['score'] for s in v['scores']}
                raw.append([m.get(c) for c in cands])
    return d, names, raw

def zed(r):            # blanks tabulate as 0, exactly as BetterVoting does
    return [0 if s is None else s for s in r]
def has_full_range(r):  # a 5 at the top AND an effective zero at the bottom
    mk = [s for s in r if s is not None]
    return 5 in mk and (any(s is None for s in r) or 0 in mk)
def levels(r):
    return len(set(zed(r)))
def pairwise(rows, i, j):
    a = b = e = 0
    for r in rows:
        if r[i] > r[j]: a += 1
        elif r[j] > r[i]: b += 1
        else: e += 1
    return a, b, e
def star(rows):
    t = [sum(r[i] for r in rows) for i in range(len(rows[0]))]
    o = sorted(range(len(t)), key=lambda i: -t[i])
    a, b, _ = pairwise(rows, o[0], o[1])
    return t, o, (o[0] if a > b else o[1])

def main(path):
    d, names, raw = load(path)
    Z = [zed(r) for r in raw]
    # BetterVoting drops ballots that score every candidate identically before totalling
    tallied = [r for r in Z if len(set(r)) > 1]
    n = len(raw)
    full = [r for r in raw if has_full_range(r)]
    comp = [r for r in raw if not has_full_range(r)]

    print(f'ballots: {n}   full range: {len(full)} ({len(full)/n:.1%})   '
          f'not full range: {len(comp)} ({len(comp)/n:.1%})')

    print('\n-- what the non-full-range ballots are missing --')
    top = collections.Counter(max(zed(r)) for r in comp)
    print('   highest score anywhere on the ballot:',
          ', '.join(f'{k}->{v}' for k, v in sorted(top.items())))
    miss5 = sum(1 for r in comp if 5 not in [s for s in r if s is not None])
    print(f'   missing a 5 (nobody earned full marks): {miss5} = {miss5/len(comp):.0%} of them')
    print(f'   missing a bottom (everyone scored >=1): {len(comp)-miss5} = {(len(comp)-miss5)/len(comp):.0%}')

    print('\n-- are they LESS expressive? distinct score levels used --')
    for label, grp in (('not full range', comp), ('full range', full)):
        c = collections.Counter(levels(r) for r in grp)
        rich = sum(v for k, v in c.items() if k >= 4)
        print(f'   {label:16s} 4+ levels: {rich:5d}/{len(grp)} = {rich/len(grp):5.1%}   '
              f'(mean {sum(levels(r) for r in grp)/len(grp):.2f} levels)')

    print('\n-- the result, as cast --')
    t, o, w = star(tallied)
    for k, i in enumerate(o):
        print(f'   {k+1}. {names[i]:22s} {t[i]:7d}')
    f1, f2 = o[0], o[1]
    a, b, e = pairwise(tallied, f1, f2)
    print(f'   runoff: {names[f1]} {a} vs {names[f2]} {b} (Equal Support {e}) -> {names[w]} wins')
    print(f'   2nd-vs-3rd scoring gap: {t[o[1]]-t[o[2]]} '
          f'({(t[o[1]]-t[o[2]])/t[o[1]]:.1%} of 2nd place) <- the fragile number')

    print('\n-- is the scoring leader also the Condorcet winner? --')
    ok = all(pairwise(tallied, f1, j)[0] > pairwise(tallied, f1, j)[1]
             for j in range(len(names)) if j != f1)
    print(f'   {names[f1]} beats all {len(names)-1} rivals head-to-head: {ok}')
    print('   => any finalist pair containing the leader returns the same winner')

    print('\n-- counterfactuals: stretch the compressed ballots to the full scale --')
    def norm(z):
        lo, hi = min(z), max(z)
        return z if hi == lo else [round((s - lo) * 5 / (hi - lo)) for s in z]
    variants = [
        ('as cast (baseline)', tallied),
        ('non-full-range ballots stretched to 0-5',
         [norm(zed(r)) if not has_full_range(r) else zed(r) for r in raw if len(set(zed(r))) > 1]),
        ('non-full-range ballots discarded entirely',
         [zed(r) for r in raw if has_full_range(r) and len(set(zed(r))) > 1]),
        ('every ballot normalized', [norm(r) for r in tallied]),
    ]
    for label, rows in variants:
        t2, o2, w2 = star(rows)
        print(f'   {label:42s} 2nd={names[o2[1]]:14s} winner={names[w2]}')

    print('\n-- runoff power: who actually wasted their vote? --')
    for label, grp in (('not full range', comp), ('full range', full)):
        rows = [zed(r) for r in grp]
        a, b, e = pairwise(rows, f1, f2)
        print(f'   {label:16s} expressed a runoff preference: '
              f'{a+b}/{len(rows)} = {(a+b)/len(rows):5.1%}  (Equal Support {e})')

    print('\n-- bootstrap: is 2nd place determinate at all? (2000 resamples) --')
    random.seed(12345)
    m = len(tallied); second = collections.Counter(); wins = collections.Counter()
    for _ in range(2000):
        s = [tallied[random.randrange(m)] for _ in range(m)]
        _, o3, w3 = star(s)
        second[names[o3[1]]] += 1; wins[names[w3]] += 1
    print('   2nd finalist slot:', dict(second.most_common()))
    print('   WINNER           :', dict(wins.most_common()))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'pres24_bv_export.json')
