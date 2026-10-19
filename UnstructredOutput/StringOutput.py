from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


model = ChatGroq(model='openai/gpt-oss-20b')
template1 = PromptTemplate(template='create a detailed report on {topic}',input_variables=['topic'])
template2 = PromptTemplate(template='create a 5 line summary on {text}',input_variables=['text'])
parser = StrOutputParser()
chain = template1 | model | parser | model |parser
result = chain.invoke({'topic':"gta 6"})
print(result)
