import ollama

def generate_response(message):

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ]
    )

    return response['message']['content']