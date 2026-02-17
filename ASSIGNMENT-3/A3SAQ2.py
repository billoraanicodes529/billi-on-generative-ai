# Q: Write a Python program to demonstrate text generation using the
# microsoft/Phi-3-mini-4k-instruct model from Transformers library.
# The program should generate a formal explanation of Generative AI.

from transformers import pipeline

model = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
)

prompt = "Write a formal explanation of Generative AI."

output = model(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)

print("Generated Explanation:")
print(output[0]["generated_text"])
