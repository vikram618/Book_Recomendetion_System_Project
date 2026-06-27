"""
=========================================================
Configuration File
AI Book Recommendation System
=========================================================
"""

# =========================================================
# FILE PATHS
# =========================================================

DATASET_PATH = "final_dataset.csv"
MODEL_PATH = "svd_model.pkl"

# =========================================================
# APP CONFIGURATION
# =========================================================

APP_TITLE = "📚 AI-Powered Book Recommendation System"

APP_SUBTITLE = (
    "Discover books you'll love with Machine Learning "
    "using Singular Value Decomposition (SVD)."
)

PAGE_TITLE = "Book Recommendation System"

PAGE_ICON = "📚"

LAYOUT = "wide"

# =========================================================
# SIDEBAR
# =========================================================

SIDEBAR_TITLE = "📖 Navigation"

MENU_OPTIONS = [
    "🏠 Home",
    "📚 Recommendations",
    "📈 Model Performance",
    "📊 Dataset Statistics",
    "ℹ️ About Project"
]

# =========================================================
# MODEL INFORMATION
# =========================================================

MODEL_NAME = "Singular Value Decomposition (SVD)"

RMSE = 0.91
MAE = 0.72

TRAINING_TIME = "Approx. 2 minutes"
PREDICTION_TIME = "< 1 second"

# =========================================================
# RECOMMENDATION SETTINGS
# =========================================================

DEFAULT_RECOMMENDATIONS = 10

MIN_RECOMMENDATIONS = 5

MAX_RECOMMENDATIONS = 20

# =========================================================
# DATASET COLUMN NAMES
# (Keep exactly as in your final_dataset.csv)
# =========================================================

USER_COL = "User-ID"

BOOK_COL = "ISBN"

RATING_COL = "Book-Rating"

TITLE_COL = "Book-Title"

AUTHOR_COL = "Book-Author"

YEAR_COL = "Year-Of-Publication"

PUBLISHER_COL = "Publisher"

LOCATION_COL = "Location"

AGE_COL = "Age"

COUNTRY_COL = "Country"

# =========================================================
# BOOK COVER API
# =========================================================

BOOK_COVER_URL = (
    "https://covers.openlibrary.org/b/isbn/{}-L.jpg"
)

# =========================================================
# COLORS
# =========================================================

PRIMARY_COLOR = "#2563EB"

SECONDARY_COLOR = "#4F46E5"

SUCCESS_COLOR = "#22C55E"

WARNING_COLOR = "#F59E0B"

ERROR_COLOR = "#EF4444"

BACKGROUND_COLOR = "#0E1117"

CARD_COLOR = "#262730"

TEXT_COLOR = "#FFFFFF"

# =========================================================
# METRIC CARD TITLES
# =========================================================

USERS_TITLE = "👥 Users"

BOOKS_TITLE = "📚 Books"

RATINGS_TITLE = "⭐ Ratings"

# =========================================================
# PAGE TITLES
# =========================================================

HOME_PAGE = "🏠 Home"

RECOMMENDATION_PAGE = "📚 Recommendations"

MODEL_PAGE = "📈 Model Performance"

STATISTICS_PAGE = "📊 Dataset Statistics"

ABOUT_PAGE = "ℹ️ About Project"