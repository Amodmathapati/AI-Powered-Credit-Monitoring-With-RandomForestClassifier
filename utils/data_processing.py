import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and create derived features."""
    df["spending_ratio"] = df["Total_Spending"] / df["Income"]
    df["delay_rate"] = df["Payment_Delay_Days"] / 30
    df["debt_to_income_ratio"] = df["Loan_Repayments"] / df["Income"]
    return df
