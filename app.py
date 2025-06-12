import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 📌 한글 폰트 설정 (NanumGothic 또는 Malgun Gothic 등)
def set_korean_font():
    font_paths = [
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",  # Linux (Streamlit Cloud 등)
        "C:/Windows/Fonts/malgun.ttf",                     # Windows
        "/System/Library/Fonts/AppleGothic.ttf"            # macOS
    ]
    for path in font_paths:
        if os.path.exists(path):
            font_name = fm.FontProperties(fname=path).get_name()
            plt.rc('font', family=font_name)
            plt.rcParams['axes.unicode_minus'] = False
            return
    st.warning("한글 폰트를 찾을 수 없어 한글이 깨질 수 있습니다.")

# 한글 폰트 설정 실행
set_korean_font()

# 📌 Streamlit UI 시작
st.title("CSV 파일 업로드 후 막대그래프 그리기")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='cp949')
    except UnicodeDecodeError:
        st.error("파일 인코딩 문제 발생: cp949 인코딩으로 읽을 수 없습니다.")
        st.stop()

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    st.write("컬럼명 리스트:", df.columns.tolist())
    st.write("데이터 미리보기")
    st.dataframe(df.head())

    # 필수 컬럼 확인
    if '연도' not in df.columns or '생활물가지수' not in df.columns:
        st.error("'연도' 또는 '생활물가지수' 컬럼이 없습니다. 컬럼명을 확인해주세요.")
        st.stop()

    df['연도'] = df['연도'].astype(str)

    # 📊 막대그래프 그리기
    fig, ax = plt.subplots()
    ax.bar(df['연도'], df['생활물가지수'])
    ax.set_xlabel('연도')
    ax.set_ylabel('생활물가지수')
    ax.set_title('연도별 생활물가지수 막대그래프')
    plt.xticks(rotation=45)

    # 그래프 출력
    st.pyplot(fig)
