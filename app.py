import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🎰 로또 번호 생성기",
    page_icon="🎯",
    layout="centered"
)

# 제목 및 설명
st.title("🎰 로또 번호 생성기 (보너스 포함)")
st.markdown("버튼을 누르면 **1~45** 중에서 **메인 6개 + 보너스 1개** 번호를 뽑아요! 🍀")

# 세트 개수 선택
count = st.slider("몇 세트를 뽑을까요?", 1, 10, 1)

# 로또 번호 1세트 생성 함수
def draw_one_set()
