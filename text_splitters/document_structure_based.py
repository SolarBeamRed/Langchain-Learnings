from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = '''
class SampleClass1:
    def __init__(self) -> None:
        pass

    def greet(self):
        print('Hello')

class SampleClass2:
    def __init__(self) -> None:
        pass

    def greet(self):
        print('Hi')
'''

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=150,
    chunk_overlap=20,
    language=Language.PYTHON
)

chunks = splitter.split_text(text=text)
print(chunks[0])