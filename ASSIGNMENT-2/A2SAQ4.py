# Q4: Write a program to summarize a paragraph by removing repeated words.
# ->

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

text = input("Enter a paragraph: ")

tokens = tokenizer.tokenize(text.lower())

unique_words = []

for word in tokens: 
    if word not in unique_words:
        unique_words.append(word)

print("\nSummarized Paragraph (After Removing Repeated Words): ")
print(" ".join(unique_words))