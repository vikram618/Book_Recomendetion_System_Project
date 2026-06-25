# Book_Recomendetion_System_Project
# 📚 Book Recommendation System

A complete end-to-end Book Recommendation System built using Machine Learning with SVD (Matrix Factorization) as the final model, deployed using Streamlit.

---

## 🎯 Project Overview

This project recommends books to users based on their reading history and ratings using collaborative filtering techniques. We compared 4 different models and finalized **SVD (Matrix Factorization)** as the best performing model.

---

## 📂 Project Structure

```
BookRecommendation/
│
├── app.py                        # Streamlit web application
├── Book_Recommendation_EDA_Cleaning.py   # EDA + Data Cleaning script
├── Book_Recommendation_Modeling.py       # All 3 CF models script
├── Book_Recommendation_SVD.py            # SVD model script
│
├── svd_model.pkl                 # Trained SVD model (saved)
├── books_info.csv                # Book titles and authors
├── popular_books.csv             # Popular books data
├── final_dataset_app.csv         # Cleaned and merged dataset
├── user_list.pkl                 # List of all user IDs
│
├── requirements.txt              # Required libraries
└── README.md                     # Project documentation
```

---

## 📊 Dataset

**Book-Crossing Dataset**

| File | Description | Rows |
|------|-------------|------|
| `Users.csv` | User details (ID, Location, Age) | 2,78,858 |
| `Books.csv` | Book details (ISBN, Title, Author, Year, Publisher) | 2,71,360 |
| `Ratings.csv` | User ratings for books (1–10) | 11,49,780 |

---

## 🔍 Project Workflow

```
Raw Data
   ↓
EDA (Exploratory Data Analysis)
   ↓
Data Cleaning
   ↓
Model Building (4 Models)
   ↓
Model Evaluation (RMSE & MAE)
   ↓
Best Model Selected (SVD)
   ↓
Deployment (Streamlit App)
```

---

## 🧹 Data Cleaning Steps

- **Age**: Invalid values (< 5 or > 100) replaced with median age (32)
- **Year**: Invalid publication years replaced with median year (1996)
- **Image URLs**: 3 image URL columns dropped (not useful for modeling)
- **Duplicates**: Duplicate rows removed from ratings
- **Implicit Ratings**: Ratings = 0 (implicit) separated from explicit ratings (1–10)
- **Cold Start Filter**: Kept only users and books with ≥ 3 ratings
- **Final Dataset**: 2,02,071 rows, 9 columns, zero null values

---

## 🤖 Models Built

### Model 1 — Popularity Based
- Recommends most rated and highest rated books to everyone
- Used as **baseline model**
- Best for **new users** with no rating history

### Model 2 — User-Based Collaborative Filtering
- Finds users similar to the target user using cosine similarity
- Recommends books that similar users liked
- Uses **KNN (K-Nearest Neighbors)** algorithm

### Model 3 — Item-Based Collaborative Filtering
- Finds books similar to books the user already liked
- Uses **KNN** on item-user matrix
- More stable than User-Based CF

### Model 4 — SVD (Matrix Factorization) ✅ Final Model
- Decomposes the user-item rating matrix into hidden features
- Learns hidden patterns like genre preferences, reading style
- Predicts missing ratings and recommends top books
- **Best performing model** among all 4

---

## 📈 Model Performance Comparison

| Rank | Model | RMSE | MAE |
|------|-------|------|-----|
| 4th | User-Based CF | 2.0373 | 1.5584 |
| 3rd | Popularity Based | 1.8028 | 1.4456 |
| 2nd | Item-Based CF | 1.7580 | 1.2610 |
| 🥇 1st | **SVD** | **1.5973** | **1.2352** |

> SVD improved RMSE by **11.4%** over the baseline Popularity model!

---

## ⚙️ SVD Model Parameters

| Parameter | Value | Meaning |
|-----------|-------|---------|
| n_factors | 50 | Number of hidden features to learn |
| n_epochs | 20 | Number of training iterations |
| lr_all | 0.005 | Learning rate |
| reg_all | 0.02 | Regularization (prevents overfitting) |

---

## 🖥️ Streamlit App Features

- **🎯 Personalized Recommendations** — Select any User ID and get top N book recommendations using SVD
- **🔥 Popular Books** — Most rated and highest rated books (great for new users)
- **📊 Model Info** — Visual comparison of all 4 models with RMSE and MAE charts

---

## 🚀 How to Run the App

### Step 1 — Clone the repository
```bash
git clone https://github.com/your-username/BookRecommendation.git
cd BookRecommendation
```

### Step 2 — Install required libraries
```bash
pip install -r requirements.txt
```

### Step 3 — Run the Streamlit app
```bash
streamlit run app.py
```

### Step 4 — Open in browser
```
http://localhost:8501
```

---

## 📦 Requirements

```
pandas
numpy
scikit-learn
scikit-surprise
scipy
streamlit
matplotlib
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | Machine learning (KNN, metrics) |
| Scikit-surprise | SVD Matrix Factorization |
| Streamlit | Web app deployment |

---

## 💡 Key Learnings

- Real-world datasets have lots of missing values and invalid data — cleaning is very important
- Recommendation systems have extremely sparse matrices (99.99% sparse)
- SVD handles sparsity better than traditional CF methods
- Cold-start problem is a real challenge — popularity model helps as fallback
- Cross-validation gives more reliable model evaluation than single train-test split

---

## 🔮 Future Improvements

- [ ] Add content-based filtering using book title and author features
- [ ] Build a hybrid model combining SVD + Content-Based
- [ ] Add book cover images using Amazon image URLs
- [ ] Deploy on cloud (Streamlit Cloud / Heroku / AWS)
- [ ] Add user registration and real-time rating collection

---

## 👤 Author

**Vicky**
- Project: Book Recommendation System
- Dataset: Book-Crossing Dataset
- Tools: Python, Scikit-Surprise, Streamlit

---

## 📄 License

This project is for educational purposes.

---

⭐ **If you found this project helpful, please give it a star!** ⭐
