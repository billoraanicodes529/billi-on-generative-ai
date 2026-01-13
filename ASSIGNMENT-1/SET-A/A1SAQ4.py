# Q4: Write a program to perform sentiment analysis using a Large Language Model (LLM)
# ->

from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

text = "I love using AI tools, they are amazing!"
# text = "I don't like AI tools, they are not amazing!"

res = sentiment(text)

print("\n", res)

print("\nSentiment Recorded: ", res[0]["label"])
print("Score Of Sentiment: ", res[0]["score"])


