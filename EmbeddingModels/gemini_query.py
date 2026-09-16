from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001',dimensions=10)
text_vector = embeddings.embed_query('hi i am kallu kalia')
print(text_vector)