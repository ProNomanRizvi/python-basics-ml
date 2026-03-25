import pandas as pd

# Sample data
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "city": ["New York", "Los Angeles", "New York", "Chicago", "Los Angeles"],
    "grade": ["A", "B", "A", "C", "B"],
    "marks": [85, 78, 92, 65, 80]
}

df = pd.DataFrame(data)

# Average marks by city and grade
pivot = df.pivot_table(
    values="marks",
    index="city",
    columns="grade",
    aggfunc="mean"
)
print(pivot)
print("\n\n")
# Fill missing values with 0
print("Pivot table with missing values filled: ")
pivot_filled = pivot.fillna(0)
print(pivot_filled)