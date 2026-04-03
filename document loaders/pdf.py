from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

import os
from langchain_mistralai import ChatMistralAI



data = PyPDFLoader(r"C:\Users\Naitik\Desktop\ML_Projects\RAG_PROJECT\document loaders\GRU.pdf")

docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=10
)

chunks=splitter.split_documents(docs)

print(len(chunks))