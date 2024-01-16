from collections import defaultdict
import pandas as pd
import random
from sentence import SentenceBuilder

file = "./2024-01/position_names.csv"
sentence = SentenceBuilder()
dtype={"Name": "string"}
df = pd.read_csv(file,dtype=dtype)
titles = df["Name"]
tokens = []
for i,t in enumerate(titles):
    e=0
    entities=[]
    entity=""
    token={}
    words=[]
    word=""
    for j,c in enumerate(t):
        if e==0 and (c == " " or j==len(t)-1):
            entity += c
            entity = entity.strip()
            entities.append(entity)
            entity=""
            e+=1
            if e==1:
                words.append(random.choice(sentence.get_adjectives()))
        elif e>0 and (c == " " or j==len(t)-1):
            entity += c
            entity = entity.strip()
            entities.append(entity)
            entity=""
            e+=1
            if e==2:
                words.append(random.choice(sentence.get_verbs()))
            elif e==3:
                words.append(random.choice(sentence.get_adverbs()))
            elif e==4:
                words.append(random.choice(sentence.get_nouns()))
            elif e==5:
                words.append(random.choice(sentence.get_conjunctions()))
            elif e==6:
                words.append(random.choice(sentence.get_prepositions()))
            elif e==7:
                words.append(random.choice(sentence.get_verbs()))
        else:
            entity += c
    token["entities"] = entities
    token["words"] = words
    tokens.append(token)
    token={}
    entities=[]
    words=[]

random.shuffle(tokens)

f = open("./2024-01/position_names_tags.txt", "w", encoding="utf-8")
entity_shortname = "POS"
for i,t in enumerate(tokens):
    ner_sentence=""
    ner_tag=""
    for j,e in enumerate(t["entities"]):
        ner_sentence = e + " "
        if j == 0:
            ner_tag = "B-"+entity_shortname + " "
        else:
            ner_tag = "I-"+entity_shortname + " "
        f.write(ner_sentence + ner_tag + "\n")
    ner_sentence=""
    ner_tag=""
    for k,w in enumerate(t["words"]):
        ner_sentence = w + " "
        ner_tag = "O" + " "
        f.write(ner_sentence + ner_tag + "\n")
f.close()