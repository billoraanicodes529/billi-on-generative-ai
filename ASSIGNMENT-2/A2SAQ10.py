# Q10: Write a Python program to read text from a file and generate an abstractive summary using a pre-trained transformer model.

from transformers import pipeline

summarizer = pipeline("summarization")

# Reading text file
text = open("sample.txt", "r").read()

summary = summarizer(text, max_length=50, min_length=20, do_sample=False)[0]['summary_text']

print("\nSummary:\n", summary)

# C:\PDBK\210-Gen-AI\ASSIGNMENT-2>python A2SAQ10.py                                                                       
# No model was supplied, defaulted to sshleifer/distilbart-cnn-12-6 and revision a4f8f3e (https://huggingface.co/sshleifer/distilbart-cnn-12-6).                                                                                                  
# Using a pipeline without specifying a model name and revision in production is not recommended.                         
# Device set to use cpu                                                                                                                                                                                                                           
# Summary:                                                                                                                  
# Generative Artificial Intelligence (GenAI) marks a profound shift in technology, moving beyond analysis and classification to the creation of novel content . Technology gained widespread public attention with the release of consumer-facing tools like ChatGPT and DALL
#                                                                                                       