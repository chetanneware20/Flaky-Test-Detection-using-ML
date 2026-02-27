import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Flaky Test Detection", layout="wide")

st.title("🧪 Flaky Test Detection Using Machine Learning")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "flaky_results.csv")

st.write("📂 Looking for file at:")
st.code(DATA_FILE)

if not os.path.exists(DATA_FILE):
    st.error("❌ flaky_results.csv not found")
    st.info("Check that the file exists inside the data/ folder")
    st.stop()

df = pd.read_csv(DATA_FILE)

st.subheader("📊 All Test Results")
st.dataframe(df, use_container_width=True)

st.subheader("⚠️ Flaky Tests")
flaky_df = df[df["flaky_label"] == "Flaky"]

if flaky_df.empty:
    st.success("🎉 No flaky tests detected")
else:
    st.warning(f"{len(flaky_df)} flaky tests detected")
    st.dataframe(flaky_df, use_container_width=True)
