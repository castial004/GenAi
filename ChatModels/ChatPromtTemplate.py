from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
#used when you want to pass a list of messages to llm instead of 1(ie: PromptTemplate)
template = ChatPromptTemplate([
    ('system','your are a helpfull assistant expert in domain {domain}'),
    ('human','{query}')
])
st.header("Ai Assistant")
domain = st.selectbox('select domain',['coding','research','gaming','romantic'])
user_input = st.text_input("enter your query")
chain = template|model
if st.button("send"):
    response = chain.invoke({
        'domain':domain,
        'query':user_input
    })
    st.text(response.content)