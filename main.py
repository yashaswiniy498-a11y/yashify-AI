from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="t5-small"
    )

text = """
Python is a popular programming language used for web development,
data science, artificial intelligence, and automation.
"""

summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

print(summary)