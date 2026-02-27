import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Flaky Test Detection",
    layout="wide"
)

st.title("🧪 Flaky Test Detection Using Machine Learning")
st.caption("Detect flaky tests using DBSCAN clustering on test execution features")

# ---------------- Upload Section ----------------
uploaded_file = st.file_uploader(
    "📂 Upload test_features.csv",
    type="csv"
)

if uploaded_file is None:
    st.info("Please upload a CSV file to start flaky test detection.")
    st.stop()

# ---------------- Read CSV ----------------
try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error("❌ Failed to read CSV file")
    st.code(str(e))
    st.stop()

# ---------------- Validate Columns ----------------
required_columns = {
    "test_name",
    "failure_rate",
    "status_switches",
    "avg_duration",
    "duration_variance"
}

if not required_columns.issubset(df.columns):
    st.error("❌ Invalid CSV format")
    st.write("Required columns:", required_columns)
    st.write("Found columns:", list(df.columns))
    st.stop()

# ---------------- Feature Processing ----------------
X = df.drop(columns=["test_name"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------- DBSCAN Parameters ----------------
st.sidebar.header("⚙️ DBSCAN Parameters")
eps = st.sidebar.slider("eps", 0.1, 3.0, 1.2, 0.1)
min_samples = st.sidebar.slider("min_samples", 1, 10, 2)

model = DBSCAN(eps=eps, min_samples=min_samples)
df["cluster"] = model.fit_predict(X_scaled)

df["flaky_label"] = df["cluster"].apply(
    lambda x: "Flaky" if x == -1 else "Stable"
)

# ---------------- Results ----------------
st.subheader("📊 Test Classification Results")
st.dataframe(df, use_container_width=True)

# ---------------- Flaky Tests Section ----------------
st.subheader("⚠️ Detected Flaky Tests")
flaky_df = df[df["flaky_label"] == "Flaky"]

if flaky_df.empty:
    st.success("🎉 No flaky tests detected")
else:
    st.warning(f"⚠️ {len(flaky_df)} flaky tests detected")
    st.dataframe(flaky_df, use_container_width=True)

# ---------------- Download Button ----------------
st.download_button(
    "⬇️ Download Results CSV",
    df.to_csv(index=False),
    file_name="flaky_results.csv",
    mime="text/csv"
)
