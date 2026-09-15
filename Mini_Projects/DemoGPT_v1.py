from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Flash-0731:deepinfra',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)
st.header("DemoGPT v1.0")
user_input = st.text_input("Enter your prompt")
if st.button("Send"):
    response = model.invoke(user_input)
    st.text(response.content)
