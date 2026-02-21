# 5] Write a python program to design a chatbot that displays 
# the current system date and time based on user queries.

from transformers import pipeline
from datetime import datetime

bot = pipeline("text2text-generation", model="google/flan-t5-base")

print("Gen AI Time & Date Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Goodbye")
        break

    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    if "time" in user_input.lower() and "date" not in user_input.lower():
        response_text = f"The current time is {time}."
    elif "date" in user_input.lower() and "time" not in user_input.lower():
        response_text = f"Today's date is {date}."
    else:
        response_text = f"The current date is {date} and the time is {time}."

    prompt = f"Say this politely: {response_text}"
    response = bot(prompt, max_new_tokens=30, do_sample=False)

    print("Bot:", response_text)