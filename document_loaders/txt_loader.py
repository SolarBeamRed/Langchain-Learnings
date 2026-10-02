import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from langchain_community.document_loaders import TextLoader
from llm_llamacpp import llm


loader = TextLoader('sample.txt')
document = loader.load()

# print("Type: ", type(document), end='\n\n')
# print('Length: ', len(document), end='\n\n')
# print(document[0].page_content, end='\n\n')
# print(document[0].metadata)

result = llm.invoke(f'Can you give me a 50 summary of what the document says?\nDocument content:\n{document[0].page_content}')
print("BOT RESPONSE:\n", result.content)