import pandas as pd
from src.analyzer import movie_stats, top_movies, weighted_rating

def test_weighted_rating_shrinks_low_votes():
    stats = pd.DataFrame({"mean":[5.0, 4.0], "votes":[1, 1000]})
    wr = weighted_rating(stats, min_votes=10, global_mean=3.0)
    assert wr.iloc[0] < 5.0
    assert abs(wr.iloc[1] - 4.0) < 0.05

def test_movie_stats_and_top():
    n = 30
    ratings = pd.DataFrame({
        "userId": list(range(n)),
        "movieId": [1]*n,
        "rating": [5.0]*n,
        "timestamp": [0]*n,
    })
    movies = pd.DataFrame({"movieId":[1],"title":["A"],"genres":["Drama"]})
    s = movie_stats(ratings, movies, min_votes=5)
    assert s.iloc[0]["votes"] == n
    assert not top_movies(s).empty
