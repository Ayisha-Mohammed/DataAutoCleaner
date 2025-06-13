import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="AutoCleaner", page_icon="🧹")
st.title("🧹 AutoCleaner: Universal Data Cleaning Tool")

uploaded_file = st.file_uploader("📁 Upload a CSV file", type="csv")

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)

    # Sidebar options
    st.sidebar.header("Options 🛠️")

    # Preview data
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Shape
    st.info(f"📐 Dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**")

    # Data info
    st.subheader("🧠 Data Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

    # Descriptive stats
    st.subheader("📊 Descriptive Statistics")
    st.write(df.describe())

    # 🆕 Missing Values & Column Types
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Values': missing,
        'Percent': missing_percent
    }).reset_index().rename(columns={'index': 'Column'})

    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()

    # Sidebar toggles
    if st.sidebar.checkbox("Show Missing Values"):
        st.subheader("🕳️ Missing Values")
        st.dataframe(missing_df)

    if st.sidebar.checkbox("Show Column Types"):
        st.subheader("🔎 Column Types")
        st.markdown(f"**Numeric Columns ({len(num_cols)}):** {', '.join(num_cols)}")
        st.markdown(f"**Categorical Columns ({len(cat_cols)}):** {', '.join(cat_cols)}")

else:
    st.warning("👈 Upload a CSV file to get started.")
