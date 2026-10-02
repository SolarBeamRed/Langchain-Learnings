import fitz
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader, TextLoader 
from llm_llamacpp import llm

fitz.TOOLS.mupdf_display_errors(False)
fitz.TOOLS.mupdf_display_warnings(False)


loaders = [
    DirectoryLoader(path='.', glob='**/*.pdf', loader_cls=PyMuPDFLoader),
    DirectoryLoader(path='.', glob='**/*.txt', loader_cls=TextLoader),
]

docs = []

for loader in loaders:
    docs.extend(loader.lazy_load())

content = '\n\n'.join(doc.page_content for doc in docs)

result = llm.invoke(
    f"""Are there two separate topics in this entire content,
or is it about the same thing?

Complete content:
{content}"""
)

result = llm.invoke(f'Are there two separate topics in this entire content, or is it about the same thing? Tell in a single paragraph. Complete content:\n{content}')
print(result.content)