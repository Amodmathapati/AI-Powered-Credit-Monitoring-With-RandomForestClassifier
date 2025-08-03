from fpdf import FPDF
import pandas as pd

def generate_pdf_report(df: pd.DataFrame, output_path="credit_report.pdf"):
    """Generate a PDF report of employee credit risks."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Monthly Credit Monitoring Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for _, row in df.iterrows():
        line = f"Employee: {row['Employee_ID']} | Risk: {row['Risk_Label']}"
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(output_path)
