import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 예제")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

# 파일이 업로드되었는지 확인
if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)
    
    # 데이터프레임 출력
    st.write("업로드된 데이터:")
    st.dataframe(df)
