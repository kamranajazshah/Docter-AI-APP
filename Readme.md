🩺 Doctor AI – Medical Chatbot

Doctor AI is an AI-powered medical assistant built using LangChain, FAISS, and Streamlit.
It allows users to ask health-related questions and receive informative, reliable responses, powered by vector search over trusted medical resources such as the Gale Encyclopedia of Medicine.

⚡ Features

💬 Conversational Chatbot – Ask medical questions in natural language.

📚 Knowledge Base – Uses FAISS vector database built from medical texts.

🔎 Semantic Search – Retrieves the most relevant chunks of information.

🧠 AI-Powered Answers – Combines retrieval with LLMs for accurate responses.

🖥️ Streamlit Interface – Clean and interactive web app.

🛡️ Disclaimer – Provides information only, not medical advice.

🛠️ Tech Stack

Python 3.10+

Streamlit
 – Web interface

LangChain
 – Retrieval Augmented Generation (RAG)

FAISS
 – Vector similarity search

[OpenAI / HuggingFace Models] – Language models

📂 Project Structure
Doctor-AI-APP/
│── load.py              # Handles FAISS loading & query function
│── app.py               # Streamlit frontend
│── data/                # Medical texts (Gale Encyclopedia, etc.)
│── faiss_index/         # Saved FAISS vector store
│── requirements.txt     # Project dependencies
│── README.md            # Documentation
