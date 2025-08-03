import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/risk_model.pkl")

def predict_risk(df: pd.DataFrame) -> pd.DataFrame:
    """Predict risk levels for employees."""
    features = df[["spending_ratio", "delay_rate", "debt_to_income_ratio"]]
    df["Predicted_Risk"] = model.predict(features)
    df["Risk_Label"] = df["Predicted_Risk"].map({0: "Safe", 1: "Watchlist", 2: "High Risk"})
    return df
