# Q13: Write a Python program that reads multiple documents and generates a summary using the Transformers summarization pipeline.

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

files = ["doc1.txt", "doc2.txt", "doc3.txt"]

combined_text = ""

for file in files:
    with open(file, "r") as f:
        combined_text += f.read() + " "

summary = summarizer(combined_text, max_length=60, min_length=30)

print("Multi-Document Summary:")
print(summary[0]['summary_text'])
