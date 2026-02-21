# 7) Develop an interactive Sentiment Analysis Chatbot in Python using a pre-trained transformer model.
# Write a Python program that uses Transformers pipeline to perform sentiment analysis on user input in a loop until the user exits.

from transformers import pipeline

bot = pipeline("sentiment-analysis")

print("Sentiment Detection Chatbot (type 'exit' to stop)")

while True:
    text = input("You: ")

    if text.lower() == "exit":
        print("Bot: Goodbye")
        break

    result = bot(text)[0]
    print("Bot: Sentiment =", result["label"])