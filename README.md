# 🏏 IPL Analytics

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![License](https://img.shields.io/badge/License-MIT-green)

**Live Demo:** [Click here to view the live deployed app](https://your-render-url-goes-here.onrender.com) *(Replace with your Render URL)*

A comprehensive, end-to-end Machine Learning web application designed to predict outcomes and scores for Indian Premier League (IPL) cricket matches in real-time. Built with Python, Flask, and Scikit-Learn, this project uses historical IPL data to generate actionable insights, win probabilities, and advanced match analytics.

---

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


##🌐 Connect With Me
Developed with ❤️ by Prasen Nimje

LinkedIn: linkedin.com/in/prasen-nimje

GitHub: github.com/Prasen8

⭐️ If you found this project helpful or interesting, please consider giving it a star!
