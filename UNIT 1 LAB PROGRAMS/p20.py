from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompts = [
    "Python is",
    "Artificial Intelligence",
    "The future of technology"
]

for p in prompts:
    result = generator(p, max_length=30)
    print("\nPrompt:", p)
    print(result[0]["generated_text"])