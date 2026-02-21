# 4] Python program to design a basic chatbot that responds to user greetings
# using a Generative AI model (FLAN-T5).

from transformers import pipeline

chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

print("Greeting Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Goodbye! Have a nice day")
        break
    
    prompt = f"Respond politely to this greeting: {user_input}"
    
    response = chatbot(
        prompt,
        max_length=50,
        do_sample=True
    )
    
    print("Bot:", response[0]["generated_text"])


# Greeting Chatbot (type 'exit' to stop)
# You: Hello!

# Bot: Hello!
# You: What is your name?

# Bot: I don't know.
# You: How are you?

# Bot: I'm fine.
# You: What is your educational qualification? 

# Bot: I'm a teacher.
# You: alright, thank you.

# Bot: Thank you.
# You: exit

# Bot: Goodbye! Have a nice day