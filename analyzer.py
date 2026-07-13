"""CSV ingestion and schema validation."""
from __future__ import annotations
import logging
import pandas as pd
from pathlib import Path

log = logging.getLogger(__name__)

MOVIES_SCHEMA = {"movieId": "int64", "title": "object", "genres": "object"}
RATINGS_SCHEMA = {"userId": "int64", "movieId": "int64",
                  "rating": "float64", "timestamp": "int64"}


def _validate(df: pd.DataFrame, schema: dict, name: str) -> None:
    missing = set(schema) - set(df.columns)
    if missing:
        raise ValueError(f"{name}: missing columns {missing}")


def load_movies(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    _validate(df, MOVIES_SCHEMA, "movies")
    log.info("loaded %d movies", len(df))
    return df


def load_ratings(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    _validate(df, RATINGS_SCHEMA, "ratings")
    log.info("loaded %d ratings", len(df))
    return df
