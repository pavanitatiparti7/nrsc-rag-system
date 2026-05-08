import ollama

def generate_response(question, context):

    prompt = f"""
You are an NRSC Knowledge Expert Assistant.

Answer the question only from the provided context.

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']