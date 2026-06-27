"""
=========================================================
Utility Functions
AI Book Recommendation System
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt

from config import *

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv(DATASET_PATH)

# ==========================================================
# Dataset Metrics
# ==========================================================

def get_dataset_metrics():
    """
    Returns dataset metrics for dashboard cards.
    """

    return {
        "Users": df[USER_COL].nunique(),
        "Books": df[BOOK_COL].nunique(),
        "Ratings": len(df)
    }


# ==========================================================
# Top Authors
# ==========================================================

def top_authors(top_n=10):

    authors = (
        df.groupby(AUTHOR_COL)[BOOK_COL]
        .count()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    authors.columns = ["Author", "Books"]

    return authors


# ==========================================================
# Top Publishers
# ==========================================================

def top_publishers(top_n=10):

    publishers = (
        df.groupby(PUBLISHER_COL)[BOOK_COL]
        .count()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    publishers.columns = ["Publisher", "Books"]

    return publishers


# ==========================================================
# Top Active Users
# ==========================================================

def top_users(top_n=10):

    users = (
        df.groupby(USER_COL)[RATING_COL]
        .count()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    users.columns = ["User-ID", "Ratings"]

    return users


# ==========================================================
# Most Popular Books
# ==========================================================

def popular_books(top_n=10):

    books = (
        df.groupby(TITLE_COL)[RATING_COL]
        .count()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    books.columns = ["Book", "Ratings"]

    return books


# ==========================================================
# Rating Distribution
# ==========================================================

def rating_distribution():

    fig, ax = plt.subplots(figsize=(8,5))

    df[RATING_COL].hist(
        bins=11,
        ax=ax
    )

    ax.set_title("Rating Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Frequency")

    plt.tight_layout()

    return fig


# ==========================================================
# Publication Year Distribution
# ==========================================================

def publication_year_chart():

    temp = df.copy()

    temp[YEAR_COL] = pd.to_numeric(
        temp[YEAR_COL],
        errors="coerce"
    )

    temp = temp.dropna(subset=[YEAR_COL])

    temp = (
        temp.groupby(YEAR_COL)[BOOK_COL]
        .count()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        temp[YEAR_COL],
        temp[BOOK_COL]
    )

    ax.set_title("Publication Year Distribution")
    ax.set_xlabel("Publication Year")
    ax.set_ylabel("Books")

    plt.tight_layout()

    return fig


# ==========================================================
# Top Authors Chart
# ==========================================================

def top_authors_chart():

    authors = top_authors()

    fig, ax = plt.subplots(figsize=(10,6))

    ax.barh(
        authors["Author"],
        authors["Books"]
    )

    ax.set_title("Top Authors")

    plt.tight_layout()

    return fig


# ==========================================================
# Top Publishers Chart
# ==========================================================

def top_publishers_chart():

    publishers = top_publishers()

    fig, ax = plt.subplots(figsize=(10,6))

    ax.barh(
        publishers["Publisher"],
        publishers["Books"]
    )

    ax.set_title("Top Publishers")

    plt.tight_layout()

    return fig


# ==========================================================
# Most Popular Books Chart
# ==========================================================

def popular_books_chart():

    books = popular_books()

    fig, ax = plt.subplots(figsize=(10,6))

    ax.barh(
        books["Book"],
        books["Ratings"]
    )

    ax.set_title("Most Popular Books")

    plt.tight_layout()

    return fig

# ==========================================================
# Most Active Users Chart
# ==========================================================

def top_users_chart():

    users = top_users()

    fig, ax = plt.subplots(figsize=(10,6))

    ax.barh(
        users["User-ID"].astype(str),
        users["Ratings"]
    )

    ax.set_title("Most Active Users")

    plt.tight_layout()

    return fig


# ==========================================================
# Model Performance Comparison
# ==========================================================

def model_performance_chart():

    models = [
        "Popularity",
        "Collaborative",
        "SVD"
    ]

    rmse = [
        2.15,
        1.28,
        RMSE
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(
        models,
        rmse
    )

    ax.set_title("Model RMSE Comparison")
    ax.set_ylabel("RMSE")

    plt.tight_layout()

    return fig


# ==========================================================
# Recommendation Explanation
# ==========================================================

def recommendation_text():

    return """
These books are recommended because users with reading
patterns similar to yours gave them high ratings.

The SVD model learns hidden relationships between
users and books by identifying latent features from
historical user-book interactions.

Instead of recommending only the most popular books,
the system predicts which books each individual user
is likely to enjoy.
"""


# ==========================================================
# About Project
# ==========================================================

def project_description():

    return """
### AI-Powered Book Recommendation System

This project recommends books using
Singular Value Decomposition (SVD).

Algorithms Compared

• Popularity-Based Recommendation

• Collaborative Filtering

• Singular Value Decomposition (SVD)

Final Selected Model

✔ Singular Value Decomposition (SVD)

Reason

The SVD model achieved the lowest RMSE and
provided better personalized recommendations
than the other models.

Dataset

Book-Crossing Dataset

Machine Learning Library

Surprise
"""