# Q3: Write a program to extract an answer from a paragraph using a question answering LLM.
# ->

from transformers import pipeline

que_model = pipeline("question-answering")

con = '''The Sun is the center of our Solar System. It is a huge ball of hot gases. Earth revolves 
around the Sun in 365 days.'''
# con = input("Enter Context Prompt: ")

que = "How many days does Earth take to revolve around the Sun?"
# que = input("Enter Question Prompt: ")

res = que_model(question = que, context = con)

print("Answer: ", res["answer"] )