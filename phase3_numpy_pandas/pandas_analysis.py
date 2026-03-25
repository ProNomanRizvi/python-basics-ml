import numpy as np
import pandas as pd

def load_csv(file):
    df = pd.read_csv(file)
    return df

def works_on_stds_data(df, path):
    # total_stds
    print(f"Total Students: {len(df)}")

    print("\n\n=========================================\n\n")

    marks_avg = df['marks'].mean()    # Pandas handles nulls automatically
    print(f"Marks Average: {marks_avg:.2f}")

    print("\n\n=========================================\n\n")

    # Fill missing marks with the median (not mean this time)
    print("=== Filling Missing Marks with Median ===")
    df['marks'] = df['marks'].fillna(df['marks'].median())
    print(df['marks'])
    print("\n\n=========================================\n\n")
    # Print names of students who failed (marks < 40)
    print("=== Failed Students ===")
    failed_stds = df[df['marks'] < 40]
    print("Failed Student: ", failed_stds)
    print("\n\n=========================================\n\n")
    # Print the student with the highest marks
    top_student = df.loc[df['marks'].idxmax()]
    print(f"Highest Marks: {top_student['name']} with {top_student['marks']}")
    # Add a column "scholarship" → True if marks >= 85, else False
    print("=== Adding Scholarship Column ===")
    df["scholarship"] = df['marks'] >= 85
    print(df)
    print("\n\n=========================================\n\n")
    # Print count of students per city using value_counts()
    print("=== Count of Students per City ===")
    print(df['city'].value_counts())
    print("\n\n=========================================\n\n")
    # Sort the DataFrame by marks descending and print top 5
    print("=== Top 5 Students ===")
    print(df.sort_values(by='marks', ascending=False).head(5))
    print("\n\n=========================================\n\n")
    # Save final DataFrame to "data/students_final.csv"
    print("=== Saving Final DataFrame ===")
    df.to_csv(f"{path}/students_final.csv", index=False)
    print(f"Final DataFrame saved to {path}/students_final.csv")

# ==========================================
def main():
    FILE_PATH = "phase3_numpy_pandas/data/students.csv"
    df = load_csv(FILE_PATH)
    works_on_stds_data(df, "phase3_numpy_pandas/data")

if __name__ == "__main__":  
    main()