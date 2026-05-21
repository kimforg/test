import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 레이아웃 설정 (넓게 보기)
st.set_page_config(layout="wide", page_title="AI 추천 전략 대시보드")

# 2. index.html 파일 읽어오기
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 3. Streamlit 화면에 HTML 코드 뿌려주기
    # 대시보드 크기에 맞게 height(높이)를 적절히 조절해주세요.
    components.html(html_code, height=650, scrolling=True)

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. 경로를 확인해주세요!")
