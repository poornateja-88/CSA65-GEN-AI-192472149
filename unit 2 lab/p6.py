from openai import OpenAI

# Enter your OpenAI API key
client = OpenAI(api_key="YOUR_API_KEY")

# Get task from user
task = input("Enter the task: ")

# Zero-shot Prompt
zero_shot = f"""
Task:
{task}
"""

# One-shot Prompt
one_shot = f"""
Example:
Input: Write a short paragraph about Python.
Output: Python is a popular programming language known for its simplicity and readability. It is widely used in web development, data science, artificial intelligence, and automation.

Now perform this task:
{task}
"""

# Few-shot Prompt
few_shot = f"""
Example 1:
Input: Write a short paragraph about Python.
Output: Python is a popular programming language used for web development, AI, and data analysis.

Example 2:
Input: Write a short paragraph about Artificial Intelligence.
Output: Artificial Intelligence enables computers to perform tasks that normally require human intelligence, such as learning and decision-making.

Now perform this task:
{task}
"""

# Function to generate response
def generate(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text

# Generate outputs
print("\n--- Zero-shot Response ---")
print(generate(zero_shot))

print("\n--- One-shot Response ---")
print(generate(one_shot))

print("\n--- Few-shot Response ---")
print(generate(few_shot))