from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from transformers.utils import logging


load_dotenv()
logging.set_verbosity_error()
logging.disable_progress_bar()

documents = [
    'Counter Strike is quite fun to watch. There are so many teams that compete a high level that it is very engaging.',
    'Playing Counter Strike though can be less than a fun experience. Too many smurfs, cheaters and moon ruiners',
    "Single player games have gotten more and more enjoyable the more I have grown up. There tends to be less table smashing with single player games, but that's not a gaurantee"
]

embedding = HuggingFaceEmbeddings(
    model_name='KaLM-Embedding/KaLM-embedding-multilingual-mini-instruct-v2.5'
)
result = embedding.embed_documents(documents)
print(type(result[0][0]))