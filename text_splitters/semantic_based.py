import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from langchain_experimental.text_splitter import SemanticChunker
from llm_llamacpp import embedder

text = '''
Counter Strike is a fun game to watch, not really a fun game to play. Lot of problems with playing the game itself, but the tournaments are fun as hell. Colleges are damn boring, I dont really like going to college. It's so damn bad

I prefer PCs over consoles. There's just more freedom in how you can use the product that you paid a whole bunch of money for. You don't want to pay thousands for a device only for it to be in a jail now, do you?
'''

splitter = SemanticChunker(
    embeddings=embedder,
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

docs = splitter.split_text(text)
print(len(docs))
for doc in docs:
    print(doc, end='\n\n')

# Bad performance