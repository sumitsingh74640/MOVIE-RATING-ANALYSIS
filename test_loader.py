"""Orchestrator / CLI entrypoint."""
from __future__ import annotations
import logging
from . import config as C
from .loader import load_movies, load_ratings
from .cleaner import clean_movies, clean_ratings, explode_genres
from .analyzer import movie_stats, top_movies, genre_stats, ratings_over_time
from . import visualizer as viz
from .reporter import render

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
log = logging.getLogger("main")


def run() -> None:
    C.REPORTS.mkdir(parents=True, exist_ok=True)
    C.DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

    movies = clean_movies(load_movies(C.MOVIES_CSV))
    ratings = clean_ratings(load_ratings(C.RATINGS_CSV))

    stats = movie_stats(ratings, movies)
    top = top_movies(stats)
    genres = genre_stats(ratings, explode_genres(movies))
    ts = ratings_over_time(ratings)

    stats.to_csv(C.DATA_PROCESSED / "movie_stats.csv", index=False)
    genres.to_csv(C.DATA_PROCESSED / "genre_stats.csv", index=False)

    viz.save_rating_distribution(ratings, C.REPORTS / "rating_distribution.png")
    viz.save_top_movies(top, C.REPORTS / "top_movies.png")
    viz.save_genre_average(genres, C.REPORTS / "genre_average.png")
    viz.save_ratings_over_time(ts, C.REPORTS / "ratings_over_time.png")

    kpis = {
        "movies": int(movies["movieId"].nunique()),
        "ratings": int(len(ratings)),
        "users": int(ratings["userId"].nunique()),
        "mean_rating": float(ratings["rating"].mean()),
    }
    top_rows = top[["title", "votes", "mean", "weighted"]].to_dict(orient="records")
    out = render(kpis, top_rows, C.REPORTS)
    log.info("report written to %s", out)


if __name__ == "__main__":
    run()
