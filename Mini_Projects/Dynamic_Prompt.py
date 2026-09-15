from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate 
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
st.header("GPT v1.0")
research_paper = st.selectbox('select reasearch paper name',['Attention is all you need','BERT: Pre-training of Deep Bidirectional Transformers'])
style = st.selectbox('select explaination style',["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length = st.selectbox('length of explaination',["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

dynamic_prompt_template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=['paper_input','style_input','length_input']
)
#fill the template
prompt = dynamic_prompt_template.invoke({
    'paper_input':research_paper,
    'style_input':style,
    'length_input':length
})


if st.button("Summarize"):
    result = model.invoke(prompt)
    st.text(result.content)