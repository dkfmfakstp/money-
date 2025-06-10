import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 예제")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # UTF-8로 먼저 시도
        df = pd.read_csv(uploaded_file)
    except UnicodeDecodeError:
        # 실패 시 CP949로 재시도
        uploaded_file.seek(0)  # 파일 포인터를 처음으로 되돌리기
        df = pd.read_csv(uploaded_file, encoding='cp949')
    
    st.write("업로드된 데이터:")
    st.dataframe(df)
