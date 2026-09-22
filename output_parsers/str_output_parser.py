from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from llm_llamacpp import llm_model

# First prompt to generate some text, second prompt to summarise the text

template1 = PromptTemplate(
    template='Write a 250 word report on "{topic}"',
    input_variables=['topic'],
    validate_template=True
)

template2 = PromptTemplate(
    template='Write a 3 line summary of "{report}"',
    input_variables=['report'],
    validate_template=True
)

parser = StrOutputParser()

chain = template1 | llm_model | parser | template2 | llm_model | parser # pyright: ignore[reportOperatorIssue]

while True:
    topic = input('Enter topic (type "exit" to quit): ')
    if topic == 'exit':
        break
    result = chain.invoke({'topic': topic})
    print(result, end='\n\n\n')