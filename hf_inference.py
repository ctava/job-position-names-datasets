import pickle
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline
#text = "software engineer loyally"
#text = "social media analyst scrolls on tiktok"
#text = "data scientist prepares a classifier"
text = "nurse draws blood for lab test"
token_classifier = pipeline(model="chris1tava/position_names", aggregation_strategy="simple")
sentence = "nurse draws blood for lab test"
tokens = token_classifier(sentence)
print(tokens)