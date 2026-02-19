# Question:
# Write a Python program to perform resume screening using Generative AI by reading .docx resumes 
# from a folder, matching a user-entered qualification, extracting the candidate name using a 
# transformer model, and extracting the phone number using regular expressions.

import os
import re
from docx import Document
from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

qualification = input("Enter qualification: ")
folder = "resumes"
found = False

for file in os.listdir(folder):
    if file.endswith(".docx") and not file.startswith("~$"):
        file_path = os.path.join(folder, file)
        doc = Document(file_path)

        text = "\n".join([p.text for p in doc.paragraphs])

        if qualification.lower() in text.lower():

            prompt = f"""
            Extract only the candidate's full name from the resume below.
            Return only the name. Do not explain.

            Resume:
            {text}
            """

            result = generator(
                prompt,
                max_new_tokens=30,
                do_sample=False
            )

            name = result[0]["generated_text"].strip()

            phone = re.findall(r"\b\d{10}\b", text)
            phone = phone[0] if phone else "Not Found"

            print("\nCandidate Found")
            print("Name:", name)
            print("Phone:", phone)

            found = True

if not found:
    print("\nNo Candidate Found")
