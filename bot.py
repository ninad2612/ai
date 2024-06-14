import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from io import BytesIO

# Function to load the language model
@st.cache_resource
def load_llm():
    return LlamaCpp(
        model_path=r"F:\LLM\Tiny\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        max_tokens=512,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        verbose=True,
        temperature=0.4,
        stop=['User :'],
        n_ctx=1000
    )

# Function to load the embeddings model
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(model_name=r'F:\LLM\Sentence_Transformers_model', model_kwargs={'device': 'cpu'})

# Text splitter configuration
@st.cache_resource
def get_text_splitter():
    return RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=124)

# Function to process uploaded PDF
def process_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Load models and components
llm = load_llm()
embeddings = load_embeddings()
text_splitter = get_text_splitter()

# Streamlit app interface
st.title("PDF Question Answering System")
st.write("Upload a PDF document and ask questions based on its content.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    # Process the uploaded PDF
    text = process_pdf(uploaded_file)
    
    # Split the document into chunks
    texts = text_splitter.split_text(text)

    # Create a FAISS vector store with the uploaded PDF
    vdb = FAISS.from_texts(texts, embeddings)
    retriever = vdb.as_retriever(search_type="similarity", search_kwargs={"k": 2}, device="cuda")
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # Text input widget for user query
    user_input = st.text_input("Input your question:", "")
    if user_input:
        # Get the answer from the question answering system
        result = qa({'query': user_input})
        st.write(f"Answer: {result['result']}")

# Run the Streamlit app with: streamlit run app.py
