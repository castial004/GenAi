from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')
st.header("Reasearch Tool")
user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    response = model.invoke(user_input)
    st.text(response.content)
