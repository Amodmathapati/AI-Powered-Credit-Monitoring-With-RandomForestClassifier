import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processing import preprocess_data
from utils.ai_analysis import predict_risk
from utils.report_generator import generate_pdf_report

st.set_page_config(page_title="AI Credit Monitoring", layout="wide")

st.title("AI-Powered Credit Monitoring for Government Employees")
st.write("Upload employee credit data to monitor spending, repayments, and detect risky patterns.")

uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Process data & predict
    df = preprocess_data(df)
    df = predict_risk(df)

    st.subheader("📊 AI Predictions")
    st.dataframe(df)

    # --- Visualization Section ---
    st.markdown("### 📊 Data Visualizations")

    # 1. Spending vs Income (Bar Chart)
    bar_fig = px.bar(
        df, x="Employee_ID", y="Total_Spending", color="Risk_Label",
        color_discrete_map={"High Risk": "red", "Safe": "green", "Watchlist": "yellow"},
        title="Spending vs Income by Employee"
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    # 2. Risk Distribution (Pie Chart)
    pie_fig = px.pie(
        df, names="Risk_Label",
        color="Risk_Label",
        color_discrete_map={"High Risk": "red", "Safe": "green", "Watchlist": "yellow"},
        title="Risk Category Distribution"
    )
    st.plotly_chart(pie_fig, use_container_width=True)

    # 3. Monthly Spending Trend (Line Chart)
    if "Month" in df.columns:
        trend_fig = px.line(
            df.sort_values("Month"),
            x="Month", y="Total_Spending",
            color="Risk_Label",
            color_discrete_map={"High Risk": "red", "Safe": "green", "Watchlist": "yellow"},
            title="Monthly Spending Trend"
        )
        st.plotly_chart(trend_fig, use_container_width=True)

    # Generate PDF Report
    generate_pdf_report(df)
    with open("credit_report.pdf", "rb") as pdf_file:
        st.download_button("📥 Download PDF Report", pdf_file, file_name="credit_report.pdf")
