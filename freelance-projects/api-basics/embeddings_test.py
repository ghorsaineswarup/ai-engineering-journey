from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

sentence = "We deliver every morning between 6-8 AM."
embedding = model.encode(sentence)


print(embedding)
print(embedding.shape)