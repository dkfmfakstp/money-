import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 예제")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='cp949')
    
    st.write("업로드된 데이터:")
    st.dataframe(df)
