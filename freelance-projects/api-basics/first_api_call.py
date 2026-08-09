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

def clean_word(word):
    return ''.join(char for char in word if char.isalnum())

def find_best_chunk(questions, chunks):
    question_words = [clean_word(w) for w in questions.lower().split()]
    best_chunk = None
    best_score = 0
    for chunk in chunks:
        chunk_words = [clean_word(w) for w in chunk.lower().split()]
        score = 0
        for word in question_words:
            if word in chunk_words:
                score += 1
        print(f"Chunk: '{chunk}' | Score: {score}")           
        if score > best_score:
            best_score = score
            best_chunk = chunk
    return best_chunk


chunks = [
    "Udhamsil Dairy sells fresh milk, cheese, yogurt, and ghee.",
    "Our milk is priced at Rs 80 per liter.",
    "We deliver every morning between 6-8 AM.",
    "Our shop is open Monday to Saturday, 7 AM to 7 PM."
]


conversation_history = [{"role": "system", "content": "You are a helpful assistant for Udhamsil Dairy Tatha Sahakari, located in Kolhavi-2, Bara, Nepal. The dairy sells milk, milk powder, ghee, paneer, curd, and other milk-related products. Help customers with questions about products, prices, availability, and orders. If asked about anything unrelated to the dairy or its products, politely redirect the conversation back to the dairy."}]

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    relevant_chunk = find_best_chunk(user_input, chunks)

    if relevant_chunk:
        context_message = f"here is some relevant information: {relevant_chunk}\n\nQuestion: {user_input}"
    else:
        context_message = user_input

    print("DEBUG - Sending to AI:",context_message)

        

    context_message = f"here is some relevant information: {relevant_chunk}\n\nQuestion: {user_input}"
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