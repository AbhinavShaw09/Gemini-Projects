import streamlit as st 
import os 
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def get_gemini_reponse(question):
    response = chat.send_message(question, stream=0)
    return response


st.set_page_config(page_title="ChatBot")

st.header('LLM ChatBot')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Enter your Question:",key='input')
submit = st.button('Ask Me')

if submit and input:
    res = get_gemini_reponse(input)
    st.session_state['chat_history'].append(("User", input))
    st.subheader("The Response is")
    for chunk in res:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.header('Chat History')
for role, text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')
