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