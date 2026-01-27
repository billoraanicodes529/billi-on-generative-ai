# Q7: Write a program that uses a zero-shot classification LLM to classify a sentence into predefined
# categories
# ->

from transformers import pipeline

classifier = pipeline("zero-shot-classification")

text = "The Indian cricket team won the match by 5 wickets."

labels = ["Sports", "Politics", "Technology"]

res = classifier(text, candidate_labels = labels)

print(res)