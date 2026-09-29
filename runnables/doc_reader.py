from dotenv import load_dotenv

import fitz
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()
fitz.TOOLS.mupdf_display_errors(False)
fitz.TOOLS.mupdf_display_warnings(False)

loader = PyMuPDFLoader('sample-text-only.pdf')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
docs = text_splitter.split_documents(documents)

embedder = OpenAIEmbeddings(
    model='local qwen emdedding',
    base_url='http://127.0.0.1:8081/v1/'
)
vectorstore = FAISS.from_documents(docs, embedding=embedder)

retriever = vectorstore.as_retriever()


# retrieving relevant text
query = 'What is the document about?'
retrieved_docs = retriever.invoke(query)

retrieved_text = '\n'.join([doc.page_content for doc in retrieved_docs])

llm = ChatOpenAI(
    model='local qwen model',
    base_url='http://127.0.0.1:8080/v1'
)

template = PromptTemplate(
    template='Answer the following query: {query}\n\n{retrieved_text}',
    input_variables=['query', 'retrieved_text'],
    validate_template=True
)
prompt = template.invoke({'query':query, 'retrieved_text':retrieved_text})
result = llm.invoke(prompt)

print('USER QUERY: ', query, end='\n\n')
print('AGENT RESPONSE: ', result.content, end='\n\n')