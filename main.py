import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
else:
    st.write("CSV 파일을 업로드해주세요.")
