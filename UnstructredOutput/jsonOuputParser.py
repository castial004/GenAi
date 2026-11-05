from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
parser = JsonOutputParser()

model = ChatGroq(model = 'openai/gpt-oss-20b')
template = PromptTemplate(
    template = """can you provide me few details on narendra modi.\n {format_instruction}""",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()})

# prompt = template.invoke({})
prompt = template.format()
response = model.invoke(prompt)
# print(response.content)
# print(type(response.content)) type will be str
final_response = parser.parse(response.content)
print(final_response)
print(final_response["name"])
print(type(final_response))