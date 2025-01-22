"""Query the vector database to retrieve relevant text segments, then input
these segments into the LLM to produce a concise response."""
import os

from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore

load_dotenv()

def connectdb():
    embeddings = OpenAIEmbeddings()
    vectorstore = AstraDBVectorStore(
              collection_name="astra_vector_langchain",
              embedding=embeddings,
              api_endpoint=os.environ['ASTRA_DB_API_ENDPOINT'],
              token=os.environ['ASTRA_DB_APPLICATION_TOKEN'],
              namespace=os.environ['ASTRA_DB_NAMESPACE'],
          )
    return vectorstore

def search_docs(query: str):
    """get similar docs from the vector db"""
    vectorstore = connectdb()
    results = vectorstore.similarity_search_with_score(query, k=3)
    return results


def query_llm(query: str):
    """send query to the llm after getting similar docs from the vector db and append the question to the end """
    # to use with LmStudio just uncomment the code below
    llm = ChatOpenAI( 
    #   base_url="http://127.0.0.1:1234/v1",
    #   model="mistral-nemo-instruct-2407",
    )
    
    chain = load_qa_chain(llm, "stuff")
    similar_docs = search_docs(query)
    docs = []
    for doc in similar_docs:
        docs.append(doc[0])
    chain_response = chain.invoke(input={"input_documents": docs, "question": query})
    return chain_response["output_text"]


def main():
    try:
        query = input("Enter your question: ")
        answer = query_llm(query)
        print(answer)
        return
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    main()
