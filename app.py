import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="IPL Analytics",
    page_icon="🏏",
    layout="wide"
)

# ==========================
# LOAD MODELS
# ==========================

# Note: Ensure these files exist in your directory, otherwise Streamlit will throw a FileNotFoundError
win_model = joblib.load("ipl_win_predictor_v2.pkl")
score_model = joblib.load("score_predictor.pkl")

# ==========================
# SIDEBAR
# ==========================

page = st.sidebar.selectbox(
    "Choose Module",
    [
        "🏏 Win Predictor",
        "📈 Score Predictor"
    ]
)

teams = [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Delhi Capitals",
    "Punjab Kings",
    "Rajasthan Royals",
    "Lucknow Super Giants",
    "Gujarat Titans"
]

# ==========================
# TEAM LOGOS
# ==========================

team_logos = {
    "Mumbai Indians": "assets/mi.png",
    "Chennai Super Kings": "assets/csk.png",
    "Royal Challengers Bangalore": "assets/rcb.png",
    "Kolkata Knight Riders": "assets/kkr.png",
    "Sunrisers Hyderabad": "assets/srh.png",
    "Delhi Capitals": "assets/dc.png",
    "Punjab Kings": "assets/pbks.png",
    "Rajasthan Royals": "assets/rr.png",
    "Lucknow Super Giants": "assets/lsg.png",
    "Gujarat Titans": "assets/gt.png"
}

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

# ====================================================
# WIN PREDICTOR
# ====================================================

if page == "🏏 Win Predictor":

    st.title("🏏 IPL Win Predictor")

    col1, col2 = st.columns(2)

    with col1:

        batting_team = st.selectbox("Batting Team", teams)
        bowling_team = st.selectbox("Bowling Team", teams)
        venue = st.selectbox("Venue", venues)
        
        # CORRECTED INDENTATION: Moved these inside 'with col1:'
        logo1, vs, logo2 = st.columns([2,1,2])

        with logo1:
            st.image(team_logos[batting_team], width=140)

        with vs:
            st.markdown(
                "<h1 style='text-align:center;'>VS</h1>",
                unsafe_allow_html=True
            )

        with logo2:
            st.image(team_logos[bowling_team], width=140)

        target = st.number_input(
            "Target Score",
            min_value=1,
            value=180
        )

        current_score = st.number_input(
            "Current Score",
            min_value=0,
            value=120
        )

    with col2:

        runs_left = st.number_input(
            "Runs Left",
            min_value=0,
            value=60
        )

        balls_left = st.number_input(
            "Balls Left",
            min_value=1,
            value=36
        )

        wickets_in_hand = st.slider(
            "Wickets In Hand",
            0,
            10,
            6
        )

        runs_last_30_balls = st.number_input(
            "Runs Last 30 Balls",
            min_value=0,
            value=40
        )

        wickets_last_30_balls = st.slider(
            "Wickets Lost Last 30 Balls",
            0,
            10,
            1
        )

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

    if st.button("Predict Win Probability"):

        input_df = pd.DataFrame({
            "runs_left": [runs_left],
            "balls_left": [balls_left],
            "wickets_in_hand": [wickets_in_hand],
            "crr": [crr],
            "rrr": [rrr],
            "run_rate_diff": [run_rate_diff],
            "pressure": [pressure],
            "current_score": [current_score],
            "current_wickets": [current_wickets],
            "target": [target],
            "runs_last_30_balls": [runs_last_30_balls],
            "wickets_last_30_balls": [wickets_last_30_balls],
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "venue": [venue]
        })

        result = win_model.predict_proba(input_df)

        batting_win = round(result[0][1] * 100, 2)
        bowling_win = round(result[0][0] * 100, 2)

        winner = batting_team if batting_win > bowling_win else bowling_team

        st.success(f"🏆 Predicted Winner: {winner}")
        # Winner Logo
        st.image(
            team_logos[winner],
            width=250,
            caption=f"{winner} Predicted as Match Winner"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(batting_team, f"{batting_win}%")

        with col2:
            st.metric(bowling_team, f"{bowling_win}%")

        chart_df = pd.DataFrame({
            "Team": [batting_team, bowling_team],
            "Probability": [batting_win, bowling_win]
        })

        fig = px.pie(
            chart_df,
            names="Team",
            values="Probability",
            title="Winning Probability"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ====================================================
# SCORE PREDICTOR
# ====================================================

elif page == "📈 Score Predictor":

    st.title("📈 IPL First Innings Score Predictor")
    st.markdown(
        "Predict the final first-innings score using current match situation."
    )

    col1, col2 = st.columns(2)

    with col1:

        batting_team = st.selectbox(
            "Batting Team",
            teams,
            key="score_batting_team"
        )

        bowling_team = st.selectbox(
            "Bowling Team",
            [team for team in teams if team != batting_team],
            key="score_bowling_team"
        )

        venue = st.selectbox(
            "Venue",
            venues,
            key="score_venue"
        )

        current_score = st.number_input(
            "Current Score",
            min_value=0,
            max_value=300,
            value=85
        )

    with col2:

        overs_completed = st.slider(
            "Overs Completed",
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.1
        )

        wickets_lost = st.slider(
            "Wickets Lost",
            min_value=0,
            max_value=10,
            value=3
        )

        runs_in_last_5_overs = st.number_input(
            "Runs Scored in Last 5 Overs",
            min_value=0,
            max_value=100,
            value=40
        )

        wickets_in_last_5_overs = st.slider(
            "Wickets Lost in Last 5 Overs",
            min_value=0,
            max_value=5,
            value=1
        )

    st.divider()

    if st.button("Predict Final Score", use_container_width=True):

        score_input = pd.DataFrame({
            "current_score": [current_score],
            "overs_completed": [overs_completed],
            "wickets_lost": [wickets_lost],
            "runs_in_last_5_overs": [runs_in_last_5_overs],
            "wickets_in_last_5_overs": [wickets_in_last_5_overs],
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "venue": [venue]
        })

        prediction = score_model.predict(score_input)

        predicted_score = int(round(prediction[0]))

        lower_bound = predicted_score - 10
        upper_bound = predicted_score + 10

        st.success(
            f"🏏 Predicted Final Score: {predicted_score}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Current Score",
                current_score
            )

        with col2:
            st.metric(
                "Predicted Score",
                predicted_score
            )

        with col3:
            st.metric(
                "Expected Range",
                f"{lower_bound}-{upper_bound}"
            )

        progress = min(predicted_score / 250, 1.0)

        st.progress(progress)

        chart_df = pd.DataFrame({
            "Metric": [
                "Current Score",
                "Predicted Final Score"
            ],
            "Runs": [
                current_score,
                predicted_score
            ]
        })

        st.subheader("Score Comparison")

        st.bar_chart(
            chart_df.set_index("Metric")
        )

        st.info(
            f"📊 Estimated Final Score Range: "
            f"{lower_bound} - {upper_bound}"
        )