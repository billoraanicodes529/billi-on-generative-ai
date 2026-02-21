# 6) Write a Python program to build a Math Chatbot using the Transformers library.

from transformers import pipeline
import re

bot = pipeline("text2text-generation", model="google/flan-t5-small")

print("Math Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye")
        break

    numbers = list(map(int, re.findall(r'\d+', user_input)))

    if len(numbers) < 2:
        print("Bot: Please ask like '10 plus 5'")
        continue

    if "plus" in user_input:
        result = numbers[0] + numbers[1]

    elif "minus" in user_input:
        result = numbers[0] - numbers[1]

    elif "multiply" in user_input or "multiplied" in user_input:
        result = numbers[0] * numbers[1]

    elif "divide" in user_input:
        result = numbers[0] / numbers[1]

    else:
        print("Bot: Operation not supported.")
        continue

    prompt = f"Rewrite nicely: The answer is {result}."
    response = bot(prompt, max_new_tokens=20, do_sample=False)
    output = response[0]["generated_text"]

    if output == "":
        output = f"The answer is {result}."

    print("Bot:", output)