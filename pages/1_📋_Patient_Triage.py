import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Patient Triage", page_icon="📋", layout="wide")
st.title("📋 Point-of-Care Patient Triage Calculator")

st.sidebar.header("Patient Clinical Parameters")
acuity = st.sidebar.selectbox("Dynamic Health Status", ["Critical", "Fluctuating", "Stable"])
tenure = st.sidebar.number_input("Care Duration (Months)", min_value=1, max_value=120, value=12)

# Calculation Logic
base_scores = {"Critical": 0.65, "Fluctuating": 0.42, "Stable": 0.18}
base = base_scores[acuity]
tenure_adj = 0.05 if tenure > 24 else 0.0
risk_score = min(0.98, base + tenure_adj)

threshold = st.slider("Active Decision Threshold (τ)", 0.10, 0.90, 0.35, 0.05)

st.metric(label="Computed Overdue Risk Score", value=f"{risk_score * 100:.1f}%")

if risk_score >= threshold:
    st.error("⚠️️ HIGH RISK: Flagged Overdue")
else:
    st.success("✅ LOW RISK: On-Time Scheduled")
