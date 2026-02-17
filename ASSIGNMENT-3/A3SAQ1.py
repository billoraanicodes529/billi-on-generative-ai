# Q1: Write a Python program to generate a one-sentence greeting message 
# using a pretrained Large Language Model (LLM) from transformers library.
# The program should use the text2text-generation pipeline and display
# the generated greeting as output. (use model google/flan-t5-large)

from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

prompt = "Write a one-sentence birthday greeting."

result = generator(prompt, max_length=30)

print("Greeting Message:")
print(result[0]["generated_text"])
