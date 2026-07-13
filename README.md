# Movie Rating Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)
![Status](https://img.shields.io/badge/status-production--ready-success.svg)

> A production-grade data-science pipeline that ingests, cleans, analyzes and reports on
> movie rating data (MovieLens-style). Built as a CODTECH summer internship submission.

**Author:** Sumit Kumar
**Intern ID:** CITS3958

---

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Architecture](#architecture)
5. [Folder Structure](#folder-structure)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Screenshots & Output](#screenshots--output)
9. [Working](#working)
10. [Example](#example)
11. [Testing](#testing)
12. [Troubleshooting](#troubleshooting)
13. [Future Improvements](#future-improvements)
14. [Acknowledgements](#acknowledgements)
15. [References](#references)
16. [License](#license)
17. [Author](#author)

---

## Project Description
This project analyses a movie ratings dataset to surface actionable insights such as
top-rated titles, most-active users, rating distributions per genre, temporal trends,
and correlations between rating volume and average score. The pipeline is fully
modular and reproducible: run `python -m src.main` and every chart, table and HTML
report is regenerated from raw CSVs.

A synthetic MovieLens-style dataset (`data/raw/movies.csv`, `data/raw/ratings.csv`)
is bundled so the pipeline runs end-to-end without any external download.

## Features
- End-to-end reproducible pipeline (loader -> cleaner -> analyzer -> reporter)
- Genre-level statistics with weighted (Bayesian) ratings to counter low-vote bias
- Top-N charts, rating histograms, genre heatmaps and time-series trend plots
- Standalone HTML report (self-contained, portable)
- JSON summary artifact for downstream tooling
- Fully unit-tested with `pytest`
- CI workflow (GitHub Actions) for lint + tests
- Clean CLI with logging and progress indicators

## Tech Stack
- **Language:** Python 3.10+
- **Data:** pandas, numpy
- **Statistics:** scipy
- **Visualization:** matplotlib, seaborn
- **Reporting:** Jinja2 (HTML), JSON
- **Testing:** pytest
- **Tooling:** ruff (lint), black (format), GitHub Actions (CI)

## Architecture
```text
        +-----------+     +-----------+     +------------+     +-----------+
raw --> |  loader   | --> |  cleaner  | --> |  analyzer  | --> | reporter  | --> reports/
        +-----------+     +-----------+     +------------+     +-----------+
              |                 |                  |                  |
              v                 v                  v                  v
        schema check      null / dup fix     weighted stats     HTML + JSON + PNG
```

## Folder Structure
```text
movie-rating-analysis/
├── src/
│   ├── __init__.py
│   ├── loader.py         # CSV ingestion + schema validation
│   ├── cleaner.py        # Null handling, deduplication, feature engineering
│   ├── analyzer.py       # Statistical analysis + aggregations
│   ├── visualizer.py     # matplotlib / seaborn charts
│   ├── reporter.py       # HTML + JSON report generation
│   ├── config.py         # Central paths + constants
│   └── main.py           # Orchestrator / CLI entrypoint
├── tests/
│   ├── test_loader.py
│   ├── test_cleaner.py
│   └── test_analyzer.py
├── notebooks/
│   └── 01_movie_rating_eda.ipynb
├── data/
│   ├── raw/              # movies.csv, ratings.csv (bundled sample)
│   └── processed/        # generated cleaned parquet/csv
├── reports/              # generated HTML + PNG + JSON
├── docs/
│   ├── ARCHITECTURE.md
│   ├── METHODOLOGY.md
│   └── FINDINGS.md
├── assets/
│   └── banner.svg
├── .github/workflows/ci.yml
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── ROADMAP.md
├── PROJECT_STRUCTURE.md
└── README.md
```

## Installation
```bash
git clone <your-fork-url> movie-rating-analysis
cd movie-rating-analysis
python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```bash
# Full pipeline (loads, cleans, analyzes, writes reports/)
python -m src.main

# Run the notebook
jupyter lab notebooks/01_movie_rating_eda.ipynb

# Run tests
pytest -q
```
Outputs land in `reports/`:
- `report.html`  – standalone summary
- `summary.json` – machine-readable metrics
- `*.png`        – individual charts

## Screenshots & Output
Charts written to `reports/`:
- `rating_distribution.png`
- `top_movies.png`
- `genre_average.png`
- `ratings_over_time.png`

## Working
1. **Ingest** raw MovieLens-style CSVs.
2. **Validate** schema and dtypes.
3. **Clean** – drop duplicates, coerce timestamps, explode multi-genre rows.
4. **Analyze** – compute per-movie/per-genre stats using a Bayesian shrinkage estimator
   `WR = (v/(v+m))*R + (m/(v+m))*C` where `C` is the global mean.
5. **Visualize** and **report**.

## Example
```
>>> python -m src.main
[INFO] loaded 9742 movies / 100836 ratings
[INFO] cleaned dataset: 100836 rows, 0 nulls
[INFO] top movie: 'Shawshank Redemption' (WR=4.41, votes=317)
[INFO] report written to reports/report.html
```

## Testing
```bash
pytest -q
```
Covers: loader schema, cleaner idempotency, weighted-rating math, genre explode.

## Troubleshooting
| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: src` | run from project root, or `pip install -e .` |
| Empty charts | ensure `data/raw/*.csv` exist and are non-empty |
| Font warnings on Linux | `sudo apt install fonts-dejavu` |

## Future Improvements
- Swap sample CSV for full MovieLens 25M via a `make data` target
- Add collaborative-filtering recommender baseline
- Streamlit dashboard for interactive exploration
- Dockerfile + docker-compose

## Acknowledgements
- CODTECH Internship Program
- GroupLens Research (MovieLens dataset format)
- The open-source Python data stack

## References
- MovieLens: https://grouplens.org/datasets/movielens/
- IMDB weighted rating formula
- "Python for Data Analysis" – Wes McKinney

## License
MIT – see [LICENSE](LICENSE).

## Author
**Sumit Kumar**
Intern ID: **CITS3958**
CODTECH Summer Internship
