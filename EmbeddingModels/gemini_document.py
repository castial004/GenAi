from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001',dimensions=20)
documents=[
    'hello how are you',
    'hello my friend',
    'do you know kallu kallia?'
]
text_vector = embeddings.embed_documents(documents)
print(text_vector)