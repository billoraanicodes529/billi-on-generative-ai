# Q7: Write a Python program to perform abstractive text summarization using a pre-trained generative AI model. 
# ->

from transformers import pipeline

summarize = pipeline("summarization", model="facebook/bart-large-cnn")

text_to_summarize = """
The Koenigsegg Agera One:1 is a limited-production hypercar built by Swedish manufacturer Koenigsegg, unveiled in 2014, and 
named for its unique one-to-one power-to-weight ratio, producing 1,341 horsepower while weighing 1,341 kilograms, a benchmark 
that earned it the title of the world’s first “megacar.” Powered by a 5.0-liter twin-turbocharged V8 paired with a seven-speed 
dual-clutch transmission, the One:1 delivers extreme performance, advanced active aerodynamics, and a lightweight carbon-fiber 
and titanium construction. It was engineered with a theoretical top speed of around 440 km/h and showcased astonishing 
acceleration, including a record-setting 0–400–0 km/h run in just over 20 seconds. Designed to be road-legal yet heavily 
track-focused, and with only six units produced, the Agera One:1 stands as one of the rarest, most technologically advanced, 
and most exclusive hypercars ever made.
"""

summary = summarize(text_to_summarize, max_length=100, min_length=30, do_sample=False)

print("Original Text: \n", text_to_summarize)
print("\nAbstractive Summary: \n", summary[0]["summary_text"])