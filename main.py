import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 및 읽기 예제")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        # 기본적으로 utf-8 인코딩으로 시도
        df = pd.read_csv(uploaded_file, encoding='utf-8')
        st.success("UTF-8 인코딩으로 성공적으로 읽었습니다!")
    except UnicodeDecodeError:
        # utf-8 실패 시 cp949 인코딩으로 시도
        uploaded_file.seek(0)  # 파일 포인터 초기화
        try:
            df = pd.read_csv(uploaded_file, encoding='cp949')
            st.success("CP949 인코딩으로 성공적으로 읽었습니다!")
        except Exception as e:
            st.error(f"파일을 읽는 데 실패했습니다: {e}")
            df = None
    except Exception as e:
        st.error(f"파일을 읽는 데 실패했습니다: {e}")
        df = None

    if df is not None:
        st.dataframe(df)  # 데이터프레임 출력
