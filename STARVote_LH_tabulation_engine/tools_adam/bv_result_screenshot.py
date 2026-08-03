#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["websockets>=12"]
# ///
"""
bv_result_screenshot.py — capture a BetterVoting results page as a house-convention PNG
=======================================================================================

Takes the `img/<bvid>_<what>.png` screenshots the case pages embed, without
anyone opening a browser, cropping by hand, or pasting `img_3.png` out of
PyCharm. Companion to `fetch_bv_export.py`: that one freezes the numbers, this
one freezes the picture.

HOW IT WORKS — headless Chrome driven over the DevTools Protocol. Because it
clips to a real DOM element, the shot comes out framed on the result card with
no nav bar, no footer, and no manual cropping.

USAGE (uv-native, PEP 723 — no venv needed):

    # the result card: winner headline + voters + the Head-to-head/Runoff chart
    uv run bv_result_screenshot.py 48hjkv --shot result \
        -o 05_Ranked_Robin/02_Examples/condorcet_vs_ranked_robin/img/48hjkv_result_bars.png

    # the Race Details table (expands the accordion first)
    uv run bv_result_screenshot.py 48hjkv --shot race-details \
        -o 05_Ranked_Robin/02_Examples/condorcet_vs_ranked_robin/img/48hjkv_race_details.png

    # anything else: clip to your own selector, optionally after running some JS
    uv run bv_result_screenshot.py 48hjkv -o img/48hjkv_matchups.png \
        --clip ".graph" --prep "document.querySelector('.detailExpander').click()"

Then embed it with a SIZED <img> (house style — a bare ![]() renders full-bleed):

    <img alt="BetterVoting result page for 48hjkv: …" src="img/48hjkv_result_bars.png" width="640">

TWO GOTCHAS, both already handled here — don't "simplify" them back out:

* **Never pass `captureBeyondViewport`.** It forces a relayout, which restarts
  recharts' bar animation, and the shot lands with every bar at zero width — a
  chart with labels and no bars. Instead this script emulates a tall viewport
  (`--height`, default 2600) so the element fits on screen and clips inside it.
* **Random tiebreaks are stable — and not because of caching.** BV tabulates on
  demand, and a drawn result (`tieBreakType: random`, e.g. `4gfwdq`, `3r3yf7`,
  `y2fbpc`, `2gvwr9`) keeps returning the same winner because the tiebreak is a
  SEEDED shuffle, not a coin flip: `seed = (rawVoteCount + hash(raceId)) >>> 0`,
  shuffled once by TinyRand, with the drawn order published as `perm`. Verified
  byte-identical across repeated fetches, and independently recomputed by
  `bv_replay_tiebreak.py`. So a screenshot won't contradict the frozen
  `_bv_export.json`. Check against the export anyway before committing a tie
  case's shot — and note the order only moves if the BALLOT COUNT changes.

House sizing: the repo's screenshots run ~1400-1600 px wide; downsample after
capture if a shot comes out larger, e.g. `magick out.png -resize 1600x -strip out.png`.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

import websockets

CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)

# Hide the collapsed "Race Details" strip so the result card ends at the chart.
_HIDE_EXPANDER = (
    "(() => { const e = document.querySelector('.detailExpander');"
    " if (e) e.style.display = 'none'; return 'hidden'; })()"
)

# Expand Race Details, then tag the "Table" card so --clip can find it.
_OPEN_RACE_DETAILS = """
(async () => {
  const x = document.querySelector('.detailExpander');
  if (!x) return 'no expander';
  x.click();
  await new Promise(r => setTimeout(r, 2000));
  const h = [...document.querySelectorAll('h5')]
      .find(e => e.textContent.trim() === 'Table');
  if (!h) return 'no Table heading';
  h.closest('.MuiPaper-root').id = 'shotTarget';
  return 'tagged';
})()
"""

SHOTS = {
    # name          -> (clip selector, prep JS)
    "result": (".flexContainer", _HIDE_EXPANDER),
    "race-details": ("#shotTarget", _OPEN_RACE_DETAILS),
    "chart": (".graph", _HIDE_EXPANDER),
    "page": (None, None),
}


def _launch(port: int, profile: Path) -> subprocess.Popen:
    if not Path(CHROME).exists():
        raise SystemExit(
            f"Chrome not found at {CHROME}\n"
            "Set $CHROME to your Chrome/Chromium binary."
        )
    return subprocess.Popen(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-first-run",
            "--no-default-browser-check",
            f"--remote-debugging-port={port}",
            f"--user-data-dir={profile}",
            "about:blank",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def _page_ws(port: int, timeout: float = 20.0) -> str:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            raw = urllib.request.urlopen(
                f"http://127.0.0.1:{port}/json/list", timeout=2
            ).read()
            for t in json.loads(raw):
                if t.get("type") == "page" and t.get("webSocketDebuggerUrl"):
                    return t["webSocketDebuggerUrl"]
        except Exception:
            pass
        time.sleep(0.3)
    raise SystemExit("Chrome's DevTools endpoint never came up")


class CDP:
    """Minimal DevTools Protocol client — send a command, await its reply."""

    def __init__(self, ws):
        self.ws = ws
        self.n = 0

    async def send(self, method: str, **params):
        self.n += 1
        mid = self.n
        await self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            msg = json.loads(await self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    async def eval(self, expr: str):
        r = await self.send(
            "Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True
        )
        return r.get("result", {}).get("value")


async def shoot(
    url: str,
    out: Path,
    clip_sel: str | None,
    prep: str | None,
    width: int,
    height: int,
    scale: float,
    pad: int,
    settle: float,
) -> None:
    profile = Path(tempfile.mkdtemp(prefix="bvshot-"))
    port = 9333
    proc = _launch(port, profile)
    try:
        async with websockets.connect(_page_ws(port), max_size=64 * 1024 * 1024) as ws:
            cdp = CDP(ws)
            await cdp.send("Page.enable")
            await cdp.send("Runtime.enable")
            # Tall viewport instead of captureBeyondViewport — see the module
            # docstring: that flag relayouts and restarts the bar animation.
            await cdp.send(
                "Emulation.setDeviceMetricsOverride",
                width=width,
                height=height,
                deviceScaleFactor=scale,
                mobile=False,
            )
            await cdp.send("Page.navigate", url=url)
            await asyncio.sleep(settle)

            if prep:
                print(f"  prep: {await cdp.eval(prep)}")
                await asyncio.sleep(1.5)

            clip = None
            if clip_sel:
                rect = await cdp.eval(
                    "(() => { const e = document.querySelector(%s);"
                    " if (!e) return null; const r = e.getBoundingClientRect();"
                    " return JSON.stringify({x: r.left + scrollX, y: r.top + scrollY,"
                    " w: r.width, h: r.height}); })()" % json.dumps(clip_sel)
                )
                if not rect:
                    raise SystemExit(f"selector not found on the page: {clip_sel}")
                r = json.loads(rect)
                clip = {
                    "x": max(0, r["x"] - pad),
                    "y": max(0, r["y"] - pad),
                    "width": r["w"] + 2 * pad,
                    "height": r["h"] + 2 * pad,
                    "scale": scale,
                }

            kw = {"format": "png", "captureBeyondViewport": False}
            if clip:
                kw["clip"] = clip
            shot = await cdp.send("Page.captureScreenshot", **kw)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(base64.b64decode(shot["data"]))
            print(f"wrote {out}  ({out.stat().st_size:,} bytes)")
    finally:
        proc.terminate()
        proc.wait(timeout=10)
        shutil.rmtree(profile, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("bvid_or_url", help="BetterVoting election id, or a full URL")
    ap.add_argument("-o", "--out", required=True, type=Path,
                    help="output PNG (house naming: img/<bvid>_<what>.png)")
    ap.add_argument("--shot", choices=sorted(SHOTS), default="result",
                    help="preset region (default: result)")
    ap.add_argument("--clip", help="CSS selector to clip to (overrides --shot)")
    ap.add_argument("--prep", help="JS to run before the shot (overrides --shot)")
    ap.add_argument("--width", type=int, default=820, help="viewport width (default 820)")
    ap.add_argument("--height", type=int, default=2600,
                    help="viewport height; must exceed the clipped element (default 2600)")
    ap.add_argument("--scale", type=float, default=2.0, help="device pixel ratio (default 2)")
    ap.add_argument("--pad", type=int, default=12, help="px of padding around the clip")
    ap.add_argument("--settle", type=float, default=8.0,
                    help="seconds to wait for React + chart animation (default 8)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing PNG")
    a = ap.parse_args()

    if a.out.exists() and not a.force:
        raise SystemExit(f"{a.out} exists — pass --force to overwrite")

    preset_clip, preset_prep = SHOTS[a.shot]
    clip = a.clip if a.clip is not None else preset_clip
    prep = a.prep if a.prep is not None else preset_prep

    target = a.bvid_or_url
    if not target.startswith("http"):
        target = f"https://bettervoting.com/{target}/results"
    print(f"capturing {target}  (shot={a.shot})")
    asyncio.run(shoot(target, a.out, clip, prep, a.width, a.height, a.scale,
                      a.pad, a.settle))
    return 0


if __name__ == "__main__":
    sys.exit(main())
