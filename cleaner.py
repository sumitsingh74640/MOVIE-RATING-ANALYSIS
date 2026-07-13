"""Central configuration: paths and constants."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

MOVIES_CSV = DATA_RAW / "movies.csv"
RATINGS_CSV = DATA_RAW / "ratings.csv"

# Bayesian shrinkage prior: minimum votes required to be listed in Top-N.
MIN_VOTES = 20
TOP_N = 10
