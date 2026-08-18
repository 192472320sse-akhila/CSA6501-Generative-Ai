from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

article = """
Artificial Intelligence is transforming healthcare by improving diagnosis,
predicting diseases, assisting doctors, and enhancing patient care.
Hospitals use AI for medical imaging, drug discovery, and robotic surgery.
"""

summary = summarizer(article, max_length=50, min_length=30)

print(summary[0]["summary_text"])
