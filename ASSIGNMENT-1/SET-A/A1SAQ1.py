# Q1: Write a Python program using the transformers library to generate a short continuation to the input
# prompt "Hello, I am learning LLM".
# ->

from transformers import pipeline

model = pipeline("text-generation");

output = model("Hello, I am learning LLM", max_length=30);

print(output[0]["generated_text"]);
