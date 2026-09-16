# qianqian-xie.github.io

Personal homepage of Qianqian Xie (谢倩倩), Professor at the School of Artificial Intelligence, Wuhan University.

The site is a single static page, bilingual (English / 中文), with no build step.

| File | What it is |
| --- | --- |
| `index.html` | The whole page: content, styles and scripts. Edit text directly here. Every string appears twice, in `data-lang="en"` and `data-lang="zh"` elements. |
| `data/pubs.js` | Publication list and citation stats, generated from Google Scholar. Do not edit by hand. |
| `scripts/sync_scholar.py` | Regenerates `data/pubs.js`. Runs weekly via GitHub Actions, or manually with `python3 scripts/sync_scholar.py`. |
| `assets/img/prof_pic.jpg` | Profile photo. |

Pushing to `main` deploys to the `gh-pages` branch, which GitHub Pages serves at <https://qianqian-xie.github.io/>.

News and lab-wide content live on the lab website, <https://clain.org/>; this page links there instead of duplicating it.
