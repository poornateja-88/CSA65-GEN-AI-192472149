from openai import OpenAI

# Enter your OpenAI API key
client = OpenAI(api_key="YOUR_API_KEY")

# Database schema
schema = """
Table: Students

Columns:
student_id INT PRIMARY KEY
name VARCHAR(50)
department VARCHAR(50)
marks INT
"""

# Get requirement from user
requirement = input("Enter SQL requirement: ")

# Structured prompt
prompt = f"""
You are an SQL expert.

Database Schema:
{schema}

Requirement:
{requirement}

Instructions:
1. Generate a valid SQL query.
2. Use only the given table and columns.
3. Return the SQL query with a short explanation.
"""

# Generate response
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

# Display output
print("\nGenerated SQL Query:\n")
print(response.output_text)