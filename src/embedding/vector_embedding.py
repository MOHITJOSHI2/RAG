from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def vector_embedding(chunks, persist_directory="db/chroma_db"):
    print("Embedding started")

    # Local open-source embedding model
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    vectorStore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print(f"Vector store created and saved to {persist_directory}")

    return vectorStore