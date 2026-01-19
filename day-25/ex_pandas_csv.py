import pandas as pd

df = pd.read_csv("day-25/data.csv")

print(df.head()) # reads only first 5 rows

print(df.tail()) #reads only last 5 of rows

#print(df["title"])

#4 Count the number of rows and columns
#Filter the titles which contain python
#Filter the titles which contain JavaScript
#Explore the data and make sense of it

rows, col = df.shape
print(f"Rows: {rows}, Columns: {col}")

python_titles = df[df["title"].str.contains("python", case=False, na=False)]
print(python_titles["title"])

print('\n', '#' * 20, '\n')

js_titles = df[df["title"].str.contains("JavaScript",case=False, na=False)]
print(js_titles["title"])