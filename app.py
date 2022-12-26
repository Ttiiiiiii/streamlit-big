import streamlit as st
view = [100,150,30]
st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview
st.title('빅프로젝트_2022_AIVLE_DX_12조')
st.header('🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎')
st.subheader('예상 잔존량 구하기')
# 경북 사과 생산량 데이터 가져오기
df_output = pd.read_csv('Gyeongbuk total output.csv', encoding='cp949')
