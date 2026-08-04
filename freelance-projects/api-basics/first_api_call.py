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

data = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {"role": "user", "content": "What is 2+2?"}
    ]
}

response = requests.post(url, headers=headers, json=data)

print("Status code:", response.status_code)
print("Response:", response.text)

result = response.json()
answer = result["choices"][0]["message"]["content"]
print("AI's answer:", answer)