# Q: Write a Python program to identify the main topic of a given paragraph using a text generation model.

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

paragraph = """
Online education platforms have made learning more accessible.
Students can attend lectures from anywhere, learn at their own pace, 
and access digital study materials at low cost.
"""

prompt = (
    "Identify the main topic of the paragraph in one short phrase:\n"
    f"{paragraph}\nTopic:"
)

output = generator(prompt, max_new_tokens=8, temperature=0.2, repetition_penalty=1.5)

print("Paragraph:\n", paragraph)
print("\nPredicted Topic:\n", output[0]["generated_text"])
