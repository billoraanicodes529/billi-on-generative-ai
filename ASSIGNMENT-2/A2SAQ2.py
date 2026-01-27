# Q2: Write a program to count the number of sentences in a paragraph and print a short summary 
#     containing only the first sentence.
# ->

text = input("Enter a paragraph: \n")
# Generative AI creates new content such as text and images. It learns patterns from data. It is used in chatbots and image creation tools.

sentences = [s for s in text.split(".") if s.strip()]

summary = sentences[0] + "."

print("Number Of Sentences: ", len(sentences))
print("Summary: ", summary)