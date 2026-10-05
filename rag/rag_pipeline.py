from rag.prompt_builder import build_prompt


class RAGPipeline:

    def __init__(self, embedding_manager, retriever, ollama_client):
        self.embedding_manager = embedding_manager
        self.retriever = retriever
        self.ollama_client = ollama_client

    def ask(self, question):

        # Convert question into embedding
        query_embedding = self.embedding_manager.create_embeddings(
            [question]
        )[0]

        # Retrieve relevant chunks
        results = self.retriever.retrieve(
            query_embedding,
            n_results=5
        )

        # Get documents
        documents = results.get("documents", [[]])[0]

        # Get source information
        metadatas = results.get("metadatas", [[]])[0]

        # Combine chunks
        context = "\n\n".join(documents)

        # Build prompt
        prompt = build_prompt(question, context)

        # Generate answer
        answer = self.ollama_client.generate_answer(prompt)

        return answer, metadatas