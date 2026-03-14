import numpy as np 
import pandas as pd

data = {
    "Employee": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Department": ["HR", "Tech", "Tech", "HR", "Finance",
                   "HR", "Tech", "Tech", "HR", "Finance"],
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan",
              "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Sales": [45000, 82000, 78000, 41000, 63000,
              51000, 89000, 72000, 47000, 71000],
    "Target": [40000, 80000, 75000, 45000, 60000,
               45000, 85000, 80000, 50000, 65000]
}

df = pd.DataFrame(data)
#print(df)

df["Acheivement_%"] = np.round((df["Sales"] / df["Target"]) * 100,2)
print(df["Acheivement_%"])
print()
df["Performance"] = df["Acheivement_%"].apply(lambda x: "Exceeds" if x >= 105 else "Meets" if x > 95 and x < 105 else "Below")
print(df["Performance"])
print()
df["Cumulative_Sales"] = df.groupby(["Employee"])["Sales"].cumsum()
print(df["Cumulative_Sales"])
print()
print(df)
Avg_Per_Dep = df.groupby(["Department","Employee"])["Acheivement_%"].mean().reset_index()
#print(Avg_Per_Dep)
top_performer = Avg_Per_Dep.groupby(["Department"])["Acheivement_%"].idxmax()
print()
print(Avg_Per_Dep.loc[top_performer])
print()
Cons_Dep = (df["Performance"] == 'Exceeds').groupby(df["Department"]).all()
print(f"The department that consistently exceeds: {", ".join(list(Cons_Dep[Cons_Dep == True].index))}")