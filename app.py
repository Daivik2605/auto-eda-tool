import streamlit as st
import pandas as pd
import sweetviz as sv


st.title("Auto-EDA Tool")
uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)  # Add Excel support with `pd.read_excel`
    st.write("### Raw Data Preview", df.head())

    # Auto-EDA
    if st.button("Generate EDA Report"):
        report = sv.analyze(df)
        report.show_html()  # Opens in browser or use `report.show_notebook()`