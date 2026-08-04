import requests

# Enter your Hugging Face API Token
API_TOKEN = "YOUR_HUGGING_FACE_API_TOKEN"

# API URL for the model
API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Get user prompt
prompt = input("Enter your prompt: ")

# Send request
response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt}
)

# Display response
result = response.json()

print("\nGenerated Text:\n")

if isinstance(result, list):
    print(result[0]["generated_text"])
else:
    print(result)