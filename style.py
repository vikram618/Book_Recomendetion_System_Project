"""
=========================================================
Professional CSS Styling
AI Book Recommendation System
=========================================================
"""

import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ------------------------------------------------ */
/* Hide Streamlit Default Elements */
/* ------------------------------------------------ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ------------------------------------------------ */
/* Main Page */
/* ------------------------------------------------ */

.stApp{

    background:#F4F7FB;

    color:#222222;

    font-family:'Segoe UI',sans-serif;

}

/* ------------------------------------------------ */
/* Hero Section */
/* ------------------------------------------------ */

.hero{

    background:linear-gradient(90deg,#2563EB,#4F46E5);

    padding:35px;

    border-radius:18px;

    color:white;

    text-align:center;

    margin-bottom:25px;

    box-shadow:0px 6px 18px rgba(0,0,0,0.15);

}

.hero h1{

    font-size:42px;

    font-weight:700;

    margin-bottom:10px;

}

.hero p{

    font-size:18px;

}

/* ------------------------------------------------ */
/* Metric Cards */
/* ------------------------------------------------ */

.metric-card{

    background:white;

    padding:25px;

    border-radius:15px;

    box-shadow:0px 5px 12px rgba(0,0,0,.12);

    text-align:center;

    transition:0.3s;

}

.metric-card:hover{

    transform:translateY(-5px);

}

.metric-title{

    color:#555;

    font-size:18px;

}

.metric-value{

    font-size:34px;

    font-weight:bold;

    color:#2563EB;

}

/* ------------------------------------------------ */
/* Recommendation Cards */
/* ------------------------------------------------ */

.book-card{

    background:white;

    border-radius:15px;

    padding:20px;

    margin-bottom:20px;

    box-shadow:0px 4px 12px rgba(0,0,0,.12);

}

.book-title{

    color:#2563EB;

    font-size:24px;

    font-weight:bold;

}

.book-author{

    color:#444;

    font-size:16px;

}

.rating{

    color:#ff9800;

    font-size:18px;

    font-weight:bold;

}

/* ------------------------------------------------ */
/* Sidebar */
/* ------------------------------------------------ */

section[data-testid="stSidebar"]{

    background:#1E293B;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* ------------------------------------------------ */
/* Buttons */
/* ------------------------------------------------ */

.stButton>button{

    width:100%;

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    padding:12px;

    font-size:17px;

    font-weight:bold;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* ------------------------------------------------ */
/* Selectbox */
/* ------------------------------------------------ */

.stSelectbox div[data-baseweb="select"]{

    border-radius:10px;

}

/* ------------------------------------------------ */
/* Number Input */
/* ------------------------------------------------ */

.stNumberInput input{

    border-radius:10px;

}

/* ------------------------------------------------ */
/* Text Input */
/* ------------------------------------------------ */

.stTextInput input{

    border-radius:10px;

}

/* ------------------------------------------------ */
/* Download Button */
/* ------------------------------------------------ */

.stDownloadButton>button{

    width:100%;

    background:#16A34A;

    color:white;

    border-radius:10px;

    border:none;

}

/* ------------------------------------------------ */
/* Expanders */
/* ------------------------------------------------ */

.streamlit-expanderHeader{

    font-size:18px;

    font-weight:bold;

}

/* ------------------------------------------------ */
/* Charts */
/* ------------------------------------------------ */

.js-plotly-plot{

    border-radius:15px;

}

/* ------------------------------------------------ */
/* Divider */
/* ------------------------------------------------ */

hr{

    margin-top:25px;

    margin-bottom:25px;

}

/* ------------------------------------------------ */
/* Footer */
/* ------------------------------------------------ */

.footer{

    text-align:center;

    color:gray;

    padding:15px;

}

</style>
""",
        unsafe_allow_html=True
    )