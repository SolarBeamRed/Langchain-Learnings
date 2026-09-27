from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from llm_llamacpp import llm_model


prompt1 = PromptTemplate(
    template='As an avid thinker, generate 3 points supporting the topic: {topic}',
    input_variables=['topic'],
    validate_template=True
)

prompt2 = PromptTemplate(
    template='As an avid thinker, generate 3 points against the topic: {topic}',
    input_variables=['topic'],
    validate_template=True
)

prompt3 = PromptTemplate(
    template='As an indiscriminate jury, compare these "for" and "against" points and give your judgement on what is more convincing\n"for" -> {for_text}\n"against" -> {against_text}',
    input_variables=['for_text', 'against_text'],
    validate_template=True
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'for_text': prompt1 | llm_model | parser,
    'against_text': prompt2 | llm_model | parser
})

merge_chain = prompt3 | llm_model | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'topic': 'vegetarianism'})
print(result)