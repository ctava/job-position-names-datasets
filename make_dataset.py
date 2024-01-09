import pandas as pd
import random

def find(token,array):
    result = False
    for i,v in enumerate(array):
        if v.lower().strip() == token.lower().strip():
            result = True
            return result
    return result

file = "./2024-01/position_names.csv"
predicate_adverbs = ['python','c#','typescript','golang']
predicate_verbs = ['writes','reads','speaks','presents','talks','tests','checks']
predicate_nouns = ['code','papers','notebooks','documents','presentations']
predicate_adjectives = ['.','a','an','and','does','in','not','the','to','yet']
predicates = []
predicates.extend(predicate_verbs)
predicates.extend(predicate_nouns)
predicates.extend(predicate_adverbs)
predicates.extend(predicate_adjectives)
dtype={'Name': 'string'}
df = pd.read_csv(file,dtype=dtype)
column = df['Name']
tokens = []
for i,c in enumerate(column):
    token=""
    tokenDict={}
    t=0
    for j,d in enumerate(c):
        if t==0 and (d == " " or j==len(c)-1):
            token += d
            token = token.strip()
            if find(token,predicates):
                #print(token.lower() + 'in')
                tokenDict['tag'] = 'O'
            else:
                #print(token + ' not in')
                tokenDict['tag'] = 'B-POS'
            tokenDict['token'] = token
            tokens.append(tokenDict)
            token=""
            tokenDict={}
            t+=1
        elif t>0 and (d == " " or j==len(c)-1):
            token += d
            token = token.strip()
            if find(token,predicates):
                tokenDict['tag'] = 'O'
            else:
                tokenDict['tag'] = 'I-POS'
            tokenDict['token'] = token
            tokens.append(tokenDict)
            token=""
            tokenDict={}
            t+=1
        else:
            token += d

tokenDict={}
num_of_records = 50000
for _ in range(num_of_records):
    tokenDict['tag'] = '0'
    pIndex = random.randint(1,len(predicates)-1)
    tokenDict['token'] = predicates[pIndex]
    tokens.append(tokenDict)
    tokenDict={}

random.shuffle(tokens)

f = open('./2024-01/position_names_tags.txt', 'w', encoding="utf-8")
for t in tokens:
    f.write(t['token'].lower() + " " + t['tag'] + "\n")
f.close()
