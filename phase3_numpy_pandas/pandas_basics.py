import numpy as np
import pandas as pd

def load_and_inspect(filepath):
    print("=== LOAD AND INSPECT ===")
    df = pd.read_csv(filepath)
    print(df)
    print(f"\nShape     : {df.shape}")
    print(f"\nDtypes:\n{df.dtypes}")
    print(f"\nNull counts:\n{df.isnull().sum()}")
    print(f"\nDescribe:\n{df.describe()}")
    return df

def filter_data(df):
    print("\n=== FILTERING ===")

    # Students with marks above 70
    above_70 = df[df["marks"] > 70]
    print(f"Above 70:\n{above_70[['name', 'marks']]}")

    # Students from Lahore
    lahore = df[df["city"] == "Lahore"]
    print(f"\nFrom Lahore:\n{lahore[['name', 'city']]}")

    # High marks AND from Lahore
    combo = df[(df["marks"] > 70) & (df["city"] == "Lahore")]
    print(f"\nHigh marks + Lahore:\n{combo[['name', 'marks', 'city']]}")
    return df

def handle_missing(df):
    print("\n=== MISSING VALUES ===")
    print(f"Nulls before:\n{df.isnull().sum()}")

    # Fill missing marks with column mean
    mean_mark = df["marks"].mean()
    df["marks"] = df["marks"].fillna(round(mean_mark, 2))

    print(f"\nNulls after:\n{df.isnull().sum()}")
    print(f"Bilal's marks filled with mean: {mean_mark:.2f}")
    return df

def add_columns(df):
    print("\n=== ADDING COLUMNS ===")

    # Pass/Fail column
    df["status"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

    # Grade column
    def get_grade(mark):
        if mark >= 80: return "A"
        elif mark >= 60: return "B"
        elif mark >= 40: return "C"
        else: return "Fail"

    df["grade"] = df["marks"].apply(get_grade)
    print(df[["name", "marks", "status", "grade"]])
    return df

if __name__ == "__main__":
    FILE_PATH = "phase3_numpy_pandas/data"
    df = load_and_inspect(f"{FILE_PATH}/students.csv")
    df = filter_data(df)
    df = handle_missing(df) 
    df = add_columns(df)