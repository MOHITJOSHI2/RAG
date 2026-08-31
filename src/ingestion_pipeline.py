from embedding.vector_embedding import vector_embedding
from documentLoader.documet_loader import document_loader
from chunking.chunking import chunking


def main():

    #Loading the Documents
    documents = document_loader()

    #Chunking the documents (Lists of smaller chunks)
    chunks = chunking(documents) 

    #Vector embedding
    embedding = vector_embedding(chunks)

main()
