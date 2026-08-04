import google.generativeai as genai

# Configure your API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Get user prompt
prompt = input("Enter your prompt: ")

# Generate response
response = model.generate_content(prompt)

# Display output
print("\nGenerated Response:\n")
print(response.text)