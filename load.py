from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
load_dotenv()
llm=ChatOpenAI()

prompt=PromptTemplate(
    template="""Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context

Context: {context}
Question: {question}

Start the answer directly. No small talk please.
""",
input_variables=["context", "question"]
)
embeddings = OpenAIEmbeddings()

# Load saved FAISS database
vectorstore = FAISS.load_local("Faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Example QA chain

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever, chain_type="stuff",  # can be "map_reduce", "refine", etc.
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

def query(question):
    result = qa_chain.invoke({"query": question})

    return (result["result"])
