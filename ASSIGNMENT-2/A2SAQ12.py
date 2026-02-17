# Q12: Write a Python program to read a pdf file and generate a summary using a pre-trained transformer model.

# pip install PyPDF2 transformers

import PyPDF2
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# pdf_path = input("Enter name of pdf: ") # example.pdf
pdf_path = "example.pdf"

pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ""

for page in pdf_reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + " "

pdf_file.close()

chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

summaries = []

for chunk in chunks:
    summary_chunk = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
    summaries.append(summary_chunk[0]['summary_text'])

final_summary = " ".join(summaries)

print("\nGenerated Summary:")
print(final_summary)
