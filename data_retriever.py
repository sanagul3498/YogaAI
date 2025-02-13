import os 
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

def web_database(question):
    pages = [
    "http://soulfulstretch.liveblog365.com/",
    ]
    docs = []
    for page in pages:
        loader = WebBaseLoader(page)
        docs.extend(loader.load())

    vector_store = InMemoryVectorStore.from_documents(docs, OpenAIEmbeddings())
    documents = vector_store.similarity_search(question)
    return  " ".join([page.page_content for page in documents]) 
