import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader



def document_loader(path="rag_files"):
    print(f"Loading files from {path}")

    #Check for path existence
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory named {path} does not exists")

    #Now load the .txt files from the directry
    loader = DirectoryLoader(
        path=path,
        glob="*.txt", # tells which files to select from the folder
        loader_cls=TextLoader # fro every files use textLoader to read it
    )

    #Calls the load function to load the documents
    documents = loader.load()

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

    #Checks for the length of the documents
    if len(documents) == 0:
        raise FileNotFoundError(f"No .txt files found in {path}")

    # Just for showing the name of the files and their content length
    for i, doc in enumerate(documents):
        print(f"Loading document {doc.metadata['source'][11:]} Content characters {len(doc.page_content)}")

    return documents