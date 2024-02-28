import pandas as pd

# Importing data from a CSV to a DataFrame
df = pd.read_csv("Python_Pandas_Tutorial\survey_results_public.csv")

# Displays the size of the DataFrame (Rows and Columns)

print(df.shape)

# Gives primary information about the DataFrame, including all the columns and what is contained within each, and its data type.

print(df.info())

# Changes the total amount of columns displayed when the DataFrame is outputted.
# option("option_name", option_setting)

pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

# Importing and displaying the schema for this DataFrame, gives info on what each column's question was.

schema_df = pd.read_csv("Python_Pandas_Tutorial\survey_results_schema.csv")
print(schema_df)