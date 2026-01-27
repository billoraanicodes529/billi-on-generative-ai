# Q3: Write a Python program to remove stopwords and print only meaningful words as a simple summary.
# ->

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = input("Enter Sentence:\n")

tokens = word_tokenize(text.lower())

stop_words = set(stopwords.words("english"))

meaningful_words = [
    word for word in tokens
    if word.isalpha() and word not in stop_words
]

print("\nMeaningful Words:")
print(" ".join(meaningful_words))

# Generative AI is a type of Artificial Intelligence that creates useful content.
