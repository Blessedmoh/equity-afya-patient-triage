import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Explainability", page_icon="🔍", layout="wide")
st.title("🔍 Model Explainability & Feature Gain")

st.subheader("XGBoost Feature Importance Ranking")
data = {
    "Feature": ["Care Duration (Months)", "Visit Density", "Dynamic Status", "Age", "Comorbidities / Gender"],
    "Importance Gain (%)": [38.0, 24.0, 18.0, 10.0, 10.0]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
