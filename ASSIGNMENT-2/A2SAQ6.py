# Q6: Write a Python program using the SentenceTransformer library to perform extractive text summarization. The program should
#     take a paragraph as input, split it into sentences, generate sentence embeddings using a pre-trained model, extract any
#     two important sentences, and display them as a summary.
# ->

from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Enter a paragraph (press enter twice to finish): ")

lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

sentences = text.split("\n")

sentence_embedding = model.encode(sentences)

paragraph_embedding = model.encode([text])

scores = util.cos_sim(sentence_embedding, paragraph_embedding)

top_two = np.argsort(scores.flatten())[-2:]

summary = [sentences[i] for i in top_two]

print("\nSummary: ")
print(" ".join(summary))

# Transformers are powerful models for NLP tasks.
# They can generate embeddings for sentences.
# These embeddings help in text summarization.
# Extractive summarization selects key sentences.
#  