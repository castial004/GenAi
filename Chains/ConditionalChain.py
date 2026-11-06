from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')

class Review(BaseModel):
    sentiment:Literal['positive','negative','neutral']=Field(description='return sentiment of the review negative,neutral,positive')

parser1 = PydanticOutputParser(pydantic_object=Review)
parser2=StrOutputParser()
prompt1 = PromptTemplate(template='''Classify the sentiment of the following feedback text into postive or negative
                         \n {feedback} \n {format_instruction}''',
                         input_variables=['feedback'],
                         partial_variables={'format_instruction':parser1.get_format_instructions()})

classifier_chain = prompt1|model|parser1
prompt2 = PromptTemplate(template='Write an appropriate response to this positive feedback \n {feedback}',input_variables=['feedback'])
prompt3 = PromptTemplate(template='Write an appropriate response to this negative feedback \n {feedback}',input_variables=['feedback'])
prompt4 = PromptTemplate(template='Write an appropriate response to this negative feedback \n {feedback}',input_variables=['feedback'])
conditional_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|model|parser2),
    (lambda x:x.sentiment=='negative',prompt3|model|parser2),
    (lambda x:x.sentiment=='negative',prompt4|model|parser2),
    RunnableLambda(lambda x:'could not find sentiment')
)
chain = classifier_chain|conditional_chain
feedback='this is a terrible smart phone'

response = chain.invoke({'feedback':feedback})
print(response)
print(chain.get_graph().print_ascii())