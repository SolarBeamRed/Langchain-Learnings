from typing import Literal

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from llm_llamacpp import llm_model


str_parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='sentiment of text')
    review: str = Field(description='Include the exact review that was originally received. Do not modify the review')
pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)


sentiment_prompt = PromptTemplate(
    template="""
Classify the following review's sentiment.

Use exactly one of:
- positive
- negative

If the review is neutral, classify it as negative. But keep in mind of slang language.
For example, "cool" is used as a positive statement

Review:
{feedback}

{format_instructions}
""",
    input_variables=['feedback'],
    partial_variables={
        'format_instructions': pydantic_parser.get_format_instructions()
    },
    validate_template=True
)

classifier_chain = sentiment_prompt | llm_model | pydantic_parser


positive_prompt = PromptTemplate(
    template='You are replying to a positive review. Be thankful and reply with a request to leave a Maps review. Make your reply personalised to the review left by the user\nReview: {feedback}',
    input_variables=['feedback']
)

negative_prompt = PromptTemplate(
    template='You are replying to a negative review. Console the user, apologise, and assure them that the customer support team will assist them in no time. Make your reply personalised to the review left by the user\nReview: {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', positive_prompt | llm_model | str_parser),
    (lambda x:x.sentiment == 'negative', negative_prompt | llm_model | str_parser),
    RunnableLambda(lambda x: 'not sure about sentiment')
)


chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'I will support this product like I support Bulbasaur'})
print(result)
