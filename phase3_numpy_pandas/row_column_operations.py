import pandas as pd
# Sample DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "marks": [85, 90, 78],
    "city": ["New York", "Los Angeles", "Chicago"],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df, "\n")

print("Applying function to a column):")
# Apply to one column
print("Add Marks Bonus (5 points):")
df["marks_bonus"] = df["marks"].apply(lambda x: x + 5)
print(df, "\n")
# Apply to entire row (axis=1)
print("Create Summary Column:")
df["summary"] = df.apply(
    lambda row: f"{row['name']} from {row['city']}", axis=1 )

print(df)