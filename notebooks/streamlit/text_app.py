# 텍스트 표시 예제

#streamlit run text_app.py

import streamlit as st

st.title("Sam LEE's First Streamlit Service:smile:") #H1
st.header("st.header(문자열): 헤더") # H2
st.subheader("st.subheader(문자열): 서브헤더") # H3
st.text("st.text(문자열): 일반 텍스트입니다.") # Text 

st.text("st.code(code): 파이썬 코드 표시")



code = '''

def hello():
    print("Hello, Streamlit!")
	
'''
code = '''

print("hello world")
'''


st.code(code)

st.markdown('스트림릿에서 **마크다운**을 사용할 수 있습니다.:sunglasses:')

