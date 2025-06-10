import streamlit as st
import pandas as pd
import altair as alt

st.title("생활물가지수 연도별 막대 그래프")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # utf-8이 안 될 경우 cp949로 재시도
        try:
            df = pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            uploaded_file.seek(0)  # 파일 포인터 처음으로 돌리기
            df = pd.read_csv(uploaded_file, encoding='cp949')
        
        st.write("업로드된 데이터:")
        st.dataframe(df)
        
        # 컬럼 확인
        if '연도' in df.columns and '생활물가지수' in df.columns:
            # 데이터 타입 맞추기
            df['연도'] = df['연도'].astype(str)
            df['생활물가지수'] = pd.to_numeric(df['생활물가지수'], errors='coerce')
            df = df.dropna(subset=['생활물가지수'])
            
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('연도', sort=None, title='연도'),
                y=alt.Y('생활물가지수', title='생활물가지수'),
                tooltip=['연도', '생활물가지수']
            ).properties(width=700, height=400, title="연도별 생활물가지수")
            st.altair_chart(chart)
        else:
            st.error("CSV 파일에 '연도' 또는 '생활물가지수' 컬럼이 없습니다.")
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("CSV 파일을 업로드해주세요.")
