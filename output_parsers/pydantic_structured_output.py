from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from llm_llamacpp import llm_model


class OutputSchema(BaseModel):
    name: str = Field(description="Car model's name")
    price: int = Field(description='Price in USD')
    horsepower: int = Field(description="Car's total horsepower output")
    company: str = Field(description="Manufacturer's name")

parser = PydanticOutputParser(pydantic_object=OutputSchema)


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