import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Flaky Test Detection",
    layout="wide"
)

st.title("🧪 Flaky Test Detection Using ML")

# Absolute path (works on Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "flaky_results.csv")

st.caption(f"📂 Loading data from: {DATA_FILE}")

# Check file exists
if not os.path.exists(DATA_FILE):
    st.error("❌ data/flaky_results.csv not found")
    st.stop()

# Read CSV safely
try:
    df = pd.read_csv(DATA_FILE)
except Exception as e:
    st.error("❌ Failed to read CSV file")
    st.code(str(e))
    st.stop()

# Validate columns
required_cols = {
    "test_name",
    "failure_rate",
    "status_switches",
    "avg_duration",
    "duration_variance",
    "cluster",
    "flaky_label"
}

if not required_cols.issubset(df.columns):
    st.error("❌ CSV columns are incorrect")
    st.write("Expected columns:", required_cols)
    st.write("Found columns:", list(df.columns))
    st.stop()

# Display full data
st.subheader("📊 All Test Results")
st.dataframe(df, use_container_width=True)

# Filter flaky tests
st.subheader("⚠️ Flaky Tests")
flaky_df = df[df["flaky_label"] == "Flaky"]

if flaky_df.empty:
    st.success("🎉 No flaky tests detected")
else:
    st.warning(f"⚠️ {len(flaky_df)} flaky tests detected")
    st.dataframe(flaky_df, use_container_width=True)
