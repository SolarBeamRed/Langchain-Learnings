from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool

class AdditionInputClass(BaseModel):
    a: int | float = Field(description='first number to add')
    b: int | float = Field(description='second number to add')

def add(a: int | float, b: int | float) -> int | float:
    return a+b

add_tool = StructuredTool(
    func=add,
    name='add',
    description='Add two integers or floats',
    args_schema=AdditionInputClass
)

print('Tool name: ', add_tool.name)
print('Tool description: ', add_tool.description)
print('Tool args: ', add_tool.args)

print('\nResult of add tool for 24.1 + 52.19:\n')
print(add_tool.invoke({'a':24.1, 'b':52.19}))