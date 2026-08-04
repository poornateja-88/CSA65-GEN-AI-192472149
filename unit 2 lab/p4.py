from openai import OpenAI

# Enter your OpenAI API key
client = OpenAI(api_key="YOUR_API_KEY")

# Get the computational problem from the user
problem = input("Enter the computational problem: ")

# Create a structured prompt
prompt = f"""
Generate a Python program for the following problem.

Problem:
{problem}

Instructions:
1. Write clean and beginner-friendly Python code.
2. Add comments explaining each step.
3. Ensure the code is correct and executable.
4. Explain the output after the code.
"""

# Generate response
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

# Display generated code
print("\nGenerated Python Program:\n")
print(response.output_text)