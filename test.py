import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore

load_dotenv()

def testSearch():
  vectorstore = db()
  results = vectorstore.similarity_search("what this pdf is about ?", k=3)

  for res in results:
      print(f"* {res.page_content} [{res.metadata}]")


def db():
    embeddings = OpenAIEmbeddings()
    vectorstore = AstraDBVectorStore(
              collection_name="astra_vector_langchain",
              embedding=embeddings,
              api_endpoint=os.environ['ASTRA_DB_API_ENDPOINT'],
              token=os.environ['ASTRA_DB_APPLICATION_TOKEN'],
              namespace=os.environ['ASTRA_DB_NAMESPACE'],
          )
    return vectorstore

if __name__ == "__main__":
    testSearch()
