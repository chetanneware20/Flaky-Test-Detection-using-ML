import streamlit as st
import pandas as pd

st.set_page_config(page_title="Flaky Test Detection Dashboard")

st.title("🧪 Flaky Test Detection using ML")

df = pd.read_csv("data/flaky_results.csv")

st.subheader("Flaky Test Summary")
st.dataframe(df)

st.subheader("Flaky Tests")
st.write(df[df['flaky_label'] == 'Flaky'])
