from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
load_dotenv()
embeddings=OpenAIEmbeddings()
#step 1 load the pdf
data_path="data/"
def load_pdf(path):
    loader=DirectoryLoader(
        path=path,glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    documents=loader.load()
    return documents
documents=load_pdf(data_path)

# create chunks
def create_chunks(document):
    textsplitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunks=textsplitter.split_documents(documents)
    return text_chunks
text_chunks=create_chunks(documents)
vectorstore=FAISS.from_documents(text_chunks,embeddings)
vectorstore.save_local("Faiss_index")