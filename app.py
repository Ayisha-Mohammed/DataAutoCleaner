import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="AutoCleaner", page_icon="🧹")
st.title("🧹 AutoCleaner: Universal Data Cleaning Tool")

uploaded_file = st.file_uploader("📁 Upload a CSV file", type="csv")

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview (first 5 rows)")
    st.dataframe(df.head())

    st.info(f"📐 Dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**")

    st.subheader("🧠 Data Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.subheader("📊 Descriptive Statistics")
    st.write(df.describe())
else:
    st.warning("👈 Upload a CSV file to get started.")
