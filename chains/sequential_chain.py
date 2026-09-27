from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_llamacpp import llm_model


prompt1 = PromptTemplate(
    template='As an expert mechanical engineer, explain about {topic} in 100-250 words',
    input_variables=['topic'],
    validate_template=True
)

prompt2 = PromptTemplate(
    template='Generate summary from following text:\n{text}',
    input_variables=['text'],
    validate_template=True
)

parser = StrOutputParser()


chain = prompt1 | llm_model | parser | prompt2 | llm_model | parser # type: ignore


while True:
    topic = input('Car topic you want to ask about? (type n to quit)\n')
    if topic == 'n':
        break
    result = chain.invoke({'topic': topic})
    print(result, end='\n\n')