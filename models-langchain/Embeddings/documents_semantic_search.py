from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from transformers.utils import logging


load_dotenv()
logging.set_verbosity_error()
logging.disable_progress_bar()

embedder = HuggingFaceEmbeddings(
    model_name='KaLM-Embedding/KaLM-embedding-multilingual-mini-instruct-v2.5'
)

docs = [
    "Counter Strike 2 is a tactical FPS released by Valve maintained by the community " \
    "at this point. It's a 5v5 team based game where one side has to plant bombs in designated " \
    "sites, and the other team has to prevent them from doing so or defuse it later.", 

    "Rise of Nations is a RTS game where you can choose to play as one of many nations. " \
    "Each nation has their own nation powers as well as unique troops. This makes it fun to play. " \
    "You can play one against one or play based on teams as well. You should try it out.", 

    "Need for Speed Most Wanted is a damn fun racing game. I love it. " \
    "The protagonist car is the famed BMW M3 GTR. One of like 3 dream cars of mine. " \
    "The Dodge Viper SRT in the game is also iconic, and one of the more beautiful cars I've seen."
]

query = 'Tell me about any racing games that are present in the given docs.'

docs_embeddings = embedder.embed_documents(docs)
query_embeddings = embedder.embed_query(query)

# Cosine similarity function expects two 2D array like inputs
scores = cosine_similarity([query_embeddings], docs_embeddings) # type: ignore
ranked = sorted(
    enumerate(scores[0]),
    key=lambda x: x[1],
    reverse=True
)

print(scores)
print(f'Most relevant doc for the given query: Doc {ranked[0][0]}')
print(f'\nDoc content:\n {docs[ranked[0][0]]}')