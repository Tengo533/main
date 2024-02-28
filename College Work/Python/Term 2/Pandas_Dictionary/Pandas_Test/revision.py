import pandas as pd

df = pd.DataFrame({
"name":["William","Emma","Sofia","Markus","Edward"],
"region":["East","North","East","South","West"],
"sales":[50000,52000,90000,34000,42000],
"expenses":[42000,43000,50000,44000,38000]})

df["Profit"] = df["sales"] - df["expenses"]
print(df)
df = df.drop(columns=["Profit"])
print(df)