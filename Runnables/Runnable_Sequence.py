from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
parser = StrOutputParser()
prompt1 = PromptTemplate(template='write a small joke about the {topic}',input_variables=['topic'])
prompt2 = PromptTemplate(template='return the same joke and Explain the following {joke}',input_variables=['joke'])
chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
response = chain.invoke({'topic':'AI'})
print(response)
chain.get_graph().print_ascii()