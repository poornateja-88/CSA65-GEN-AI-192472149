from openai import OpenAI

# Enter your OpenAI API key
client = OpenAI(api_key="YOUR_API_KEY")

# Get task from user
task = input("Enter the text generation task: ")

# Different prompts
prompt1 = f"""
Write about:
{task}
"""

prompt2 = f"""
Write a clear and detailed paragraph about:
{task}

Use simple language.
"""

prompt3 = f"""
You are an expert writer.

Write a well-structured paragraph about:
{task}

Requirements:
1. Simple language
2. Around 100 words
3. Correct grammar
4. Proper conclusion
"""

# Function to generate response
def generate(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text

# Generate outputs
output1 = generate(prompt1)
output2 = generate(prompt2)
output3 = generate(prompt3)

# Display responses
print("\n----- Prompt 1 Response -----")
print(output1)

print("\n----- Prompt 2 Response -----")
print(output2)

print("\n----- Prompt 3 Response -----")
print(output3)

# Display evaluation
print("\nPrompt Evaluation")
print("----------------------------------------------")
print("Prompt 1 : Basic prompt, less detailed.")
print("Prompt 2 : Better clarity and relevance.")
print("Prompt 3 : Most complete, accurate, and well formatted.")

print("\nRefined Prompt")
print("----------------------------------------------")
print("""
You are an expert content writer.

Generate a well-structured paragraph on the given topic.
Requirements:
- Use simple English.
- Around 100 words.
- Ensure accuracy and relevance.
- Maintain correct grammar.
- End with a short conclusion.
""")