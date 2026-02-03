# Q8: Write a Python program to summarize story text
# ->

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

print("Enter a Story to Summarize: ")

story_text = input()

summary = summarizer(story_text, max_length=60, min_length=15)

print("\n---Original Story---")

print(story_text)

print("\n---Summary---")

print(summary[0]["summary_text"])

# The Koenigsegg Agera One:1 is a limited-production hypercar built by Swedish manufacturer Koenigsegg, unveiled in 2014. It is named One:1 because of its unique one-to-one power-to-weight ratio, producing 1,341 horsepower while weighing 1,341 kilograms, a benchmark that qualifies it as the world’s first “megacar.” Powered by a 5.0-liter twin-turbocharged V8 engine, the Agera One:1 delivers extreme performance, advanced aerodynamics, and lightweight carbon-fiber construction. Only six units were produced, making it one of the rarest and most exclusive hypercars ever made.