import pandas as pd
from src.cleaner import clean_ratings, clean_movies, explode_genres

def test_clean_ratings_dedup():
    df = pd.DataFrame({"userId":[1,1,2],"movieId":[10,10,10],
                       "rating":[4.0,4.0,5.0],"timestamp":[1,1,2]})
    out = clean_ratings(df)
    assert len(out) == 2
    assert "datetime" in out.columns and "year" in out.columns

def test_clean_movies_year_extract():
    df = pd.DataFrame({"movieId":[1],"title":["Foo (1999)"],"genres":["Drama"]})
    out = clean_movies(df)
    assert out.loc[0,"release_year"] == 1999

def test_explode_genres():
    df = pd.DataFrame({"movieId":[1],"title":["x"],"genres":["A|B|C"]})
    out = explode_genres(df)
    assert set(out["genre"]) == {"A","B","C"}
