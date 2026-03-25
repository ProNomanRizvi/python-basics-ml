# Merge — Combining Two DataFrames
# Merge is SQL JOIN for Pandas. You will use this constantly when combining datasets.

import pandas as pd

df1 = pd.DataFrame({
    "name": ["Noman", "Ali", "Sara"],
    "marks": [88, 55, 92]
})

df2 = pd.DataFrame({
    "name": ["Noman", "Ali", "Ahmed"],
    "city": ["Lahore", "Karachi", "Islamabad"]
})

# Inner join — only matching rows
inner = pd.merge(df1, df2, on="name", how="inner")
print("Inner Join: ")
print(inner)
print("\n\n")

# Left join — all rows from df1
left = pd.merge(df1, df2, on="name", how="left")
print("Left Join: ")
print(left)
print("\n\n")

# Outer join — all rows from both
outer = pd.merge(df1, df2, on="name", how="outer")
print("Outer Join: ")
print(outer)