from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama  # Correct import for Ollama
import streamlit as st

# Define the prompt template (using PromptTemplate instead of ChatPromptTemplate)
prompt = PromptTemplate.from_template(
    "You are a helpful assistant. Please respond to the user's question: {question}"
)

# Streamlit framework
st.title("LangChain Demo With Ollama LLM")
input_text = st.text_input("Search the topic you want")

# Initialize the Ollama model (LLama3.2 LLM)
llm = Ollama(model="llama3.2")  # Correct initialization for Ollama

# Process user input and display the output
if input_text:
    response = llm.predict(input_text)  # Directly call predict to get the response
    st.write(response)
