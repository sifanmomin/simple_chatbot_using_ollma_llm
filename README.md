# LangChain Demo With Ollama LLM

This repository contains a chatbot application built using LangChain, Streamlit, and the Ollama LLM. The application allows users to interact with an AI-powered assistant to get responses based on their input.

## Preview

![App Preview](./Screenshot%202025-01-21%20152130.png)

## Features

- **Interactive Chatbot**: The app uses LangChain and the Ollama LLM for natural language processing.
- **Streamlit Interface**: Simple and intuitive UI for interacting with the chatbot.
- **Custom Prompts**: Uses a customizable prompt template for tailored responses.

## Installation and Setup

### Prerequisites

- Python 3.10
- Streamlit and required dependencies (see `requirements.txt`)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Create a Virtual Environment:

bash
Copy
Edit
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the App:

bash
Copy
Edit
streamlit run main.py
Open the link provided in the terminal (usually http://localhost:8501) to access the app.

File Structure
plaintext
Copy
Edit
your-repo-name/
├── main.py                # Streamlit app code
├── requirements.txt       # Required dependencies
├── runtime.txt            # Runtime configuration for deployment
├── Screenshot 2025-01-21 152130.png  # Screenshot for README
└── README.md              # This file
Example Usage
Here’s a quick example of how the app works:

Enter a question or topic in the input box (e.g., "Explain the Fibonacci sequence").
The chatbot will generate a helpful response using the Ollama LLM.
View the results displayed below the input field.
Code Example
Below is the core code used for this application:

python
Copy
Edit
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama  # Correct import for Ollama
import streamlit as st

# Define the prompt template correctly
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Please respond to the user's question: {question}"
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
Dependencies
Ensure the following dependencies are listed in requirements.txt:

plaintext
Copy
Edit
streamlit==1.14.0
langchain==0.0.27
langchain_community==0.0.27
pydantic==1.10.4
pyyaml==6.0
requests==2.28.1
sqlalchemy==2.0.9
python-dotenv==0.21.0
altair==4.2.2
Deployment
For deploying on platforms like Streamlit Sharing or other cloud services:

Ensure the runtime.txt file specifies the correct Python version (python-3.10).
Push your code and dependencies to GitHub.
Use the deployment platform's documentation for further instructions.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License. See LICENSE for details.

Enjoy exploring LangChain and Ollama LLM with this chatbot application!

vbnet
Copy
Edit

This file integrates your screenshot and provides a complete guide for users of your GitHub repository. Let me know if you’d like to modify or add anything!






