import streamlit as st

st.set_page_config(
    page_title="Equity Afya - Patient Triage System",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Equity Afya: Clinical Triage & Early Warning System")
st.markdown("---")
st.markdown("""
Welcome to the **Equity Afya Chronic Care Adherence Triage Tool**.

This application leverages machine learning (XGBoost) to predict patient appointment non-adherence and overdue risk for Non-Communicable Diseases (NCDs) such as Hypertension, Diabetes, and Asthma.

### **Available Navigation:**
* **📋 Patient Triage:** Point-of-care interactive risk calculator for individual patients.
* **📊 Population Dashboard:** High-level analytics and multimorbidity trends across the cohort.
* **🔍 Model Explainability:** Feature importance gain audit and predictive drivers.
""")
