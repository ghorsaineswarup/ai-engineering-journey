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

conversation_history = [{"role": "system", "content": "You are a helpful assistant for Udhamsil Dairy Tatha Sahakari, located in Kolhavi-2, Bara, Nepal. The dairy sells milk, milk powder, ghee, paneer, curd, and other milk-related products. Help customers with questions about products, prices, availability, and orders. If asked about anything unrelated to the dairy or its products, politely redirect the conversation back to the dairy."}]
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    conversation_history.append({"role": "user", "content": user_input})

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": conversation_history
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        print("AI:", answer)

        conversation_history.append({"role": "assistant", "content": answer})

    except requests.exceptions.RequestException as e:
        print("Error:", e)