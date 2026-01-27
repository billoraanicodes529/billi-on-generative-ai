# Q9: Write a Python program using the sentence-transformer library to find the semantic simantic
#     similarity between the sentences given by the users. Display the similarity score.
# ->

from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("all-MiniLM-L6-v2")

str1 = input("Enter First Prompt: ")
str2 = input("Enter Second Prompt: ")

emb1 = model.encode(str1)
emb2 = model.encode(str2)

similarity = util.cos_sim(emb1, emb2)
print("Similarity Score: ", similarity.item())

# Enter First Prompt: Football is my favorite sports
# Enter Second Prompt: I love to play football
# Similarity Score:  0.7769744992256165