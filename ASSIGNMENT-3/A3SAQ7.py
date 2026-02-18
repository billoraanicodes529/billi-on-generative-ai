# Write a python program to demonstrate Chain-of-Thought Prompting 
# using the Microsoft Phi-3 mini instruct model to generate 
# step-by-step reasoning for a given problem.

# Chain-of-Thought Prompting Example

from transformers import pipeline

model = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
)

# Chain-of-Thought Prompt
prompt = """
Solve the following problem step by step.

Question: If a book costs 25 rupees and you buy 4 books, how much do you pay in total?

Let's think step by step.
"""

# Generate output
output = model(
    prompt,
    max_new_tokens=150,
    temperature=0.7,
    do_sample=True
)

print("Chain-of-Thought Output:\n")
print(output[0]["generated_text"])
