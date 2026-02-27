import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Flaky Test Detection", layout="wide")

st.title("🧪 Flaky Test Detection Using ML")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "flaky_results.csv")

if not os.path.exists(DATA_PATH):
    st.error("❌ Required file not found: data/flaky_results.csv")
    st.info("Run feature_engineering.py and clustering_model.py first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

st.subheader("📊 All Test Results")
st.dataframe(df, use_container_width=True)

st.subheader("⚠️ Flaky Tests")
flaky_df = df[df["flaky_label"] == "Flaky"]

if flaky_df.empty:
    st.success("🎉 No flaky tests detected")
else:
    st.warning(f"{len(flaky_df)} flaky tests detected")
    st.dataframe(flaky_df, use_container_width=True)
