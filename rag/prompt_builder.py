def build_prompt(question, context):
    prompt = f"""
You are a helpful document question-answering assistant.

Answer the user's question using only the provided document context.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded documents."

Document Context:
{context}

User Question:
{question}

Answer:
"""

    return prompt