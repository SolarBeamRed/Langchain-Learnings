from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_llamacpp import llm_model


template = PromptTemplate(
    template='As an expert mechanical engineer, explain about {topic} in 100-250 words',
    input_variables=['topic'],
    validate_template=True
)

parser = StrOutputParser()

chain = template | llm_model | parser


while True:
    topic = input('Car topic you want to ask about? (type n to quit)\n')
    if topic == 'n':
        break
    result = chain.invoke({'topic': topic})
    print(result, end='\n\n')