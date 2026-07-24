from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

s1 = "The cat is sleeping."
s2 = "A cat is taking a nap."

i1 = tokenizer(s1, return_tensors="pt")
i2 = tokenizer(s2, return_tensors="pt")

o1 = model(**i1).last_hidden_state.mean(dim=1)
o2 = model(**i2).last_hidden_state.mean(dim=1)

similarity = torch.nn.functional.cosine_similarity(o1, o2)

print("Cosine Similarity:", similarity.item())