import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 나눔고딕 폰트 경로 설정 (로컬 또는 폰트 업로드 후 사용)
# 폰트 파일을 프로젝트에 넣고 사용하거나 시스템에 설치된 경로 지정
font_path = './NanumGothic.ttf'  # 이 경로에 폰트가 있어야 함
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# Streamlit 앱 UI
st.title("생활물가지수 분석")

uploaded_file = st.file_uploader("생활물가지수 CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)

    st.write("데이터 미리보기:")
    st.dataframe(df.head())

    # 연도 열 추정: 첫 번째 열이 연도라고 가정
    year_column = df.columns[0]
    value_column = df.columns[1]  # 두 번째 열이 지수 값이라고 가정

    # '/1'로 끝나는 연도만 필터링
    filtered_df = df[df[year_column].astype(str).str.endswith("/1")]

    # 시각화
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_df[year_column], filtered_df[value_column], marker='o')
    plt.title("생활물가지수 연도별 변화 (연도 끝이 '/1'인 데이터만)")
    plt.xlabel("연도")
    plt.ylabel("생활물가지수")
    plt.xticks(rotation=45)
    plt.grid(True)

    st.pyplot(plt)
