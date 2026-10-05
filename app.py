import streamlit as st
import tempfile
from pathlib import Path
import uuid

from ingestion.document_processor import process_document
from utils.helpers import chunk_text
from embeddings.embedding_manager import EmbeddingManager
from vectorstore.chroma_manager import ChromaManager
from retrieval.retriever import Retriever
from llm.ollama_client import OllamaClient
from rag.rag_pipeline import RAGPipeline


st.set_page_config(
    page_title="MultiDoc AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 MultiDoc AI")
st.write("Multi-Document Retrieval-Augmented Question Answering System")


# Initialize components
embedding_manager = EmbeddingManager()
vectorstore = ChromaManager()
retriever = Retriever(vectorstore)
ollama_client = OllamaClient()

rag_pipeline = RAGPipeline(
    embedding_manager,
    retriever,
    ollama_client
)


# Sidebar
st.sidebar.header("📂 Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF, DOCX or TXT files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)


# Process documents
if uploaded_files:

    for uploaded_file in uploaded_files:

        suffix = Path(uploaded_file.name).suffix

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(uploaded_file.getbuffer())
            temp_path = temp_file.name

        try:
            text = process_document(temp_path)

            chunks = chunk_text(text)

            # Create embeddings
            embeddings = embedding_manager.create_embeddings(chunks)

            # Create unique IDs
            ids = [
                f"{uploaded_file.name}_{uuid.uuid4().hex}_{i}"
                for i in range(len(chunks))
            ]

            # Metadata
            metadatas = [
                {"source": uploaded_file.name}
                for _ in chunks
            ]

            # Store in ChromaDB
            vectorstore.add_documents(
                documents=chunks,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )

            st.success(
                f"✅ {uploaded_file.name} processed and stored!"
            )

            st.write(f"Extracted characters: {len(text)}")
            st.write(f"Created chunks: {len(chunks)}")

        except Exception as e:
            st.error(
                f"Error processing {uploaded_file.name}: {e}"
            )


# Question section
# Question section
st.divider()

st.subheader("💬 Ask a Question")

question = st.text_input(
    "Ask something about your uploaded documents:"
)

if st.button("🔍 Ask"):

    if not question:
        st.warning("Please enter a question.")

    elif not uploaded_files:
        st.warning("Please upload a document first.")

    else:
        with st.spinner("🤖 Generating answer..."):

            try:
                answer, sources = rag_pipeline.ask(question)

                st.subheader("🤖 Answer")
                st.write(answer)

                st.subheader("📚 Sources")

                if sources:
                    source_names = set()

                    for source in sources:
                        if source and "source" in source:
                            source_names.add(source["source"])

                    for source_name in source_names:
                        st.write(f"📄 {source_name}")

                else:
                    st.write("No source information available.")

            except Exception as e:
                st.error(f"Error generating answer: {e}")