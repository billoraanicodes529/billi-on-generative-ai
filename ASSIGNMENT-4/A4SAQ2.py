# Write a Python program to extract professional skills 
# from a .docx resume using a Generative AI transformer model.

# pip install python-docx
# pip install transformers
# pip install torch

from docx import Document
from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

file_path = "resume123.docx"  
document = Document(file_path)

resume_text = ""
for para in document.paragraphs:
    resume_text += para.text + " "

prompt = f"""
Extract only the professional skills from the following resume.
Return skills as a comma separated list.

Resume:
{resume_text}
"""

# Generate output
result = generator(
    prompt,
    max_length=150,
    do_sample=True,
    temperature=0.5
)

print("\n--- Extracted Skills (AI Generated) ---")
print(result[0]["generated_text"])
