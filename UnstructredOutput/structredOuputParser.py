from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser , ResponseSchema
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
schema = [
    ResponseSchema(name='Full Name',description='full name of the person'),
    ResponseSchema(name='DOB',description='date of birth and age of the person'),
    ResponseSchema(name='Birth Place',description='birth place location of the person')
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(template='give me detail about this person {person}. \n {format_instruction}',
                          input_variables=['person'],
                          partial_variables={'format_instruction':parser.get_format_instructions()}
                          )

chain = template |model | parser
response = chain.invoke({'person':'narendra modi'})
print(response)