from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
model = ChatOpenAI(model='gpt-4',temperature=0.5,max_completion_tokens=2500)

st.header("Research Tool")

paper_input_st = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input_st = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input_st = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt("template.json")
prompt = template.invoke(
    {
        'paper_input':paper_input_st,
        'style_input':style_input_st,
        'length_input':length_input_st
    }
)

if st.button("Summarise"):
    result = model.invoke(prompt)
    st.write(result.content)
