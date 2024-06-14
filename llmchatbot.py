from PyPDF2 import PdfReader
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

tempelate = """
{context}
Question: {question}
Helpful Answer:
"""

llm=LlamaCpp(
    model_path = r"F:\LLM\Tiny\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    max_tokens = 512,
    CallbackManager = CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose= True,
    temperature = 0.4,
    stop = ['User :'],
    n_ctx=4096

)

embeddings = HuggingFaceEmbeddings(model_name=r'F:\LLM\Sentence_Transformers_model', model_kwargs={'device':'cpu'})

text_splitter = RecursiveCharacterTextSplitter(chunk_size= 1000,chunk_overlap=200)

from langchain.document_loaders import PyPDFLoader


loader = PyPDFLoader(r"F:\LLM\Vedantcv (3).pdf")
data = loader.load_and_split()

texts = text_splitter.split_documents(data) 

vdb = FAISS.from_documents(texts,embeddings)

retriever= vdb.as_retriever(serach_type="similarity",search_kwargs={"k":2},device="cuda")

# Create a question answering system based on information retrieval using the RetrievalQA class, which takes as input a neural language model, a chain type and a retriever (an object that allows you to retrieve the most relevant chunks of text for a query)
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Create an infinite loop to interact with the system, asking the user to enter a query or exit the program
import sys

while True:
  user_input = input(f"Input Prompt: ")
  if user_input == 'exit':
    print('Exiting')
    sys.exit()
  if user_input == '':
    continue
  # pass the query to the system and print the response
  result = qa({'query': user_input})
  print(f"Answer: {result['result']}")