import chromadb


class ChromaManager:

    def __init__(self, persist_directory="data/chroma"):
        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name="multidoc_documents"
        )

    def add_documents(self, documents, embeddings, metadatas, ids):
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def search(self, query_embedding, n_results=5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )