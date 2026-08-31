from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from aiConnector.LLM import llm_response

persist_directory = "db/chroma_db"

print("Loading embedding model...")


# Initializing the free embedding model from HuggungFace
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={
        "device": "cpu"
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)

print("Embedding model loaded!")

#Loading the chroma databse
db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space": "cosine"}
)

print("Chroma loaded!")


query = "what are the nine principal islands Velorian Archipelago"


#Setting retriever to get only 2 chuks
retriever = db.as_retriever(
    search_kwargs={"k": 2}
)

print("Searching...")

#Retreving only 2 relevant chunks
relevant_document = retriever.invoke(query)


# Getting the page_content from the relevant documents
context = "\n\n".join(
    doc.page_content for doc in relevant_document
)


prompt = f"""
You are a RAG agent.

Answer the user's question using ONLY the information provided
in the context.

Do not use your own knowledge unless you have solid knowledge of the context.
Do not hallucinate.

If the answer cannot be found in the context, say:
"I am unable to answer that."

Context:
{context}

Question:
{query}
"""

# Calling the LLM with prompt as parameters {my case the LLM is Mistral}
response = llm_response(prompt=prompt)


print("\n========== ANSWER ==========")
print(response["message"]["content"])