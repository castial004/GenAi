from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Flash-0731:deepinfra',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("how is vellore institute of technology bhopal")
print(response.content)