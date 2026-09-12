from dotenv import load_dotenv

from transformers.utils import logging
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()
logging.disable_progress_bar()
logging.set_verbosity_error()

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation',
    pipeline_kwargs={
        'temperature':1.2,
        'max_new_tokens':2500
    }
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("Can you tell me what the optimal strategy on Dust 2 is for T side when 4 terrorists have Long spawn?")

print(result.content)