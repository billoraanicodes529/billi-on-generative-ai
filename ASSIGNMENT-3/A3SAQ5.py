# Q: Write a Python program using the Transformers library to implement
# Few-Shot Learning for simple arithmetic question answering.

from transformers import pipeline

model = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
)

prompt = (
    "Q: What is 2 + 3?\n"
    "A: 5\n"
    "Q: What is 4 + 6?\n"
    "A: 10\n"
    "Q: What is 7 + 8?\n"
    "A:"
)

result = model(prompt, max_new_tokens=20)

print("Few-Shot Arithmetic Question:")
print("\nPredicted Answer:", result[0]["generated_text"].strip())
