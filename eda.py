import pandas as pd

df = pd.read_csv("./2024-01/position_names.csv")
print(df.head(5))
print(f"There are {df.shape[0]} rows and {df.shape[1]} columns.")  # f-string