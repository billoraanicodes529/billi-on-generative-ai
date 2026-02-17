# Q9: Write a Program to Summarize Chat Conversations Using LLM.

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

print("Enter chat conversation (Press ENTER twice to finish):")

chat_lines = []

while True:
    line = input()
    if not line:
        break
    chat_lines.append(line)

chat_text = "".join(chat_lines)  # better than newline for BART

result = summarizer(chat_text, max_length=80, min_length=40, do_sample=False)[0]["summary_text"]

print("\nSummary:")
print(result)

# Arya: Hi, I need help with my shopping Bushra: Sure, can you tell me what issue you are facing? Arya: I dont know the areas from where to shop Bushra: Have you tried searching them Arya: Yes, but confused Bushra: Okay, I will come with you tomorrow Arya: Sure i will wait for you Bushra: I will make a list of places for tomorrow. Arya: Thank you!

# C:\PDBK\210-Gen-AI\ASSIGNMENT-2>python A2SAQ9.py                                                                          
# Device set to use cpu                                                                                                     
# Enter chat conversation (Press ENTER twice to finish):                                                                    
# Arya: Hi, I need help with my shopping Bushra: Sure, can you tell me what issue you are facing? Arya: I dont know the areas from where to shop Bushra: Have you tried searching them Arya: Yes, but confused Bushra: Okay, I will come with you tomorrow Arya: Sure i will wait for you Bushra: I will make a list of places for tomorrow. Arya: Thank you!                                                                                                                                                                                                                                                                       
# Summary:                                                                                                                  
# Arya asks Bushra to help her with her shopping. Bushra says she will make a list of places for tomorrow. Arya thanks her for her help. She is confused as to where to shop.                                                                             