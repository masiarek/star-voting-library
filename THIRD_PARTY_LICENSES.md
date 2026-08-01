# Third-Party Licenses

This project depends on third-party packages. Their licenses are recorded below.
Everything — runtime, tooling, and vendored code — is permissive (MIT / BSD / Apache-2.0).

## Vendored code (copied into this repository)

| Project | Where | License | Notice file |
|---------|-------|---------|-------------|
| `starvote` (Larry Hastings) | `STARVote_LH_tabulation_engine/starvote/` | MIT | [`STARVote_LH_tabulation_engine/LICENSE`](STARVote_LH_tabulation_engine/LICENSE) |
| `pyrankvote` (Jon Tingvold) | `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/pyrankvote/` | MIT | [`LICENSE.txt`](06_Other/RCV_IRV/RCV_IRV_tabulation_engine/pyrankvote/LICENSE.txt) in its directory |
| `tabulate` (Sergey Astanin and contributors) | `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/tabulate/` | MIT | [`LICENSE`](06_Other/RCV_IRV/RCV_IRV_tabulation_engine/tabulate/LICENSE) in its directory |

## Installed dependencies

| Package | Used for | License |
|---------|----------|---------|
| `pyyaml` (runtime) | reading the election YAML files | MIT (full text below) |
| `pref-voting` (runtime) | independent cross-check of ranked/Condorcet tabulations | MIT |
| `pytest` (dev) | the test suite | MIT |
| `abcvoting` (dev) | independent cross-check of multi-winner Approval (ABC) rules | MIT |
| `mypy` (dev) | optional type checking | MIT |
| `faker` (tools) | candidate-name generation | MIT |
| `playwright` (tools) | ballot-sheet PDF rendering | Apache-2.0 |
| `segno` (tools) | QR codes on printable ballots | BSD-3-Clause |
| `mkdocs` / `mkdocs-material` / `mkdocs-same-dir` / `mkdocs-redirects` (docs) | the website build | BSD-2-Clause / MIT / MIT / MIT |

All of these are downloaded from PyPI at install time (none are redistributed
here), so shipping their license texts is not required; the vendored copies
above do ship their notices in-tree.

## PyYAML

- **Package:** `pyyaml` (>=6.0.3)
- **License:** MIT License — a permissive license. It allows use, copying, modification, merging, publishing, distribution, sublicensing, and sale, including in closed-source commercial software. The only obligation is to include the copyright notice and license text in copies or substantial portions of the software. No warranty is provided.
- **Verdict:** Permissive and safe to use, including commercially.

```
Copyright (c) 2017-2021 Ingy döt Net
Copyright (c) 2006-2016 Kirill Simonov

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
