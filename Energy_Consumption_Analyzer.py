import numpy as np
import pandas as pd

data = {
    "City": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad",
             "Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad"],
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan",
              "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Renewable_Energy": [450, 320, 580, 410, 390,
                         480, 350, 610, 440, 420],
    "Non_Renewable_Energy": [850, 1200, 620, 780, 920,
                             820, 1150, 590, 750, 890],
    "Population": [20000000, 32000000, 13000000, 10000000, 10000000,
                   20000000, 32000000, 13000000, 10000000, 10000000]
}
df = pd.DataFrame(data)
df["Total_Energy"] = df["Renewable_Energy"] + df["Non_Renewable_Energy"]
print(df["Total_Energy"])
print()
df["Renewable_Ratio"] = np.round(df["Renewable_Energy"] / df["Total_Energy"],4)
print(df["Renewable_Ratio"])
print()
df["Energy_Per_Capita"] = np.round(df["Total_Energy"] / df["Population"],6)
print(df["Energy_Per_Capita"])
print()
df["Energy_Status"] = df["Renewable_Ratio"].apply(lambda x: "Green" if x > 0.4 else "Moderate" if x > 0.3 and x < 0.4 else "Critical")
print(df["Energy_Status"])
print()
Improved_Ratio = df.groupby(["City"])["Renewable_Ratio"].pct_change()
Best_Idx = Improved_Ratio.idxmax()
Best_City = df.loc[Best_Idx]
print(f"The most improved city: {Best_City['City']} with {Best_City['Renewable_Ratio']}")
Efficient_City = df[df["Energy_Per_Capita"] == df["Energy_Per_Capita"].min()]
print()
for _,rows in Efficient_City.iterrows():
    print(f"The most energy efficient city: {rows['City']}")