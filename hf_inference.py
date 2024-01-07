import pickle
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline
#text = "A software engineer walked into a library and then took a full stack engineer for coffee."
#text="software engineer"
text="cto"
model = AutoModelForTokenClassification.from_pretrained('./jpn202401')
tokenizer = AutoTokenizer.from_pretrained(
   './jpn202401', model_max_length=512)
nlp = pipeline("ner", model=model, tokenizer=tokenizer,
               aggregation_strategy="average")
print(nlp(text))