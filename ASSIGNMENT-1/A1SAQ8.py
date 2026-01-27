# Q8: Write a program that uses an LLM to correct the spelling of a sentence provided by the user.
# ->
from transformers import pipeline

corrector = pipeline("text2text-generation", model = "vennify/t5-base-grammar-correction")

sentence = input("Enter a sentence with spelling mistakes: ")

corrected = corrector("Correct: " + sentence)[0]["generated_text"]

print("Original Sentence: ", sentence)
print("Corrected Sentence: ", corrected)