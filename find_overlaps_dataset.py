import pandas as pd
import traceback
try:
    np = open("./nouns.csv", mode='r', encoding=None, newline=None)
    n = np.read()
    ns = n.split()
    print(len(ns))
    pos = open("./2024-01/position_names.csv", mode='r', encoding=None, newline=None)
    o = open("./overlaps-nouns.csv", mode='w', encoding=None, newline=None)
    for i,p in enumerate(pos):
        words = p.split()
        for w in words:
            if w in ns:
                print(f"found {w}")
                o.write(w+"\n")
except Exception as e:
    print(e)
    print(traceback.format_exc())


