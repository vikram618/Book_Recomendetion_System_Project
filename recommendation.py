import pickle
import pandas as pd
import numpy as np
from functools import lru_cache

from config import *

# ==========================================================
# Load Model
# ==========================================================

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv(DATASET_PATH)

# Remove duplicates
df = df.drop_duplicates()

# Book Information
books = (
    df[
        [
            BOOK_COL,
            TITLE_COL,
            AUTHOR_COL,
            PUBLISHER_COL,
            YEAR_COL,
        ]
    ]
    .drop_duplicates()
)

# ==========================================================
# Statistics
# ==========================================================

TOTAL_USERS = df[USER_COL].nunique()
TOTAL_BOOKS = df[BOOK_COL].nunique()
TOTAL_RATINGS = len(df)

# ==========================================================
# Autocomplete
# ==========================================================

@lru_cache(maxsize=1)
def get_book_titles():
    """
    Returns sorted book titles for autocomplete.
    """
    return sorted(df[TITLE_COL].dropna().unique())


# ==========================================================
# Get User IDs
# ==========================================================

@lru_cache(maxsize=1)
def get_user_ids():

    return sorted(df[USER_COL].unique())


# ==========================================================
# Cover Image
# ==========================================================

def get_cover(isbn):

    return BOOK_COVER_URL.format(str(isbn))


# ==========================================================
# Search Books
# ==========================================================

def search_books(keyword):

    keyword = keyword.lower()

    result = books[
        books[TITLE_COL].str.lower().str.contains(
            keyword,
            na=False,
        )
    ]

    return result


# ==========================================================
# Similar Books
# ==========================================================

def get_similar_books(book_title, top_n=10):
    """
    Popular books by same author.
    (Can later be replaced with latent similarity.)
    """

    row = books[
        books[TITLE_COL] == book_title
    ]

    if row.empty:

        return pd.DataFrame()

    author = row.iloc[0][AUTHOR_COL]

    rec = books[
        books[AUTHOR_COL] == author
    ].copy()

    rec = rec[
        rec[TITLE_COL] != book_title
    ]

    rec["Predicted Rating"] = np.nan

    return rec.head(top_n)


# ==========================================================
# Personalized Recommendation
# ==========================================================

def get_recommendations(user_id, top_n=10):

    if user_id not in df[USER_COL].values:

        return pd.DataFrame()

    rated_books = set(

        df[
            df[USER_COL] == user_id
        ][BOOK_COL]

    )

    unseen = books[
        ~books[BOOK_COL].isin(rated_books)
    ]

    predictions = []

    for isbn in unseen[BOOK_COL]:

        pred = model.predict(user_id, isbn)

        predictions.append(

            (
                isbn,
                pred.est,
            )

        )

    prediction_df = pd.DataFrame(

        predictions,

        columns=[

            BOOK_COL,

            "Predicted Rating",

        ],

    )

    recommendation = prediction_df.merge(

        books,

        on=BOOK_COL,

        how="left",

    )

    recommendation = recommendation.sort_values(

        "Predicted Rating",

        ascending=False,

    )

    recommendation = recommendation.head(top_n)

    recommendation["Cover"] = recommendation[
        BOOK_COL
    ].apply(get_cover)

    return recommendation.reset_index(drop=True)


# ==========================================================
# Recommendation Explanation
# ==========================================================

def recommendation_reason():

    return (
        "These books are recommended because the "
        "SVD model learned hidden relationships "
        "between readers and books. "
        "Based on your previous ratings, "
        "the model predicts that these books "
        "are likely to match your interests."
    )


# ==========================================================
# Dataset Metrics
# ==========================================================

def dataset_metrics():

    return {

        "Users": TOTAL_USERS,

        "Books": TOTAL_BOOKS,

        "Ratings": TOTAL_RATINGS,

    }


# ==========================================================
# Book Details
# ==========================================================

def get_book_details(isbn):

    book = books[
        books[BOOK_COL] == isbn
    ]

    if book.empty:

        return None

    return book.iloc[0]