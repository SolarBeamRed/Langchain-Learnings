from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class AdditionInputClass(BaseModel):
    a: int | float = Field(description='first number to add')
    b: int | float = Field(description='second number to add')

class AddTool(BaseTool):
    name: str = 'add'
    description: str = 'ADD TWO INTEGERS OR FLOATS'
    args_schema: Type[BaseModel] = AdditionInputClass

    def _run(self, a: int | float, b: int | float) -> int | float:
        return a+b


add_tool = AddTool()

print('Tool name: ', add_tool.name)
print('Tool description: ', add_tool.description)
print('Tool args: ', add_tool.args)

print('\nResult of add tool for 24.1 + 52.19:\n')
print(add_tool.invoke({'a':24.1, 'b':52.19}))
