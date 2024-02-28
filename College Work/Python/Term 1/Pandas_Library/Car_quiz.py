import pandas as pd

df = pd.read_csv(r"C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Pandas_Library\Automobile_data - Automobile_data.csv")
highest_price = df.loc[df["price"].max()]
print(highest_price)

