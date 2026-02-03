# Q5: Write a program that summarizes a long article into 3 lines.
# ->

from transformers import pipeline
summarizer = pipeline("summarization")

article = """
The Koenigsegg Agera One:1 is a limited-production hypercar built by Swedish manufacturer Koenigsegg, 
unveiled in 2014. It is named One:1 because of its unique one-to-one power-to-weight ratio, producing 
1,341 horsepower while weighing 1,341 kilograms, a benchmark that qualifies it as the world’s first 
“megacar.” Powered by a 5.0-liter twin-turbocharged V8 engine, the Agera One:1 delivers extreme 
performance, advanced aerodynamics, and lightweight carbon-fiber construction. Only six units were 
produced, making it one of the rarest and most exclusive hypercars ever made.
"""

summary = summarizer(article, max_length=90, min_length=60)

print("======3-Line Summary======")

print(summary[0]["summary_text"])