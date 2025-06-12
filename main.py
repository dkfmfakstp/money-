import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os


# 한글 폰트 설정 (예: NanumGothic)
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 리눅스용 NanumGothic 위치
if not os.path.exists(font_path):
    # Streamlit 환경이나 로컬 환경에 따라 다른 경로 또는 대체 폰트가 필요할 수 있음
    font_path = fm.findfont("Malgun Gothic")  # Windows용
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
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
