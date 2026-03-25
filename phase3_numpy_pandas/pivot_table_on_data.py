import pandas as pd

df = pd.read_csv("phase3_numpy_pandas/data/students.csv")
# Pivot Table — Reshaping Data
# Pivot tables are used to reshape data, similar to Excel pivot tables. They allow you to summarize data by grouping and aggregating.

# Create a pivot table to find the maximum marks by city
print("Original DataFrame: ")
print(df, "\n\n")

print("Pivot Table (Max Marks by City): ")
pivot = df.pivot_table(values="marks", index="city", aggfunc="max")
print(pivot)
