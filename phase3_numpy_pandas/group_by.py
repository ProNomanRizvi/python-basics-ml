import pandas as pd

df = pd.read_csv("phase3_numpy_pandas/data/students.csv")

# Average marks per city
print("Average marks per city: ")
print(df.groupby("city")["marks"].mean())
print("\n\n")
# Multiple aggregations at once
print("Multiple aggregations at once: ")
print(df.groupby("city")["marks"].agg(["mean", "min", "max", "count"]))
print("\n\n")
# Group by multiple columns
print("Average marks per city and grade: ")
print(df.groupby(["city", "grade"])["marks"].mean())
print("\n\n")
# =====================
# Built-in aggregations

print("Built-in aggregations: ")

print(df.groupby("city").agg({
    "marks": ["mean", "max", "min"],
    "age":   ["mean", "count"]
}))
print("\n")
# Custom aggregation function
print("Range of marks per city: ")
print(df.groupby("city")["marks"].agg(lambda x: x.max() - x.min()))
# → range of marks per city