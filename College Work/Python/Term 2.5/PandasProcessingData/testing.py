import pandas as pd
import matplotlib as plt


def richest_person():
    df = pd.read_csv("Term 2.5\PandasProcessingData\Billionaires Statistics Dataset.csv")
    df_rp = df.loc[df["finalWorth"] == df["finalWorth"].max()]
    name = df_rp["personName"].to_string(index=False)
    worth = df_rp["finalWorth"].to_string(index=False)
    print(f"The richest person in the world is {name} with a final worth of ${worth}!")

richest_person()