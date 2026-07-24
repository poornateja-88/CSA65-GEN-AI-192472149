from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Education is important because"

result = generator(prompt, max_length=50)

print(result[0]["generated_text"])