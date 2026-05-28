import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.simplefilter(
    "ignore",
    InconsistentVersionWarning
)

import os
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# =========================
# LOAD MODELS
# =========================

win_model = joblib.load(
    'models/ipl_win_predictor_v2.pkl'
)

score_model = joblib.load(
    'models/score_predictor.pkl'
)

# =========================
# TEAM LOGOS
# =========================

team_logos = {
    "Mumbai Indians": "mi.png",
    "Chennai Super Kings": "csk.png",
    "Royal Challengers Bangalore": "rcb.png",
    "Kolkata Knight Riders": "kkr.png",
    "Sunrisers Hyderabad": "srh.png",
    "Delhi Capitals": "dc.png",
    "Punjab Kings": "pk.png",
    "Rajasthan Royals": "rr.png",
    "Lucknow Super Giants": "lsg.png",
    "Gujarat Titans": "gt.png"
}

teams = list(team_logos.keys())

venues = [
    "Wankhede Stadium",
    "M Chinnaswamy Stadium",
    "Eden Gardens",
    "MA Chidambaram Stadium",
    "Narendra Modi Stadium",
    "Arun Jaitley Stadium",
    "Rajiv Gandhi International Stadium",
    "Punjab Cricket Association Stadium",
    "Sawai Mansingh Stadium",
    "Ekana Cricket Stadium"
]

# =========================
# HOME
# =========================

@app.route('/')
def home():
    return render_template('index.html')

# =========================
# WIN PREDICTOR
# =========================

@app.route('/win-predictor', methods=['GET', 'POST'])
def win_predictor():

    prediction = None

    if request.method == 'POST':

        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        venue = request.form['venue']

        target = int(request.form['target'])
        current_score = int(request.form['current_score'])
        runs_left = int(request.form['runs_left'])
        balls_left = int(request.form['balls_left'])
        wickets_in_hand = int(request.form['wickets_in_hand'])
        runs_last_30_balls = int(request.form['runs_last_30_balls'])
        wickets_last_30_balls = int(request.form['wickets_last_30_balls'])

        current_wickets = 10 - wickets_in_hand

        overs_completed = (120 - balls_left) / 6

        crr = current_score / overs_completed if overs_completed > 0 else 0

        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        run_rate_diff = crr - rrr

        pressure = (
            runs_left / wickets_in_hand
            if wickets_in_hand > 0
            else runs_left
        )

        input_df = pd.DataFrame({
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_in_hand': [wickets_in_hand],
            'crr': [crr],
            'rrr': [rrr],
            'run_rate_diff': [run_rate_diff],
            'pressure': [pressure],
            'current_score': [current_score],
            'current_wickets': [current_wickets],
            'target': [target],
            'runs_last_30_balls': [runs_last_30_balls],
            'wickets_last_30_balls': [wickets_last_30_balls],
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'venue': [venue]
        })

        result = win_model.predict_proba(input_df)

        batting_win = round(result[0][1] * 100, 2)
        bowling_win = round(result[0][0] * 100, 2)

        winner = batting_team if batting_win > bowling_win else bowling_team

        # Pressure Meter
        pressure_index = rrr - crr

        if pressure_index <= 1:
            pressure_status = 'Low Pressure'
        elif pressure_index <= 3:
            pressure_status = 'Medium Pressure'
        else:
            pressure_status = 'High Pressure'

        # Momentum
        momentum_score = (
            runs_last_30_balls - (wickets_last_30_balls * 10)
        )

        if momentum_score >= 40:
            momentum = 'Strong Momentum'
        elif momentum_score >= 20:
            momentum = 'Positive Momentum'
        else:
            momentum = 'Slow Momentum'

        # Chase Difficulty
        if target <= 150:
            difficulty = 'Easy Chase'
        elif target <= 180:
            difficulty = 'Balanced Match'
        elif target <= 210:
            difficulty = 'Tough Chase'
        else:
            difficulty = 'Very Difficult Chase'

        prediction = {
            'batting_win': batting_win,
            'bowling_win': bowling_win,
            'winner': winner,
            'pressure_status': pressure_status,
            'momentum': momentum,
            'difficulty': difficulty,
            'batting_team': batting_team,
            'bowling_team': bowling_team,
            'winner_logo': team_logos[winner]
        }

    return render_template(
        'win_predictor.html',
        teams=teams,
        venues=venues,
        team_logos=team_logos,
        prediction=prediction
    )

# =========================
# SCORE PREDICTOR
# =========================

@app.route('/score-predictor', methods=['GET', 'POST'])
def score_predictor():

    prediction = None

    if request.method == 'POST':

        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        venue = request.form['venue']

        current_score = int(request.form['current_score'])

        overs_completed = float(
            request.form['overs_completed']
        )

        wickets_lost = int(
            request.form['wickets_lost']
        )

        runs_in_last_5_overs = int(
            request.form['runs_in_last_5_overs']
        )

        wickets_in_last_5_overs = int(
            request.form['wickets_in_last_5_overs']
        )

        score_input = pd.DataFrame({

            'current_score': [current_score],

            'overs_completed': [overs_completed],

            'wickets_lost': [wickets_lost],

            'runs_in_last_5_overs': [
                runs_in_last_5_overs
            ],

            'wickets_in_last_5_overs': [
                wickets_in_last_5_overs
            ],

            'batting_team': [batting_team],

            'bowling_team': [bowling_team],

            'venue': [venue]

        })

        predicted_score = int(
            round(score_model.predict(score_input)[0])
        )

        prediction = {
            'predicted_score': predicted_score,
            'lower_bound': predicted_score - 10,
            'upper_bound': predicted_score + 10
        }

    return render_template(
        'score_predictor.html',
        prediction=prediction,
        teams=teams,
        venues=venues
    )

# =========================
# ABOUT PAGE
# =========================

@app.route('/about')
def about():
    return render_template('about.html')

# =========================
# MAIN
# =========================

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
