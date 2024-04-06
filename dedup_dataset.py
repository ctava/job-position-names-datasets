import pandas as pd
import traceback
try:
    f = open("./2024-01/position_names_new2.csv", mode='r', encoding=None, newline=None)
    nf = open("./2024-01/position_names_new2_dedup.csv", mode='w', encoding=None, newline=None)
    records=[]
    for i,r in enumerate(f):
        print(i,r)
        if r not in records:
            records.append(r)
            nf.write(r)
    f.close()
    nf.close()
    # df = pd.read_csv("./2024-01/position_names_sorted_new.csv")
    # df.head()
    # records=[]
    # i=0
    # for r in df.iterrows():
    #     print(r[0])
    #     records.append(r['Name'])
    #     i+=1
    #     if 
    #df.to_csv("./2024-01/position_names_sorted_new_new.csv",index=False)
except Exception as e:
    print(e)
    print(traceback.format_exc())


