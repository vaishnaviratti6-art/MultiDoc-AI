class Retriever:

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def retrieve(self, query_embedding, n_results=5):
        results = self.vectorstore.search(
            query_embedding,
            n_results=n_results
        )

        return results