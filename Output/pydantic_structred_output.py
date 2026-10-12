from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal,Optional
load_dotenv()
model = ChatGroq(model = 'openai/gpt-oss-20b')

class Review(BaseModel):
    key_themes: list[str] = Field(description="write the all key themes discussed in the review in a list")
    summary:str = Field(description="a brief overview of thr review")
    sentiment: Literal['negative','positive'] = Field(description="return sentiment of the review negative,neutral,positive")
    pros: Optional[list[str]] = Field(default=None,description="write all pros mentioned in the review inside the list ")
    cons: Optional[list[str]] = Field(default=None,description="write all cons mentioned in the review inside the list ")

structred_model = model.with_structured_output(Review)
#pydantic object not a dictionary
response = structred_model.invoke("""
    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
    
        The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
    
        However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
    
        Pros:
        Insanely powerful processor (great for gaming and productivity)
        Stunning 200MP camera with incredible zoom capabilities
        Long battery life with fast charging
        S-Pen support is unique and useful
                                        
        Review by Nitish Singh
""")
print(response.summary)
print(response.key_themes)
print(response.sentiment)
print(response.pros)
print(response.cons)