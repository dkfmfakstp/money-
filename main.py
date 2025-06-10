import streamlit as st
import matplotlib.pyplot as plt

st.title("간단한 막대그래프 예제")

# 샘플 데이터
categories = ['사과', '바나나', '체리', '오렌지']
values = [10, 15, 7, 12]

fig, ax = plt.subplots()
ax.bar(categories, values)
ax.set_xlabel("과일")
ax.set_ylabel("수량")
ax.set_title("과일별 수량 막대그래프")

st.pyplot(fig)
