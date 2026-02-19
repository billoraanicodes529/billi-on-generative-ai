# 1] Write a python program to extract and display Name and Contact Number 
# from a resume in Word format using Python.

# pip install python-docx
# pip install transformers
# pip install torch

from docx import Document
from transformers import pipeline
import re

llm = pipeline("text2text-generation", model="google/flan-t5-base")

doc = Document("resume1.docx")
text = "\n".join(p.text for p in doc.paragraphs)

phone = re.findall(r"\b\d{10}\b", text)
phone = phone[0] if phone else "Not Found"

prompt = f"Extract the full name from this resume: \n{text}"
name = llm(prompt, max_length=30, temperature=0.0)[0]["generated_text"]

print("Name:", name)
print("Contact Number:", phone)
