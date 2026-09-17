from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as numpy
load_dotenv()

query='tell me about sahil mall'
documents=[
    'sahil mall is a very good kind hearted person',
    'sahil is good at coding',
    'today is sunday',
    'hasnain is a boy'
]

embeddings = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')

doc_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)

#cosin_siilarity need 2d array 1.query 2.documents
scores = cosine_similarity([query_embeddings],doc_embeddings)[0]
index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] #get the last item
print(query)
print(documents[index])
print('similarity score is: ',score)