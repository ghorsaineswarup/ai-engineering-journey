def clean_word(word):
    return ''.join(char for char in word if char.isalnum())


def find_best_chunk(question, chunks):
    question_words = [clean_word(w) for w in question.lower().split()]
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

question = "What time do you deliver?"
result = find_best_chunk(question, chunks)
print(result)
