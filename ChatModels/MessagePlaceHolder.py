from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import json
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
# multiple input+dynamic
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
#list of tuples
chat_template = ChatPromptTemplate([
    ('system','you are a helpful support customer agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{user_query}')
])
chat_history=[]
with open('old_chat.json') as f:
    for msg in json.load(f):
        if msg['type']=='human':
            chat_history.append(HumanMessage(content=msg['message']))
        elif msg['type']=='ai':
            chat_history.append(AIMessage(content=msg['message']))
        else:
            chat_history.append(SystemMessage(content=msg['message']))

while True:
    user_input = input("you: ") 
    if(user_input=='exit'):
        break
    prompt = chat_template.invoke({
        'chat_history':chat_history,
        'user_query':user_input
    })
    response = model.invoke(prompt)
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))
    print("AI:",response.content)

print(chat_history)    

