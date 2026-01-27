# Q2:Write a Python program to load a pre-trained Large Language Model (LLM) using the transformers 
# library to generate a simple text continuation for a given prompt
# ->

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter a prompt: ")

result = generator(prompt, max_length=40, num_return_sequences=1)

print("Generated Output.")

print(result[0]["generated_text"])