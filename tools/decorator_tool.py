from langchain_core.tools import tool

@tool
def add(a: int | float, b: int | float) -> int | float:
    ''' ADD TWO INTEGERS OR FLOATS'''
    return a+b

print('Tool name: ', add.name, end='\n\n')
print('Tool description: ', add.description, end='\n\n')
print('Tool arguments: ', add.args, end='\n\n')

result = add.invoke({'a':4, 'b':15})
print('Tool result on 4 + 15: ', result)