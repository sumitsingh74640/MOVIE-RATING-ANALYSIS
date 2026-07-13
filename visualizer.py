"""Cleaning + feature engineering."""
from __future__ import annotations
import pandas as pd


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["userId", "movieId"]).copy()
    df = df.dropna(subset=["rating"])
    df["rating"] = df["rating"].clip(0.5, 5.0)
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")
    df["year"] = df["datetime"].dt.year
    return df.reset_index(drop=True)


def clean_movies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["movieId"]).copy()
    df["genres"] = df["genres"].fillna("(no genres listed)")
    # Extract release year from title "Movie (1994)"
    df["release_year"] = df["title"].str.extract(r"\((\d{4})\)").astype("float")
    return df.reset_index(drop=True)


def explode_genres(movies: pd.DataFrame) -> pd.DataFrame:
    out = movies.assign(genre=movies["genres"].str.split("|")).explode("genre")
    return out.reset_index(drop=True)
