# Q10: Write a program that uses a translation LLM to convert English text into Hindi text.
# ->

from transformers import pipeline

translator = pipeline("translation", model = "Helsinki-NLP/opus-mt-en-hi")

text = input("Enter Text In English: ")

result = translator(text)

print("Translated Text (Hindi): ", result[0]["translation_text"])