import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import tempfile

st.title("CSV + 폰트 파일 업로드 후 한글 막대그래프 그리기")

# ▶️ 한글 폰트 파일 업로드 받기
font_file = st.file_uploader("한글 폰트 파일(.ttf)을 업로드하세요", type=["ttf"])
font_path = None

if font_file is not None:
    # 임시 파일에 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ttf") as tmp_file:
        tmp_file.write(font_file.read())
        font_path = tmp_file.name

    # ✅ matplotlib에 폰트 등록
    font_prop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())
    plt.rcParams['axes.unicode_minus'] = False
    st.success(f"'{font_prop.get_name()}' 폰트가 설정되었습니다.")

# ▶️ CSV 업로드 및 그래프
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None and font_path:
    try:
        df = pd.read_csv(uploaded_file, encoding='cp949')
    except UnicodeDecodeError:
        st.error("파일 인코딩 문제 발생: cp949 인코딩으로 읽을 수 없습니다.")
        st.stop()

    df.columns = df.columns.str.strip()
    st.write("컬럼명 리스트:", df.columns.tolist())
    st.write("데이터 미리보기")
    st.dataframe(df.head())

    if '연도' not in df.columns or '생활물가지수' not in df.columns:
        st.error("'연도' 또는 '생활물가지수' 컬럼이 없습니다.")
        st.stop()

    df['연도'] = df['연도'].astype(str)

    fig, ax = plt.subplots()
    ax.bar(df['연도'], df['생활물가지수'])
    ax.set_xlabel('연도')
    ax.set_ylabel('생활물가지수')
    ax.set_title('연도별 생활물가지수')
    plt.xticks(rotation=45)

    st.pyplot(fig)
