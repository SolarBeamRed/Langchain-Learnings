from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import load_prompt

from llm_llamacpp import llm_model


load_dotenv()

st.header('IC Engine Enthusiast')


engine_type_input = st.selectbox('Select Engine type', [
    'V4', 'V6', 'V8', 'W16'])

style_input = st.selectbox('Select explanation type', [
    'Casual', 'Technical', 'Physics-focused'])

length_input = st.selectbox('Select length of explanation', [
    'Short(100-150) words', '250-300 words', 'Long(>350) words'])


template = load_prompt('template.json')


if st.button('Explain'):
    chain = template | llm_model
    result = chain.invoke({
    'engine_type_input': engine_type_input,
    'style_input': style_input,
    'length_input': length_input
    }).content
    if '</think>' in result:
        output = result.split('</think>', maxsplit=1)[1].strip() # type: ignore
    else:
        output = result.strip() # type: ignore
    st.write(output)