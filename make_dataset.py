import pandas as pd

file = "./2024-01/position_names.csv"

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
            tokenDict['token'] = token
            tokenDict['tag'] = 'B-POS'
            tokens.append(tokenDict)
            token=""
            tokenDict={}
            t+=1
        elif t>0 and (d == " " or j==len(c)-1):
            token += d
            tokenDict['token'] = token
            tokenDict['tag'] = 'I-POS'
            tokens.append(tokenDict)
            token=""
            tokenDict={}
            t+=1
        else:
            token += d

f = open('./2024-01/position_names_tags.txt', 'w', encoding="utf-8")
for t in tokens:
    f.write(t['token'].lower() + " " + t['tag'] + "\n")
f.close()



# df.info()
# df.head()
# df.describe()

