# Q3: Write a Python program to remove stopwords and print only meaningful words as a simple summary.
# ->

import torch
from transformers import BertTokenizer
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

text = input("Enter Sentence:\n")

tokens = tokenizer.tokenize(text.lower())

stop_words = set(stopwords.words("english"))

meaningful_words = [ word for word in tokens if word not in stop_words ]

print("\nMeaningful Words:")
print(" ".join(meaningful_words))

# Generative AI is a type of Artificial Intelligence that creates useful content.
