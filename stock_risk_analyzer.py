import pandas as pd
import numpy as np

df = pd.read_csv("amazon.csv")
print(df.shape)
print(df.isnull().sum())
print(df.dtypes)
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
