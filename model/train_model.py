import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load sample data
df = pd.read_csv("../sample_data/employees.csv")

# Feature engineering
df["spending_ratio"] = df["Total_Spending"] / df["Income"]
df["delay_rate"] = df["Payment_Delay_Days"] / 30
df["debt_to_income_ratio"] = df["Loan_Repayments"] / df["Income"]

# Simulated labels for training (0=Safe, 1=Watchlist, 2=High Risk)
# df["Risk_Level"] = [0, 0, 1, 2, 1]

def assign_risk(row):
    if row["spending_ratio"] > 0.9:
        return 2
    elif row["spending_ratio"] > 0.6 or row["delay_rate"] > 0.3:
        return 1
    else:
        return 0


df["Risk_Level"] = df.apply(assign_risk, axis=1)


# Train model
X = df[["spending_ratio", "delay_rate", "debt_to_income_ratio"]]
y = df["Risk_Level"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "risk_model.pkl")

print("✅ Model trained and saved as risk_model.pkl")

