import pandas as pd
data = {
  'Name': ['Madhav', 'Vishakha', 'Lalita', 'Rishabh'],
  'Age': [16,17,18,19],
  'Salary': [90000, 70000, 50000, 30000]
}

df = pd.DataFrame(data)
print(df)
df.shape # returns a tuple containing the shape of the DataFrame - rows & columns

print("\n")
print(df.head(2))   # First two rows (default is first 5)

print("\n")
print(df.tail(2))   # Last two rows  (default is last 5)

print("\n")
print("Number of Rows & Columns are :",df.shape) # returns a tuple containing the shape of the DataFrame - rows & columns

print("\n")
print(df.columns)  # list of column names in a dataframe

print("\n")
df.rename(columns={'Salary': 'Monthly_Salary'}, inplace=True) # rename column name/s
print(df)