# ================================================================
# BOOK RECOMMENDATION SYSTEM — STREAMLIT APP
# Model: SVD (Matrix Factorization)
# Run: streamlit run app.py
# ================================================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title = "📚 Book Recommendation System",
    page_icon  = "📚",
    layout     = "wide",
    initial_sidebar_state = "expanded"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        padding: 10px 0;
    }
    .sub-title {
        font-size: 18px;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
    }
    .book-card {
        background: #F8F9FA;
        border-left: 4px solid #2980B9;
        padding: 12px 16px;
        border-radius: 8px;
        margin: 8px 0;
    }
    .popular-card {
        background: #FFF9F0;
        border-left: 4px solid #E67E22;
        padding: 12px 16px;
        border-radius: 8px;
        margin: 8px 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #2980B9, #1ABC9C);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 30px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1ABC9C, #2980B9);
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)


# ── Load Model & Data ─────────────────────────────────────────
@st.cache_resource
def load_model():
    model = pickle.load(open('svd_model.pkl', 'rb'))
    return model

@st.cache_data
def load_data():
    df         = pd.read_csv('final_dataset_app.csv')
    books_info = pd.read_csv('books_info.csv')
    pop_books  = pd.read_csv('popular_books.csv')
    user_list  = pickle.load(open('user_list.pkl', 'rb'))
    return df, books_info, pop_books, user_list

# Load everything
try:
    svd_model            = load_model()
    df, books_info, pop_books, user_list = load_data()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"Error loading model/data: {e}")
    st.stop()


# ── Recommendation Functions ──────────────────────────────────
def recommend_svd(user_id, n=10):
    """SVD based personalized recommendations"""
    rated_books   = set(df[df['User-ID'] == user_id]['ISBN'].values)
    all_books     = books_info['ISBN'].values
    unrated_books = [isbn for isbn in all_books if isbn not in rated_books]

    preds = []
    for isbn in unrated_books:
        pred = svd_model.predict(user_id, isbn)
        preds.append((isbn, round(pred.est, 2)))

    preds.sort(key=lambda x: x[1], reverse=True)
    top_isbns = [p[0] for p in preds[:n]]
    top_scores = dict(preds[:n])

    recs = books_info[books_info['ISBN'].isin(top_isbns)].copy()
    recs['Predicted Rating'] = recs['ISBN'].map(top_scores)
    recs = recs.sort_values('Predicted Rating', ascending=False).reset_index(drop=True)
    recs.index += 1
    return recs

def get_user_history(user_id, n=5):
    """Get books already rated by user"""
    history = (df[df['User-ID'] == user_id]
               .sort_values('Book-Rating', ascending=False)
               [['Book-Title','Book-Author','Book-Rating']]
               .drop_duplicates('Book-Title')
               .head(n)
               .reset_index(drop=True))
    history.index += 1
    return history


# ================================================================
# MAIN APP LAYOUT
# ================================================================

# ── Header ────────────────────────────────────────────────────
st.markdown('<div class="main-title">📚 Book Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Powered by SVD Matrix Factorization | Book-Crossing Dataset</div>', unsafe_allow_html=True)
st.markdown("---")

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/book-shelf.png", width=80)
    st.markdown("## ⚙️ Settings")
    st.markdown("---")

    mode = st.radio(
        "Choose Mode",
        ["🎯 Personalized (SVD)", "🔥 Popular Books", "📊 Model Info"],
        index=0
    )

    st.markdown("---")
    st.markdown("### 📈 Model Performance")
    st.markdown("| Metric | Score |")
    st.markdown("|--------|-------|")
    st.markdown("| RMSE   | 1.5973 |")
    st.markdown("| MAE    | 1.2352 |")
    st.markdown("| Rank   | 🥇 Best |")

    st.markdown("---")
    st.markdown("### 📦 Dataset Info")
    st.metric("Total Users",   f"{df['User-ID'].nunique():,}")
    st.metric("Total Books",   f"{books_info.shape[0]:,}")
    st.metric("Total Ratings", f"{len(df):,}")


# ================================================================
# MODE 1: PERSONALIZED SVD RECOMMENDATIONS
# ================================================================
if mode == "🎯 Personalized (SVD)":
    st.markdown("## 🎯 Personalized Book Recommendations")
    st.markdown("Select a User ID to get personalized book recommendations using SVD!")

    col1, col2 = st.columns([2, 1])

    with col1:
        # User ID input
        user_input_method = st.radio(
            "How to select User?",
            ["Select from list", "Type User ID"],
            horizontal=True
        )

        if user_input_method == "Select from list":
            selected_user = st.selectbox(
                "Select User ID",
                options=user_list[:500],   # show first 500 users
                help="Select a user to get recommendations"
            )
        else:
            selected_user = st.number_input(
                "Enter User ID",
                min_value=int(min(user_list)),
                max_value=int(max(user_list)),
                value=int(user_list[0]),
                step=1
            )

        n_recs = st.slider("Number of Recommendations", min_value=5, max_value=20, value=10)

    with col2:
        st.markdown("### 👤 User Summary")
        user_data = df[df['User-ID'] == selected_user]
        st.metric("Books Rated",    len(user_data))
        st.metric("Avg Rating Given", f"{user_data['Book-Rating'].mean():.1f}" if len(user_data) > 0 else "N/A")
        if 'Age' in user_data.columns:
            age = user_data['Age'].iloc[0] if len(user_data) > 0 else "N/A"
            st.metric("Age", age)
        if 'Country' in user_data.columns:
            country = user_data['Country'].iloc[0] if len(user_data) > 0 else "N/A"
            st.metric("Country", str(country)[:20])

    st.markdown("---")

    if st.button("🚀 Get Recommendations"):
        with st.spinner("Finding best books for you using SVD..."):

            col_hist, col_recs = st.columns([1, 2])

            with col_hist:
                st.markdown("### 📖 User's Reading History")
                st.markdown("*(Books they rated highest)*")
                history = get_user_history(selected_user, n=5)
                if len(history) > 0:
                    for _, row in history.iterrows():
                        stars = "⭐" * int(row['Book-Rating'])
                        st.markdown(f"""
                        <div class="book-card">
                            <b>{row['Book-Title'][:45]}</b><br>
                            <small>✍️ {row['Book-Author']}</small><br>
                            <small>{stars} {row['Book-Rating']}/10</small>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No rating history found for this user.")

            with col_recs:
                st.markdown(f"### 🎯 Top {n_recs} Recommended Books")
                st.markdown("*(Predicted by SVD Model)*")
                try:
                    recs = recommend_svd(selected_user, n=n_recs)
                    for _, row in recs.iterrows():
                        rating_bar = "🟦" * int(row['Predicted Rating'])
                        st.markdown(f"""
                        <div class="book-card">
                            <b>#{_} {row['Book-Title'][:50]}</b><br>
                            <small>✍️ {row['Book-Author']}</small><br>
                            <small>⭐ Predicted Rating: <b>{row['Predicted Rating']}/10</b></small>
                        </div>
                        """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Could not generate recommendations: {e}")


# ================================================================
# MODE 2: POPULAR BOOKS
# ================================================================
elif mode == "🔥 Popular Books":
    st.markdown("## 🔥 Most Popular Books")
    st.markdown("Best books based on ratings from all users — great for new users!")

    col1, col2 = st.columns([1, 1])

    with col1:
        min_ratings = st.slider("Minimum number of ratings", 50, 500, 100, step=50)

    with col2:
        top_n = st.slider("Number of books to show", 5, 50, 10)

    filtered_pop = (pop_books[pop_books['Num Ratings'] >= min_ratings]
                    .head(top_n)
                    .reset_index(drop=True))
    filtered_pop.index += 1

    st.markdown("---")
    st.markdown(f"### 📚 Top {top_n} Books (min {min_ratings} ratings)")

    col_a, col_b = st.columns([2, 1])

    with col_a:
        for _, row in filtered_pop.iterrows():
            st.markdown(f"""
            <div class="popular-card">
                <b>#{_} {row['Book-Title'][:55]}</b><br>
                <small>✍️ {row['Book-Author']}</small><br>
                <small>⭐ Avg Rating: <b>{row['Avg Rating']:.2f}/10</b>
                &nbsp;|&nbsp; 👥 {int(row['Num Ratings'])} ratings</small>
            </div>
            """, unsafe_allow_html=True)

    with col_b:
        st.markdown("### 📊 Quick Stats")
        st.metric("Books shown",      len(filtered_pop))
        st.metric("Highest Rating",   f"{filtered_pop['Avg Rating'].max():.2f}")
        st.metric("Most Rated Book",  f"{int(filtered_pop['Num Ratings'].max())} ratings")

        # Mini bar chart
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(5, 4))
        top5 = filtered_pop.head(5)
        short = [t[:20]+'…' for t in top5['Book-Title']]
        ax.barh(short[::-1], top5['Avg Rating'][::-1], color='#E67E22', edgecolor='white')
        ax.set_xlim(8, 10)
        ax.set_title('Top 5 Avg Ratings', fontsize=10, fontweight='bold')
        ax.set_facecolor('#F7F9FC')
        fig.patch.set_facecolor('#F7F9FC')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


# ================================================================
# MODE 3: MODEL INFO
# ================================================================
elif mode == "📊 Model Info":
    st.markdown("## 📊 Model Performance & Comparison")

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Popularity RMSE",   "1.8028", delta=None)
    with col2:
        st.metric("User-CF RMSE",      "2.0373", delta=None)
    with col3:
        st.metric("Item-CF RMSE",      "1.7580", delta=None)
    with col4:
        st.metric("SVD RMSE ✅",        "1.5973", delta="-0.1607 vs Item-CF")

    st.markdown("---")

    col_chart, col_info = st.columns([2, 1])

    with col_chart:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.patch.set_facecolor('#F7F9FC')

        models    = ['Popularity', 'User-CF', 'Item-CF', 'SVD']
        rmse_vals = [1.8028, 2.0373, 1.7580, 1.5973]
        mae_vals  = [1.4456, 1.5584, 1.2610, 1.2352]
        colors    = ['#3498DB','#E74C3C','#E67E22','#27AE60']

        axes[0].bar(models, rmse_vals, color=colors, edgecolor='white', width=0.5)
        axes[0].set_title('RMSE Comparison', fontweight='bold')
        axes[0].set_ylim(1.3, 2.2)
        axes[0].set_facecolor('#F7F9FC')
        for i, v in enumerate(rmse_vals):
            axes[0].text(i, v+0.01, f'{v:.4f}', ha='center', fontsize=9, fontweight='bold')

        axes[1].bar(models, mae_vals, color=colors, edgecolor='white', width=0.5)
        axes[1].set_title('MAE Comparison', fontweight='bold')
        axes[1].set_ylim(1.0, 1.8)
        axes[1].set_facecolor('#F7F9FC')
        for i, v in enumerate(mae_vals):
            axes[1].text(i, v+0.01, f'{v:.4f}', ha='center', fontsize=9, fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col_info:
        st.markdown("### 🏆 Why SVD Wins?")
        st.markdown("""
        ✅ **Lowest RMSE** (1.5973)
        
        ✅ **Lowest MAE** (1.2352)
        
        ✅ Handles **sparse data** well
        
        ✅ Finds **hidden patterns** in ratings
        
        ✅ Fully **personalized** for each user
        
        ✅ Used by **Netflix & Amazon**
        """)

        st.markdown("### 📐 SVD Parameters")
        st.markdown("""
        | Parameter | Value |
        |-----------|-------|
        | n_factors | 50 |
        | n_epochs  | 20 |
        | lr_all    | 0.005 |
        | reg_all   | 0.02 |
        """)

    st.markdown("---")
    st.markdown("### 🔄 How SVD Works")
    st.markdown("""
    1. **Load** user-book rating matrix
    2. **Decompose** into 3 smaller matrices using SVD
    3. **Learn** hidden features (genres, styles, themes)
    4. **Predict** missing ratings using learned features
    5. **Recommend** top books with highest predicted ratings
    """)

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center><small>📚 Book Recommendation System | Built with SVD Matrix Factorization | "
    "Book-Crossing Dataset</small></center>",
    unsafe_allow_html=True
)
