import pandas as pd
import traceback
try:
    df = pd.read_csv("./2024-01/position_names.csv")
    df.head()
    df = df.sort_values(by='Name')
    df.to_csv("./2024-01/position_names_new2.csv",index=False)
except Exception as e:
    print(e)
    print(traceback.format_exc())


