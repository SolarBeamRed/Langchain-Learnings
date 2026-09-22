from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

from llm_llamacpp import llm_model


schema = [
    ResponseSchema(name='name', description='Car model name'),
    ResponseSchema(name='price', description='Car price'),
    ResponseSchema(name='horsepower', description='Car total horsepowers')
]
parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template='Return the name, price and horsepower of a totally random car.\n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()},
    validate_template=True
)

chain = template | llm_model | parser

while True:
    user_input = input('Give a random car? (y/n): ')
    if user_input == 'n':
        break
    print(chain.invoke({}), end='\n\n') # type: ignore