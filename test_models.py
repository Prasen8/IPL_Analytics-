import pickle

with open("score_predictor.pkl", "rb") as f:
    model = pickle.load(f)

print(type(model))

if hasattr(model, "feature_names_in_"):
    print(model.feature_names_in_)