import streamlit as st
from openai import OpenAI

st.title("자동 보고서 생성기 \nCreated by Ctrl+Z")
subject = st.text_input("어느 지역에 대한 보고서를 작성할까요?")
st.write(f"지역명: {subject}")

from dotenv import load_dotenv

# 환경 변수 불러오기
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY) 

if st.button("보고서 작성"):
    with st.spinner("보고서 작성 중..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "너는 유능한 보고서 작성 AI야."},
                {"role": "user", "content": f"{subject} 지역의 문화 행사 및 문화 시설 현황에 대한 보고서를 작성해줘"}
            ]
        )
        st.write(response.choices[0].message.content)