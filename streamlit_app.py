import streamlit as st
import pyshorteners

# 제목 설정
st.title("URL Shortener")

# 사용자가 입력할 URL
url = st.text_input("Enter the URL to shorten:")

# URL이 입력되었을 때
if url:
    # URL을 단축하는 함수
    def shorten_url(url):
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
    
    # 단축된 URL 생성
    short_url = shorten_url(url)
    
    # 단축된 URL 표시
    st.write("Shortened URL:", short_url)
else:
    st.write("Please enter a valid URL.")
