from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')
class person(BaseModel):
    name:str=Field(description='full name of the person')
    age:int=Field(gt=20,lt=75,description='date of birth and age of the person')
    occupation:str=Field(description='currunt occupation of the person')

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(template='''give me detail about this person {person}. \n {format_instruction}''',
                          input_variables=['person'],
                          partial_variables={'format_instruction':parser.get_format_instructions()}
                          )

prompt = template.invoke({'person':'narendra modi'})
result = model.invoke(prompt)
print(result.content)