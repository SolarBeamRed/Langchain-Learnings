from langchain_core.tools import tool

@tool
def add(a: int | float, b: int | float) -> int | float:
    ''' ADD TWO INTEGERS OR FLOATS'''
    return a+b

@tool
def subtract(a: int | float, b: int | float) -> int | float:
    ''' SUBTRACT TWO INTEGERS OR FLOATS'''
    return a-b

@tool
def multiply(a: int | float, b: int | float) -> int | float:
    ''' MULTIPLY TWO INTEGERS OR FLOATS'''
    return a*b

@tool
def divide(a: int | float, b: int | float) -> int | float:
    ''' DIVIDE TWO INTEGERS OR FLOATS'''
    return a/b

@tool
def modulus(a: int | float, b: int | float) -> int | float:
    ''' RETURN REMAINDER OF TWO INTEGERS OR FLOATS'''
    return a%b


# Create toolkit class
class MathToolKit:
    def get_tools(self):
        return [add, subtract, multiply, divide]


# Create toolkit object and use
toolkit = MathToolKit()
tools = toolkit.get_tools()

for tool in tools:
    print(f'Tool: {tool.name} ==> {tool.description}')