from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

import os
from langchain_mistralai import ChatMistralAI

splitter=CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)


data = TextLoader(r"C:\Users\Naitik\Desktop\ML_Projects\RAG_PROJECT\document loaders\notes.txt")

docs=data.load()
chunks=splitter.split_documents(docs)

print(len(chunks))