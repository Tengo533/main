import pandas as pd

# Importing data from a CSV to a DataFrame

df = pd.read_csv("Python_Pandas_Tutorial\survey_results_public.csv")#

# Displaying the first 10 rows of the DataFrame

print(df.head(10))

# Displaying the last 10 rows of the DataFrame

print(df.tail(10))