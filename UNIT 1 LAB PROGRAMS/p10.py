print("Program started")

from transformers import pipeline

print("Loading model...")

sentiment = pipeline("sentiment-analysis")

print("Model loaded")

text = "I love learning Artificial Intelligence."

result = sentiment(text)

print(result)