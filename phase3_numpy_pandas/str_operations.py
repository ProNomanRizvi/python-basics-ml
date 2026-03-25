import pandas as pd 
df = pd.read_csv("phase3_numpy_pandas/data/students.csv")

print("Original DataFrame: ")
print(df.head(), "\n\n")


# Pandas has built-in string methods via .str
print("String Operations: ")
df["name_upper"] = df["name"].str.upper()
df["city_lower"] = df["city"].str.lower()
df["name_len"]   = df["name"].str.len()

print("DataFrame with String Operations:")
print(df, "\n\n")


# Filter by string content
print("Students from Lahore: ")
lahore = df[df["city"].str.contains("Lahore")]
print(lahore, "\n\n")