import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV 파일 업로드 후 막대그래프 그리기")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 연도가 문자열로 되어있다면 문자열로 변환
    df['연도'] = df['연도'].astype(str)

    st.write("데이터 미리보기")
    st.dataframe(df.head())

    fig, ax = plt.subplots()
    ax.bar(df['연도'], df['생활물가지수'])
    ax.set_xlabel('연도')
    ax.set_ylabel('생활물가지수')
    ax.set_title('연도별 생활물가지수 막대그래프')
    plt.xticks(rotation=45)

    st.pyplot(fig)
