from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Write a professional email requesting leave due to illness."

result = generator(prompt, max_length=120)

print(result[0]["generated_text"])
