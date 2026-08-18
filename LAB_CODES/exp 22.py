from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Write a 200-word blog on Applications of Artificial Intelligence in Healthcare."

result = generator(prompt, max_length=300)

print(result[0]["generated_text"])
