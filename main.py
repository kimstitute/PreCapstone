import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()

from openai import OpenAI

# OpenAI API 키 설정
try:
    api_key = st.secrets["OPENAI_API_KEY"]
    if not api_key:
        st.error("OpenAI API 키가 설정되지 않았습니다. Streamlit Cloud의 Secrets에서 'OPENAI_API_KEY'를 설정해주세요.")
        st.stop()
except Exception as e:
    st.error("OpenAI API 키를 가져오는데 실패했습니다. Streamlit Cloud의 Secrets에서 'OPENAI_API_KEY'를 설정해주세요.")
    st.stop()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

st.title("자동 보고서 생성기 Created by Ctrl+Z")
subject = st.text_input("어느 지역에 대한 보고서를 작성할까요?")
st.write(f"지역명: {subject}")

if st.button("보고서 작성"):
    with st.spinner("보고서 작성 중..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 유능한 보고서 작성 AI야."},
                {"role": "user", "content": f"{subject} 지역의 문화 행사 및 문화 시설 현황에 대한 보고서를 작성해줘"}
            ]
        )
        st.write(response.choices[0].message.content)

