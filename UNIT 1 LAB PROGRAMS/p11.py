from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

text = "Machine learning is interesting."

tokens = tokenizer.tokenize(text)

print(tokens)