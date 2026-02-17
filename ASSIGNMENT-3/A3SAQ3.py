# Q: Write a Python program to generate a short story of approximately 50 words using a text generation model.

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

prompt = "Once upon a time in a small village,"

result = generator(prompt, max_new_tokens=50, temperature=0.7, repetition_penalty=1.2, num_return_sequences=1)

print("Generated Short Story:")
print(result[0]["generated_text"])
