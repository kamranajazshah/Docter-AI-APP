import streamlit as st
from load import query
st.title("AI MEDICAL CHATBOT")
if "message_history" not in st.session_state:
    st.session_state["message_history"]=[]
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_query =st.chat_input("enter the message")
if user_query:
    st.session_state["message_history"].append({"role":"user","content":user_query})
    with st.chat_message("user"):
        st.text(user_query)
    with st.chat_message("assistant"):
        response=query(question=user_query)
        st.write(response)

    
    st.session_state["message_history"].append({"role":"assistant","content":response})