import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import urllib.request

def download_and_set_font():
    font_dir = "./fonts"
    font_path = os.path.join(font_dir, "NanumGothic.ttf")

    if not os.path.exists(font_path):
        os.makedirs(font_dir, exist_ok=True)
        # ✅ 수정된 raw.githubusercontent 링크
        url = "https://raw.githubusercontent.com/naver/nanumfont/master/ttf/NanumGothic.ttf"
        urllib.request.urlretrieve(url, font_path)

    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
    plt.rcParams['axes.unicode_minus'] = False

# ▶️ 한글 폰트 다운로드 및 설정
download_and_set_font()

# 📊 Streamlit UI
st.title("CSV 파일 업로드 후 막대그래프 그리기")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
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
        st.error("'연도' 또는 '생활물가지수' 컬럼이 없습니다. 컬럼명을 확인해주세요.")
        st.stop()

    df['연도'] = df['연도'].astype(str)

    fig, ax = plt.subplots()
    ax.bar(df['연도'], df['생활물가지수'])
    ax.set_xlabel('연도')
    ax.set_ylabel('생활물가지수')
    ax.set_title('연도별 생활물가지수 막대그래프')
    plt.xticks(rotation=45)

    st.pyplot(fig)
