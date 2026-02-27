import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Flaky Test Detection", layout="wide")

st.title("🧪 Flaky Test Detection Using ML")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "flaky_results.csv")

st.write("📂 Looking for file at:", DATA_PATH)

if not os.path.exists(DATA_PATH):
    st.error("❌ data/flaky_results.csv not found")
    st.stop()

try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error("❌ CSV read error")
    st.code(str(e))
    st.stop()

st.subheader("📊 All Test Results")
st.dataframe(df, use_container_width=True)

if "flaky_label" not in df.columns:
    st.error("❌ Column 'flaky_label' missing in CSV")
    st.stop()

st.subheader("⚠️ Flaky Tests")
flaky_df = df[df["flaky_label"] == "Flaky"]

if flaky_df.empty:
    st.success("🎉 No flaky tests detected")
else:
    st.warning(f"{len(flaky_df)} flaky tests detected")
    st.dataframe(flaky_df, use_container_width=True)
