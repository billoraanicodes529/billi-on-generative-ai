# Q6: Write a program to accept input from user and correct the grammer by using LLM
# ->

from transformers import pipeline

grammarCorrector = pipeline("text2text-generation", model="grammarly/coedit-large")

sentence = input("Enter a sentence to correct grammar: ")

corrected = grammarCorrector(sentence)[0]["generated_text"]

print(f"\nOriginal Sentence: {sentence}")
print(f"\nCorrected Sentence: {corrected}")
