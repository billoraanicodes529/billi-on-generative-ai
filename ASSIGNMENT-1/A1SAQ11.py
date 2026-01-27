# Q11: Write a program that uses a translation LLM to convert English text into Marathi text.
# ->

from transformers import pipeline

translator = pipeline("translation", model = "Helsinki-NLP/opus-mt-en-mr")

text = input("Enter Text In English: ")

result = translator(text)

print("Translated Text (Marathi): ", result[0]["translation_text"])