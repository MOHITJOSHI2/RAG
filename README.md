# Simple RAG Pipeline Using Mistral

A simple RAG (Retrieval-Augmented Generation) pipeline using **Mistral, Ollama, LangChain, and ChromaDB**.

## Setup

### 1. Create a virtual environment

Create and activate a virtual environment to isolate the project's dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

Install the required Python libraries:

```bash
pip install ollama langchain-text-splitters langchain-community langchain-huggingface langchain-chroma
```

Make sure **Ollama** is installed and the Mistral model is available:

```bash
ollama pull mistral
```

### 3. Add documents

Place the `.txt` files you want the RAG system to use inside the `rag_files` folder.

```text
rag_files/
├── document1.txt
├── document2.txt
└── document3.txt
```

### 4. Run the ingestion pipeline

Run the ingestion script first:

```bash
python ingestion_pipeline.py
```

This will load the documents, split them into chunks, create embeddings, and store them in ChromaDB.

### 5. Run the retrieval pipeline

Set your prompt/query inside `retrieval_pipeline.py` and then run:

```bash
python retrieval_pipeline.py
```

The retrieval pipeline will find relevant information from the stored documents and provide it as context to Mistral to generate the final answer.

## Note

If you add or modify documents in the `rag_files` folder, run `ingestion_pipeline.py` again before running the retrieval pipeline.
