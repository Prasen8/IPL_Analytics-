# 🏏 IPL Analytics

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Live Demo:** [Click here to view the live deployed app](https://ipl-analytics-jx75.onrender.com) 

A comprehensive, end-to-end Machine Learning web application designed to predict outcomes and scores for Indian Premier League (IPL) cricket matches in real-time. Built with Python, Flask, and Scikit-Learn, this project uses historical IPL data to generate actionable insights, win probabilities, and advanced match analytics.

---

# 📊 Data Pipeline

| File              | Purpose                                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IPL_Data.py` | Downloads ball-by-ball data from Cricsheet, cleans team names, engineers features (cumulative score, run rate, phase, etc.), and saves CSVs ready for analysis |

---

# 📓 Jupyter Notebooks

| Notebook                      | What it does                                                                                                                                                                      | Audience                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `ipl_wow_facts.ipynb`         | 🎤 10 hook-style “did you know?” IPL stats with interactive Plotly charts. Perfect for opening a session.                                                                         | Beginners / General Fans |
| `ipl_eda_insights.ipynb`      | 📊 Deep exploratory analysis — powerplay impact, venue patterns, chase win % by required run rate, head-to-head matrix                                                            | Mixed Audience           |
| `ipl_win_predictor.ipynb`     | 🤖 Trains ML models (Logistic Regression, Random Forest, Gradient Boosting) to predict live chase win probability ball-by-ball. Includes calibration check and live match replay. | Technical                |
| `ipl_awards_predictor.ipynb`  | 🏆 Predicts Orange Cap, Purple Cap, Most 4s, Most 6s — both for current season projection and next season using ML models trained on historical player data.                      | Technical                |


---

## 📊 Data Pipeline

| File              | Purpose                                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_ipl_data.py` | Downloads ball-by-ball data from Cricsheet, cleans team names, engineers features (cumulative score, run rate, phase, etc.), and saves CSVs ready for analysis |

---

## 📓 Jupyter Notebooks

| Notebook                      | What it does                                                                                                                                                                      | Audience                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `ipl_wow_facts.ipynb`         | 🎤 10 hook-style “did you know?” IPL stats with interactive Plotly charts. Perfect for opening a session.                                                                         | Beginners / General Fans |
| `ipl_eda_insights.ipynb`      | 📊 Deep exploratory analysis — powerplay impact, venue patterns, chase win % by required run rate, head-to-head matrix                                                            | Mixed Audience           |
| `ipl_win_predictor.ipynb`     | 🤖 Trains ML models (Logistic Regression, Random Forest, Gradient Boosting) to predict live chase win probability ball-by-ball. Includes calibration check and live match replay. | Technical                |
| `ipl_awards_predictor.ipynb`  | 🏆 Predicts Orange Cap, Purple Cap, Most 4s, Most 6s — both for current season projection and next season using ML models trained on historical player data.                      | Technical                |
| `ipl_playoff_predictor.ipynb` | 🎯 Predicts playoff qualification using Monte Carlo simulation (10K runs) and NRR-based scenario analysis.                                                                        | Technical                |

---

# 🚀 Key Highlights

✅ Machine Learning Based Predictions
✅ IPL Ball-by-Ball Analytics
✅ Interactive Visualizations with Plotly
✅ Flask-Based Full Stack Web Application
✅ Real-Time Match Win Probability
✅ Score Prediction & Match Insights
✅ Professional Deployment Ready





## 🔥 Key Features

* **🏆 Match Win Predictor:** Calculates the real-time probability of the batting or bowling team winning based on current match conditions (target, overs left, wickets, etc.).
* **📈 First Innings Score Predictor:** Estimates the final first-innings score using current run rates, wickets lost, and momentum in the last 5 overs.
* **⚡ Advanced Match Analytics:** 
    * **Pressure Meter:** Evaluates the required run rate vs. current run rate to determine batting pressure.
    * **Momentum Analysis:** Tracks performance over the last 30 balls to gauge team momentum.
    * **Chase Difficulty:** Categorizes the required target into dynamic difficulty levels.
* **🎨 Dynamic UI/UX:** Features an interactive, responsive dashboard with automatic team logo updates upon selection, built with Bootstrap 5 and JavaScript.

---

## 🛠️ Tech Stack

### Machine Learning & Data Processing
* **Python:** Core programming language.
* **Scikit-Learn:** Used for training the `RandomForestClassifier` (Win Prediction) and `RandomForestRegressor` (Score Prediction).
* **Pandas & NumPy:** For data cleaning, feature engineering, and pipeline processing.
* **Joblib:** For saving and loading the trained machine learning models (`.pkl` files).

### Backend & Web Framework
* **Flask:** Lightweight WSGI web application framework.
* **Gunicorn:** Python WSGI HTTP Server for UNIX (used for deployment).

### Frontend
* **HTML5 / CSS3 / JavaScript:** Core frontend technologies.
* **Bootstrap 5:** For responsive grids, cards, and styling.
* **Jinja2:** Flask's templating engine for dynamic HTML rendering.

---

## 📁 Project Structure

```text
IPL-Analytics-Flask/
│
├── app.py                      # Main Flask application file
├── requirements.txt            # Python dependencies
├── Procfile                    # Render/Heroku deployment config
├── .gitignore                  # Git ignore rules
│
├── models/                     # Saved Machine Learning models
│   ├── ipl_win_predictor_v2.pkl
│   └── score_predictor.pkl
│
├── static/                     # Static assets (CSS, JS, Images)
│   ├── css/
│   │   └── style.css
│   └── images/                 # Team logos
│       ├── csk.png
│       ├── mi.png
│       └── ...
│
└── templates/                  # HTML Templates (Jinja2)
    ├── layout.html             # Base layout/navbar
    ├── index.html              # Homepage
    ├── win_predictor.html      # Win prediction interface
    ├── score_predictor.html    # Score prediction interface
    └── about.html              # Developer portfolio/about page

``` 

### 🌐 Connect With Me
Developed with ❤️ by Prasen Nimje

LinkedIn: https://linkedin.com/in/prasen-nimje

GitHub: github.com/Prasen8

⭐️ If you found this project helpful or interesting, please consider giving it a star!
