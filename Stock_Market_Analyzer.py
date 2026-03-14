import numpy as np
import pandas as pd


data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
             "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"],
    "Stock": ["AAPL", "AAPL", "AAPL", "AAPL", "AAPL",
              "GOOGL", "GOOGL", "GOOGL", "GOOGL", "GOOGL"],
    "Price": [185.2, 187.5, 183.8, 189.2, 191.5,
              140.3, 142.8, 139.5, 144.2, 146.8],
    "Volume": [1200000, 1350000, 980000, 1420000, 1100000,
               890000, 920000, 850000, 960000, 1010000]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
print(df)
print()
df["Daily_Return"] = np.round(df.groupby(["Stock"])["Price"].pct_change()*100,2)
print(df["Daily_Return"])
print()
df["Rolling_Avg"] = np.round(df.groupby(["Stock"])["Price"].rolling(window=3).mean().reset_index(level=0,drop=True),2)
print(df["Rolling_Avg"])
print()
Volitility = np.round(df.groupby(["Stock"])["Daily_Return"].std().reset_index(),2)
print(Volitility)
print()
Best_Stock = df.groupby(["Stock"])["Daily_Return"].idxmax()
Best_Stock_Details = df.loc[Best_Stock][["Date","Stock","Daily_Return"]]
for _,row in Best_Stock_Details.iterrows():
    print(f"Best day for {row['Stock']} is {row['Date'].strftime('%Y-%m-%d')} with {row['Daily_Return']}% return")
print()
df["Signal"] = df["Daily_Return"].apply(lambda x: "Buy" if x > 1 else "Sell" if x < -1 else "Hold")
print(df["Signal"])