# 6] Write a Python program that uses Few-Shot prompting with an 
# instruction-tuned language model to classify the sentiment 
# of a given text review.

from transformers import pipeline

model = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",
)

prompt = """Classify the sentiment of the review as Positive or Negative.

Review: The movie was amazing and full of emotions.
Sentiment: Positive

Review: The service was very slow and disappointing.
Sentiment: Negative

Review: The product quality is excellent.
Sentiment:"""

result = model(prompt, max_new_tokens=3)

print(result[0]["generated_text"])
