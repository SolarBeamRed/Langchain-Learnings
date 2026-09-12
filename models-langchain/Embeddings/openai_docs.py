from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

documents = [
    'Counter Strike is quite fun to watch. There are so many teams that compete a high level that it is very engaging.',
    'Playing Counter Strike though can be less than a fun experience. Too many smurfs, cheaters and moon ruiners',
    "Single player games have gotten more and more enjoyable the more I have grown up. There tends to be less table smashing with single player games, but that's not a gaurantee"
]

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=256)
result = embedding.embed_documents(documents)

print(str(result))