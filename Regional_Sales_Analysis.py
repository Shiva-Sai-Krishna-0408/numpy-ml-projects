import pandas as pd
import numpy as np

data = {
    "Region":   ["North", "South", "East", "West", "North", 
                 "South", "East", "West", "North", "South"],
    "Quarter":  ["Q1", "Q1", "Q1", "Q1", "Q2", 
                 "Q2", "Q2", "Q2", "Q3", "Q3"],
    "Revenue":  [150000, 180000, 120000, 200000, 165000,
                 195000, 135000, 210000, 178000, 205000],
    "Target":   [140000, 170000, 130000, 190000, 160000,
                 185000, 140000, 205000, 175000, 200000],
    "Headcount":[45, 52, 38, 61, 47, 54, 40, 63, 49, 56]
}
df = pd.DataFrame(data)
df["Achievement"] = round((df["Revenue"] / df["Target"] * 100),2)
df["Status"] = df["Achievement"].apply(lambda x: "Exceeded" if x>100 else "Met" if x==100 else "Missed")
df["Revenue_Per_Head"] = np.round(df["Revenue"] / df["Headcount"],2)
print(df)
print()
# Creating Pivot Table
Avg_Achievements = pd.pivot_table(
    df,
    values="Achievement",
    index = "Region",
    columns = "Quarter",
    aggfunc="mean"
    )
print(Avg_Achievements)
print()
#Region with most Exceeded Targets
region_target = df[df["Status"]=="Exceeded"].groupby(["Region"])["Status"].count().reset_index()

region_target.columns = ["Region","Count"]
max_count = region_target["Count"].max()
top_regions = region_target[region_target["Count"] == max_count]
print()
print(f"Region that consistently exceeds: {",".join(list(top_regions["Region"].values))} with {max_count} times")
#print(region_target)