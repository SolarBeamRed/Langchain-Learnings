import os
import numpy as np
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"]
)


video_id = 'syE8f_ow0iM'
ytt_api = YouTubeTranscriptApi()

try:
    transcript_list = ytt_api.fetch(video_id=video_id)
    print('Length of list: ', len(transcript_list), end='\n\n')
    print(transcript_list[0], end='\n\n')
    print('Type of each transcript snippet item: ', type(transcript_list[0]))

except TranscriptsDisabled:
    print('No transcript for this video')

transcript = ' '.join(chunk.text for chunk in transcript_list).replace('\n', ' ')
print('Joined transcript total length:\n', len(transcript))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.create_documents([transcript])




# Embed all chunks
chunk_texts = [chunk.page_content for chunk in chunks]

chunk_embeddings = client.feature_extraction(
    chunk_texts,
    model="Qwen/Qwen3-Embedding-0.6B"
)

# Embed the query
query = "The Great War"
query_embedding = client.feature_extraction(
    query,
    model="Qwen/Qwen3-Embedding-0.6B"
)

chunk_embeddings = np.asarray(chunk_embeddings)
query_embedding = np.asarray(query_embedding)

# Cosine similarity
query_embedding = query_embedding / np.linalg.norm(query_embedding)
chunk_embeddings = chunk_embeddings / np.linalg.norm(
    chunk_embeddings,
    axis=1,
    keepdims=True
)

scores = chunk_embeddings @ query_embedding

# Top 10
top_indices = np.argsort(scores)[::-1][:10]

for rank, idx in enumerate(top_indices, 1):
    print(f"\n--- {rank} | score={scores[idx]:.4f} ---")
    print(chunks[idx].page_content)