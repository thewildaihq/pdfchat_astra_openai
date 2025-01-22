from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_astradb import AstraDBVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from uuid import uuid4
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def load_docs(directory):
    """Loads all pdf files from a directory"""
    loader = DirectoryLoader(path=directory, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()


def split_docs(documents):
    """Divides a document into smaller chunks """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50)
    return text_splitter.split_documents(documents)


def ingest():
    """Generates embeddings for document segments and uploads them to AstraDB"""
    try:
        documents = load_docs("./documents")
        docs = split_docs(documents)
        # print(docs)
        embeddings = OpenAIEmbeddings()        
        vector_store = AstraDBVectorStore(
            collection_name="astra_vector_langchain",
            embedding=embeddings,
            api_endpoint=os.environ['ASTRA_DB_API_ENDPOINT'],
            token=os.environ['ASTRA_DB_APPLICATION_TOKEN'],
            namespace=os.environ['ASTRA_DB_NAMESPACE'],
        )
      
        uuids = [str(uuid4()) for _ in range(len(docs))]
        result = vector_store.add_documents(documents=docs, ids=uuids)
        print(result)

        print("File inserted into vector database successfully")
    except Exception as exception_message:
        print(str(exception_message))


if __name__ == "__main__":
    ingest()
