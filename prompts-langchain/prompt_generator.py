from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["engine_type_input", "style_input", "length_input"],
    validate_template=True,
    template="""You are an expert internal combustion (IC) engine explainer.

Explain the following IC engine based on the user's inputs:

Engine type: {engine_type_input}
Explanation style: {style_input}
Desired explanation length: {length_input}

Provide a clear and technically accurate explanation. Cover the engine's basic working principle, major components, combustion cycle, and how the components interact. Adapt the terminology, complexity, tone, and level of detail to the requested explanation style and length.

Do not discuss unrelated engine types unless they are necessary for comparison or clarification."""
)

# Save as JSON instead of python object
template.save('template.json')