from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompts = [
"""Generate a product description for a Smart Fitness Watch.""",

"""Example:
Product: Wireless Earbuds
Description: Crystal-clear sound with long battery life.

Now generate a product description for a Smart Fitness Watch.""",

"""Example 1:
Product: Bluetooth Speaker
Description: Portable speaker with powerful bass.

Example 2:
Product: Laptop
Description: Lightweight laptop with fast performance.

Now generate a product description for a Smart Fitness Watch."""
]

titles = ["Zero-shot", "One-shot", "Few-shot"]

for i in range(3):
    print("\n", titles[i])
    result = generator(prompts[i], max_length=100)
    print(result[0]["generated_text"])
