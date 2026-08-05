import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Conversation memory
messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Remember user's message
    messages.append({
        "role": "user",
        "content": user_input
    })

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": messages
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        answer = result["choices"][0]["message"]["content"]

        print("AI:", answer)

        # Remember AI's reply
        messages.append({
            "role": "assistant",
            "content": answer
        })

    except requests.exceptions.RequestException as e:
        print("Error:", e)