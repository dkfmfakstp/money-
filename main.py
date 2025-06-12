import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 📌 나눔고딕 폰트 경로 설정
font_path = './NanumGothic.ttf'  # 같은 폴더에 있는 경우
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    st.warning("❌ 'NanumGothic.ttf' 폰트 파일이 폴더에 없습니다. 한글이 깨질 수 있습니다.")

# 기본 Streamlit 앱 UI
st.title("📈 생활물가지수 분석")

uploaded_file = st.file_uploader("📂 생활물가지수 CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    # CSV 읽기
    df = pd.read_csv(uploaded_file)

    st.subheader("✅ 데이터 미리보기")
    st.dataframe(df.head())

    # 열 이름 자동 추정 (첫 번째: 연도, 두 번째: 지수)
    if df.shape
