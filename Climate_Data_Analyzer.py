import numpy as np
import pandas as pd

data = {
    "City": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata",
             "Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata"],
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan",
              "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Temperature": [18.5, 28.2, 26.8, 22.1, 19.3,
                    21.2, 29.8, 28.1, 23.4, 22.7],
    "Rainfall":    [12.3, 45.6, 34.2, 28.9, 67.8,
                    8.9,  38.4, 29.7, 22.1, 54.3],
    "AQI":         [285, 142, 98, 67, 198,
                    310, 156, 102, 72, 187]
}

df = pd.DataFrame(data)
col = df["Temperature"]
df["Temp_Normalized"] = np.round((col - col.min()) / (col.max() - col.min()),2)
print(df["Temp_Normalized"])
print()

aqi = df["AQI"]
df["AQI_Zscore"] = np.round(((aqi - aqi.mean()) / aqi.std()),2)
print(df["AQI_Zscore"])
print()

City_Avg = df.groupby(["City"])["AQI"].mean()
print(City_Avg)
print()
print(f"City with highest avg AQI: {City_Avg.idxmax()} with {City_Avg.max()}")
print()

Month_Avg = np.round(df.groupby(["Month"])["Rainfall"].mean(),2)
print(Month_Avg)
print()
print(f"Month with highest avg Rainfall: {Month_Avg.idxmax()} with {Month_Avg.max()}")
print()

df["Climate_Risk"] = df.apply(lambda row: "High" if row['AQI'] > 200 and row['Rainfall'] < 30 else "Medium" if row['AQI'] > 100 and row['AQI'] < 200 else "Low",axis = 1)
print(df)

