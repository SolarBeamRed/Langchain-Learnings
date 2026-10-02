import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

import fitz
from langchain_community.document_loaders import PyMuPDFLoader
from llm_llamacpp import llm

fitz.TOOLS.mupdf_display_errors(False)
fitz.TOOLS.mupdf_display_warnings(False)


loader = PyMuPDFLoader('sample.pdf')
docs = loader.load()


result = llm.invoke(f'Tell me in 50 words what this document is about. Document:\n{docs}')
print(result.content)