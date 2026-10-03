import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from langchain_community.document_loaders import WebBaseLoader
from llm_llamacpp import llm


url = 'https://en.uesp.net/wiki/Skyrim:Dragonbane'

loader = WebBaseLoader(
    web_path=url,
    show_progress=True,
)

docs = loader.load()
content = '\n\n'.join(doc.page_content for doc in docs)

result = llm.invoke(f"Tell me about this weapon's lore:\n{content}")
print(result.content) 