# Q5: Write a program to perform sentiment analysis on multiple sentences using an LLM
# ->

from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

sentences = [
    "The movie was amazing and inspiring!",
    "I did not like the food at the restaurant.",
    "The weather today is okay."
]

res = sentiment(sentences)

for i, result in enumerate(res):
    print(f"\nSentence: {sentences[i]}")
    print(f"Sentiment: {result['label']}")
    print(f"Score: {round(result['score'], 3)}")
