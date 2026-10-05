import ollama


class OllamaClient:

    def __init__(self, model="llama3.2"):
        self.model = model

    def generate_answer(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]