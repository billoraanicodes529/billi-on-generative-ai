# Q12: Write a Python program using the BERT-based-fill-mask model to predict missing words in a 
#      sentence. Accept a sentence from the user and display the predicted words along with their
#      probability scores.

from transformers import pipeline

fill_mask = pipeline("fill-mask", model = "bert-base-uncased")

text = "Artificial Intelligence is an emerging [MASK]."

output = fill_mask(text)

print("BERT Fill-Mask Predictions: \n")

for pred in output:
    print(pred["token_str"], " → ", pred["score"])