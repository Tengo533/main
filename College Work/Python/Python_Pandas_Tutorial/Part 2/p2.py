import pandas as pd

# Standard python dictionary

people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

# Converting the dictionary into a DataFrame

df = pd.DataFrame(people)

# Outputting the "email" column from the DataFrame, can also be in the form df.email but using the . method could cause issues due to df having different attributes.

print(df['email'])

# Outputting the type of the "email" column

print(type(df['email']))

# A series is a 1 dimensional array, for example the "email" column within this DataFrame

# Outputting two columns at once

print(df[["last", "email"]])

# Output all the column names within the DataFrame

print(df.columns)

# Locates a row using integer location, in this example the first row within the DataFrame.
# Find multiple rows by doing df.iloc[[0, 1, etc]]

print(df.iloc[0])

# Locate the rows and sort by the columns we want to display.

print(df.iloc[[0, 1], 2])


# Locate the row by using the index label.
# Locate multiple rows by doing df.loc[[index1, index2, etc]]

print(df.loc[0])