from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',max_output_tokens=30)
response = model.invoke('which model you are?')
print(response.content[0]['text'])