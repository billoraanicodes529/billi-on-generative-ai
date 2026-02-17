# Q11: Write a Python program using a Generative AI Transformer model to summarize a story and display the summary in bullet points.

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

story = """
Once upon a time in a small village, there lived a boy named Raju.
He loved to explore forests and spend time with animals.
One day, he found an injured bird and took it home.
Raju cared for the bird until it healed and could fly again.
The villagers appreciated his kindness, and Raju became known as a loving and helpful boy.
"""

summary = summarizer(story, max_length=80, min_length=40, do_sample=False)[0]["summary_text"]

sentences = summary.split(".")

print("Story Summary in Bullet Points:")

for s in sentences:
    if s.strip():
        print(".", s.strip())
