"""Chart generation."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="viridis")


def save_rating_distribution(ratings, out: Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(ratings["rating"], bins=10, ax=ax, kde=False)
    ax.set_title("Rating Distribution")
    ax.set_xlabel("Rating"); ax.set_ylabel("Count")
    fig.tight_layout(); fig.savefig(out, dpi=110); plt.close(fig)
    return out


def save_top_movies(top, out: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=top, y="title", x="weighted", ax=ax)
    ax.set_title("Top Movies (Bayesian Weighted Rating)")
    ax.set_xlabel("Weighted rating"); ax.set_ylabel("")
    fig.tight_layout(); fig.savefig(out, dpi=110); plt.close(fig)
    return out


def save_genre_average(genre, out: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=genre, y="genre", x="mean", ax=ax)
    ax.set_title("Average Rating by Genre")
    ax.set_xlabel("Mean rating"); ax.set_ylabel("")
    fig.tight_layout(); fig.savefig(out, dpi=110); plt.close(fig)
    return out


def save_ratings_over_time(ts, out: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(ts["year"], ts["mean"], marker="o")
    ax.set_title("Mean Rating Over Time")
    ax.set_xlabel("Year"); ax.set_ylabel("Mean rating")
    fig.tight_layout(); fig.savefig(out, dpi=110); plt.close(fig)
    return out
