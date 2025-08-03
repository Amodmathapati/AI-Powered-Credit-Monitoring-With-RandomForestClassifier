# AI-Powered Credit Monitoring for Government Employees

## 📌 Project Overview
This project is a **web-based AI application** that continuously monitors the credit behavior of government employees based on uploaded financial data.  
It uses **Machine Learning** to detect spending patterns, repayment behavior, and flag high-risk cases.  
The system generates **interactive dashboards** and a **monthly PDF report** for better decision-making.

---

## ✨ Features
- **CSV File Upload** → Upload employee financial data directly in the browser.
- **AI-Powered Risk Prediction** → Classifies employees as:
  - 🟢 **Safe**
  - 🟡 **Watchlist**
  - 🔴 **High Risk**
- **Interactive Visualizations** → 
  - Bar chart for spending vs income
  - Pie chart for risk distribution
  - Line chart for monthly spending trends
- **PDF Report Generation** → Download monthly summary reports.
- **Consistent Color Coding** → Easy risk category recognition across tables & charts.

---

## 🛠 Tech Stack Used

### **Frontend**
- [Streamlit](https://streamlit.io/) → Python-based web app framework
- [Plotly](https://plotly.com/python/) → Interactive data visualization
- [Altair](https://altair-viz.github.io/) → Lightweight visualization library (optional)

### **Backend / Machine Learning**
- [Python 3.x](https://www.python.org/) → Core programming language
- [Pandas](https://pandas.pydata.org/) → Data processing
- [Scikit-learn](https://scikit-learn.org/) → Machine Learning (Random Forest Classifier) & feature engineering
- [Joblib](https://joblib.readthedocs.io/) → Model persistence (saving/loading ML models)

### **Report Generation**
- [FPDF](https://pyfpdf.readthedocs.io/) → PDF creation library

---

## 📂 Folder Structure
project/
│
├── app.py                      # Main Streamlit dashboard
├── model/
│   ├── train_model.py           # Model training script
│   ├── risk_model.pkl           # Pre-trained ML model
│
├── utils/
│   ├── data_processing.py       # Data cleaning & feature engineering
│   ├── ai_analysis.py           # Model prediction functions
│   ├── report_generator.py      # PDF report creation
│
├── sample_data/
│   ├── employees.csv            # Example input dataset
│
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation


---

## ⚙️ Setup Instructions

### **1. Clone the repository**
git clone https://github.com/Amodmathapati/ai-credit-monitoring.git
cd ai-credit-monitoring

### **2. Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### **3. Install dependencies**
pip install -r requirements.txt

### **4. Train the model (only if retraining)**
cd model
python train_model.py
This will generate a risk_model.pkl file.

### **5. Train the model (only if retraining)**
streamlit run app.py
The app will open at:
http://localhost:8501

