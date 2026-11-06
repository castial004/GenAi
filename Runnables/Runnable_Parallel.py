from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-20b')
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)
paralle_chain = RunnableParallel({
    'x':RunnableSequence(prompt1,model,parser),
    'li':RunnableSequence(prompt2,model,parser)
})

response_dictionary = paralle_chain.invoke({'topic':'AI'})
print(response_dictionary)
paralle_chain.get_graph().print_ascii()