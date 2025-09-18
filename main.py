import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()

from openai import OpenAI

client = OpenAI()

st.title("자동 보고서 생성기 Created by Ctrl+Z")
subject = st.text_input("어느 지역에 대한 보고서를 작성할까요?")
st.write(f"지역명: {subject}")

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

