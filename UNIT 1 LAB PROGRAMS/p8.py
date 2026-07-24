from transformers import BertTokenizer

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Input sentence
text = "Machine learning is interesting."

# Tokenize the sentence
tokens = tokenizer.tokenize(text)

# Display tokens
print("Tokens:")
print(tokens)