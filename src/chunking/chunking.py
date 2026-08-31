from langchain_text_splitters import CharacterTextSplitter


def chunking(documents, chunk_size=800, chunk_overlap=0):
    print(f"Chunking started")

    spliter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap= chunk_overlap
    )

    chunks = spliter.split_documents(documents)


    '''
    Documents Format

    document = [
        Document(
            page_content="Contents of the file",
            metadata={'source':'rag_files/01_aurora_forge.txt'}
        ),
        Document(
            page_content="Contents of the file",
            metadata={'source':'rag_files/02_velorian_ecology.txt'}
        ),
    ]
    '''

    if chunks:
        for i, chunk in enumerate(chunks[:5]): # Limited chunks to 5 chunks
            print(f"chunk N.O {i+1} from Source {chunk.metadata['source']}\n")
            print(f"Chunks content____: \n {chunk.page_content}")
            print("_"*200)

    return chunks