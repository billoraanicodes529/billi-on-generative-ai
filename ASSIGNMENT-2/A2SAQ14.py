# Q14: Write a Python program to assess the performance of a Generative AI summarization model using ROUGE scores.

# pip install rouge-score

from rouge_score import rouge_scorer

reference_summary = "Machine learning algorithms help analyze large datasets to make predictions and improve decision-making in various industries."
generated_summary = "Machine learning is used to analyze data and enhance decision-making across industries."

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
# Stemming reduces words to their root form (e.g., "analyzing" → "analyze")

scores = scorer.score(reference_summary, generated_summary)

print("----ROUGE Evaluation:----\n")
for key, value in scores.items():
    print(f"{key.upper()}: Precision={value.precision:.2f}, Recall={value.recall:.2f}, F1={value.fmeasure:.2f}")
