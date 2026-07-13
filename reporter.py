"""Statistical analysis."""
from __future__ import annotations
import pandas as pd
from .config import MIN_VOTES, TOP_N


def weighted_rating(stats: pd.DataFrame, min_votes: int, global_mean: float) -> pd.Series:
    v = stats["votes"]
    r = stats["mean"]
    return (v / (v + min_votes)) * r + (min_votes / (v + min_votes)) * global_mean


def movie_stats(ratings: pd.DataFrame, movies: pd.DataFrame,
                min_votes: int = MIN_VOTES) -> pd.DataFrame:
    g = ratings.groupby("movieId")["rating"].agg(["mean", "count"]).rename(
        columns={"count": "votes"})
    g["weighted"] = weighted_rating(g, min_votes, ratings["rating"].mean())
    return g.merge(movies[["movieId", "title", "genres"]], on="movieId").sort_values(
        "weighted", ascending=False)


def top_movies(stats: pd.DataFrame, n: int = TOP_N) -> pd.DataFrame:
    return stats[stats["votes"] >= MIN_VOTES].head(n).reset_index(drop=True)


def genre_stats(ratings: pd.DataFrame, movies_exploded: pd.DataFrame) -> pd.DataFrame:
    merged = ratings.merge(movies_exploded[["movieId", "genre"]], on="movieId")
    g = merged.groupby("genre")["rating"].agg(["mean", "count"]).rename(
        columns={"count": "votes"}).sort_values("mean", ascending=False)
    return g.reset_index()


def ratings_over_time(ratings: pd.DataFrame) -> pd.DataFrame:
    return ratings.groupby("year")["rating"].agg(["mean", "count"]).reset_index()
