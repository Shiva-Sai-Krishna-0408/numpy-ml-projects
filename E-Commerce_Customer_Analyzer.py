import numpy as np
import pandas as pd


data = {
    "Customer": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Category": ["Electronics", "Clothing", "Electronics", "Food", "Clothing",
                 "Food", "Electronics", "Clothing", "Electronics", "Food"],
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan",
              "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Spend": [12000, 4500, 8900, 2300, 6700,
              15000, 5200, 7800, 3100, 4900],
    "Orders": [8, 5, 12, 3, 7,
               10, 6, 9, 4, 6]
}

df = pd.DataFrame(data)
df["Spend_Per_Order"] = np.round(df["Spend"] / df["Orders"],2)
print(df["Spend_Per_Order"])
df["Total_Spend"] = df.groupby(["Customer"])["Spend"].transform("sum")
print(df["Total_Spend"])
top_75 = np.percentile(df["Total_Spend"],75)
top_25 = np.percentile(df["Total_Spend"],25)
df["Customer_Segment"] = df["Total_Spend"].apply(lambda x: "Premium" if x > top_75 else "Regular" if x < top_75 and x > top_25 else "Budget")
print(df["Customer_Segment"])
Highest_Category_Spend = df.groupby(["Category"])["Spend"].sum().reset_index()
Popular_Category = Highest_Category_Spend[Highest_Category_Spend["Spend"] == Highest_Category_Spend["Spend"].max()]
for _,row in Popular_Category.iterrows():
    print(f"Most Popular Category is : {row['Category']} with {row['Spend']}")
print()
Highest_Monthly_Spend = df.groupby(["Customer"])["Spend"].sum().reset_index()
Valueable_Customer = Highest_Monthly_Spend[Highest_Monthly_Spend["Spend"] == Highest_Monthly_Spend["Spend"].max()]
for _,row in Valueable_Customer.iterrows():
    print(f"Most Valuable Customer is : {row['Customer']} with {row['Spend']}")
df["MoM_Growth"] = np.round(df.groupby(["Customer"])["Spend"].pct_change()*100,2)
print()
print(df["MoM_Growth"])
print()
print(df)