import pandas as pd

path="data/products.csv"
data = pd.read_csv(path)
print(data.head())
