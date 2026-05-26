import joblib

model = joblib.load("score_predictor.pkl")

print(type(model))

try:
    print(model.feature_names_in_)
except:
    print("No feature_names_in_ available")

print(model)