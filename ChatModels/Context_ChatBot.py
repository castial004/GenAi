from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
chat_history=[
    SystemMessage(content="You are a helpfull assisstant")
]
while True:
    user_input=input("USER: ")
    if(user_input=='exit'): break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ",response.content)