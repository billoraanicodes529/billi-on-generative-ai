# Q1: Write a Python program that prints a short summary by selecting the first two sentences 
#     of a paragraph
# -> 

text = '''Generative AI creates new content such as text and images. It learns patterns from data.
It is used in chatbots and image creation tools.'''

sentences = text.split(".")

summary = sentences[0] + "." + sentences[1] + "."

print("Summary: ", summary)

