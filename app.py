# ==========================================================
# AI Book Recommendation System
# app.py (Part 1)
# ==========================================================

import streamlit as st
import pandas as pd

from config import *
from style import load_css

from recommendation import (
    dataset_metrics,
    get_book_titles,
    get_user_ids,
    get_recommendations,
    get_similar_books,
    recommendation_reason
)

from utils import (
    rating_distribution,
    publication_year_chart,
    top_authors_chart,
    top_publishers_chart,
    popular_books_chart,
    top_users_chart,
    model_performance_chart,
    project_description
)

# ----------------------------------------------------------
# Streamlit Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# Load Custom CSS
load_css()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.title("📖 Navigation")

page = st.sidebar.radio(
    "",
    MENU_OPTIONS
)

st.sidebar.markdown("---")

st.sidebar.subheader("⚙ Recommendation Model")

st.sidebar.success("✔ SVD (Final Model)")

st.sidebar.metric(
    "RMSE",
    RMSE
)

st.sidebar.metric(
    "MAE",
    MAE
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
This recommendation engine uses
**Singular Value Decomposition (SVD)**

The model predicts books
based on hidden user-book
interaction patterns.
"""
)

# ----------------------------------------------------------
# HOME PAGE
# ----------------------------------------------------------

if page == "🏠 Home":

    st.markdown(
        """
        <div class='hero'>
            <h1>📚 AI-Powered Book Recommendation System</h1>

            <p>
            Discover books you'll love using
            Machine Learning and
            Singular Value Decomposition (SVD).
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Dashboard")

    metrics = dataset_metrics()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-title'>
                    👥 Users
                </div>

                <div class='metric-value'>
                    {metrics["Users"]:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-title'>
                    📚 Books
                </div>

                <div class='metric-value'>
                    {metrics["Books"]:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-title'>
                    ⭐ Ratings
                </div>

                <div class='metric-value'>
                    {metrics["Ratings"]:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        """
Welcome to the **AI Book Recommendation System**.

This application recommends books using a trained
**Singular Value Decomposition (SVD)** model.

Navigate to **Recommendations** from the sidebar
to search by **Book Title** or **User ID**.
"""
    )

# ==========================================================
# RECOMMENDATIONS PAGE
# ==========================================================

elif page == "📚 Recommendations":

    st.title("📚 Book Recommendation System")

    st.write(
        "Choose one of the following recommendation methods."
    )

    st.divider()

    # ------------------------------------------------------
    # Search by Book Title
    # ------------------------------------------------------

    st.subheader("🔍 Search by Book Title")

    titles = get_book_titles()

    selected_book = st.selectbox(
        "Select a Book",
        options=titles,
        index=None,
        placeholder="Type or search a book title..."
    )

    if st.button("📖 Get Similar Books"):

        if selected_book:

            with st.spinner("Finding similar books..."):

                books = get_similar_books(selected_book)

            if books.empty:

                st.warning("No recommendations found.")

            else:

                st.success(
                    f"Books similar to '{selected_book}'"
                )

                for _, row in books.iterrows():

                    with st.container():

                        c1, c2 = st.columns([1, 4])

                        with c1:

                            st.image(
                                f"https://covers.openlibrary.org/b/isbn/{row[BOOK_COL]}-L.jpg",
                                width=120
                            )

                        with c2:

                            st.markdown(
                                f"### {row[TITLE_COL]}"
                            )

                            st.write(
                                f"**Author:** {row[AUTHOR_COL]}"
                            )

                            st.write(
                                f"**Publisher:** {row[PUBLISHER_COL]}"
                            )

                            st.write(
                                f"**Year:** {row[YEAR_COL]}"
                            )

                            with st.expander("View Details"):

                                st.write(
                                    f"ISBN : {row[BOOK_COL]}"
                                )

                                st.write(
                                    "Recommendation Type : Similar Book"
                                )

                    st.divider()

    st.divider()

    # ------------------------------------------------------
    # Search by User ID
    # ------------------------------------------------------

    st.subheader("👤 Personalized Recommendation")

    users = get_user_ids()

    user = st.selectbox(
        "Select User ID",
        users
    )

    top_n = st.slider(
        "Number of Recommendations",
        5,
        20,
        10
    )

    if st.button("🔍 Get Personalized Recommendations"):

        with st.spinner(
            "Generating recommendations..."
        ):

            recommendations = get_recommendations(
                user,
                top_n
            )

        if recommendations.empty:

            st.error("User not found.")

        else:

            st.success(
                f"Top {top_n} Recommended Books"
            )

            for _, row in recommendations.iterrows():

                c1, c2 = st.columns([1,4])

                with c1:

                    st.image(
                        row["Cover"],
                        width=120
                    )

                with c2:

                    st.markdown(
                        f"## {row[TITLE_COL]}"
                    )

                    st.write(
                        f"**Author:** {row[AUTHOR_COL]}"
                    )

                    st.write(
                        f"**Publisher:** {row[PUBLISHER_COL]}"
                    )

                    st.write(
                        f"**Year:** {row[YEAR_COL]}"
                    )

                    st.success(
                        f"⭐ Predicted Rating : {row['Predicted Rating']:.2f}"
                    )

                    with st.expander(
                        "View Details"
                    ):

                        st.write(
                            f"ISBN : {row[BOOK_COL]}"
                        )

                        st.write(
                            f"Book Title : {row[TITLE_COL]}"
                        )

                        st.write(
                            f"Author : {row[AUTHOR_COL]}"
                        )

                        st.write(
                            f"Publisher : {row[PUBLISHER_COL]}"
                        )

                        st.write(
                            f"Publication Year : {row[YEAR_COL]}"
                        )

                st.divider()

            # ------------------------------------------
            # Download CSV
            # ------------------------------------------

            csv = recommendations.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="📥 Download Recommendations",
                data=csv,
                file_name="recommended_books.csv",
                mime="text/csv"
            )

            st.info(
                recommendation_reason()
            )


# ==========================================================
# DATASET STATISTICS PAGE
# ==========================================================

elif page == "📊 Dataset Statistics":

    st.title("📊 Dataset Statistics")

    st.markdown(
        "Explore insights from the final Book Recommendation dataset."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(top_authors_chart())

    with col2:
        st.pyplot(top_publishers_chart())

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.pyplot(rating_distribution())

    with col4:
        st.pyplot(publication_year_chart())

    st.divider()

    col5, col6 = st.columns(2)

    with col5:
        st.pyplot(popular_books_chart())

    with col6:
        st.pyplot(top_users_chart())


# ==========================================================
# MODEL PERFORMANCE PAGE
# ==========================================================

elif page == "📈 Model Performance":

    st.title("📈 Model Performance")

    st.write(
        "Performance comparison of all recommendation models."
    )

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "RMSE",
            RMSE
        )

    with c2:
        st.metric(
            "MAE",
            MAE
        )

    st.metric(
        "Training Time",
        TRAINING_TIME
    )

    st.metric(
        "Prediction Time",
        PREDICTION_TIME
    )

    st.divider()

    st.pyplot(model_performance_chart())

    st.success(
        """
🏆 Best Model

Singular Value Decomposition (SVD)

The SVD model achieved the lowest RMSE
and provides better personalized
recommendations than the other models.
"""
    )


# ==========================================================
# ABOUT PAGE
# ==========================================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About Project")

    st.markdown(project_description())

    st.divider()

    st.subheader("Workflow")

    st.markdown("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis

4. Popularity-Based Recommendation

5. Collaborative Filtering

6. Singular Value Decomposition (SVD)

7. Personalized Book Recommendation

8. Streamlit Deployment
""")

    st.divider()

    st.subheader("Dataset")

    st.info(
        """
Book-Crossing Dataset

Contains information about:

• Users

• Books

• Ratings

The final dataset was cleaned and
combined before training the SVD model.
"""
    )

    st.divider()

    st.subheader("Recommendation Engine")

    st.success(
        """
The recommendation engine predicts
books that a user has not rated.

Instead of recommending only the
most popular books, SVD identifies
hidden relationships between users
and books using latent factors.
"""
    )

    st.divider()

    st.subheader("Future Improvements")

    st.markdown("""
- Add user login

- Book cover caching

- Hybrid recommendation

- Deep Learning models

- Real-time recommendations

- Cloud database integration

- User feedback system
""")