import os
import unicodedata
from langchain.document_loaders import (
    DirectoryLoader, MergedDataLoader, TextLoader, CSVLoader, 
    UnstructuredWordDocumentLoader, UnstructuredEPubLoader, 
    UnstructuredMarkdownLoader, UnstructuredODTLoader, PyPDFLoader, 
    UnstructuredPowerPointLoader, NotebookLoader, PythonLoader, 
    JSONLoader, BSHTMLLoader, UnstructuredXMLLoader, UnstructuredExcelLoader
)
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA

# Function to prompt the user for directory input
def get_user_directory():
    return input("Please enter the directory path containing the files: ")

# Get the directory from the user
user_directory = get_user_directory()

# Ensure the directory exists
if not os.path.isdir(user_directory):
    raise ValueError(f"The provided directory does not exist: {user_directory}")

# Define a cleaning function
def clean_text(text):
    allowed_categories = ['Ll', 'Lu', 'Nd', 'Pc', 'Pd']
    cleaned_text = ''.join(c for c in text if unicodedata.category(c) in allowed_categories or c == ' ')
    cleaned_text = cleaned_text.replace('NaN', ' ')
    return cleaned_text

# Individual loaders for each file type
loader_txt = DirectoryLoader(user_directory, glob="*.txt", loader_cls=TextLoader, use_multithreading=True, show_progress=True)
loader_csv = DirectoryLoader(user_directory, glob="*.csv", loader_cls=CSVLoader, use_multithreading=True, show_progress=True)
loader_doc = DirectoryLoader(user_directory, glob="*.doc", loader_cls=UnstructuredWordDocumentLoader, use_multithreading=True, show_progress=True)
loader_docx = DirectoryLoader(user_directory, glob="*.docx", loader_cls=UnstructuredWordDocumentLoader, use_multithreading=True, show_progress=True)
loader_epub = DirectoryLoader(user_directory, glob="*.epub", loader_cls=UnstructuredEPubLoader, use_multithreading=True, show_progress=True)
loader_md = DirectoryLoader(user_directory, glob="*.md", loader_cls=UnstructuredMarkdownLoader, use_multithreading=True, show_progress=True)
loader_odt = DirectoryLoader(user_directory, glob="*.odt", loader_cls=UnstructuredODTLoader, use_multithreading=True, show_progress=True)
loader_pdf = DirectoryLoader(user_directory, glob="*.pdf", loader_cls=PyPDFLoader, use_multithreading=True, show_progress=True)
loader_ppt = DirectoryLoader(user_directory, glob="*.ppt", loader_cls=UnstructuredPowerPointLoader, use_multithreading=True, show_progress=True)
loader_pptx = DirectoryLoader(user_directory, glob="*.pptx", loader_cls=UnstructuredPowerPointLoader, use_multithreading=True, show_progress=True)
loader_ipynb = DirectoryLoader(user_directory, glob="*.ipynb", loader_cls=NotebookLoader, use_multithreading=True, show_progress=True)
loader_py = DirectoryLoader(user_directory, glob="*.py", loader_cls=PythonLoader, use_multithreading=True, show_progress=True)
loader_json = DirectoryLoader(user_directory, glob="*.json", loader_cls=JSONLoader, use_multithreading=True, show_progress=True)
loader_html = DirectoryLoader(user_directory, glob="*.html", loader_cls=BSHTMLLoader, use_multithreading=True, show_progress=True)
loader_xml = DirectoryLoader(user_directory, glob="*.xml", loader_cls=UnstructuredXMLLoader, use_multithreading=True, show_progress=True)
loader_log = DirectoryLoader(user_directory, glob="*.log", loader_cls=TextLoader, use_multithreading=True, show_progress=True)
loader_xlsx = DirectoryLoader(user_directory, glob="*.xlsx", loader_cls=UnstructuredExcelLoader, use_multithreading=True, show_progress=True)

# Merged loader combining all individual loaders
loader_all = MergedDataLoader(loaders=[
    loader_txt, loader_csv, loader_doc, loader_docx, loader_epub, loader_md, 
    loader_odt, loader_pdf, loader_ppt, loader_pptx, loader_ipynb, loader_py, 
    loader_json, loader_html, loader_xml, loader_log, loader_xlsx
])

# Load all files from the user-provided directory
documents = loader_all.load()

# Clean the content of each document immediately after loading
for document in documents:
    document.page_content = clean_text(document.page_content)

# Initialize LLM
llm = LlamaCpp(
    model_path=r"F:\LLM\Tiny\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    max_tokens=512,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=True,
    temperature=0.4,
    stop=['User :'],
    n_ctx=4096
)

print(documents)

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name=r'F:\LLM\Sentence_Transformers_model', model_kwargs={'device': 'cpu'})

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split documents into chunks
texts = text_splitter.split_documents(documents)

# Create FAISS vector store from documents
vdb = FAISS.from_documents(texts, embeddings)

# Create a retriever
retriever = vdb.as_retriever(search_type="similarity", search_kwargs={"k": 2})

# Create a question answering system based on information retrieval
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Interactive loop to query the system
import sys

while True:
    user_input = input("Input Prompt: ")
    if user_input.lower() == 'exit':
        print('Exiting')
        sys.exit()
    if user_input == '':
        continue
    # Pass the query to the system and print the response
    result = qa({'query': user_input})
    print(f"Answer: {result['result']}")
