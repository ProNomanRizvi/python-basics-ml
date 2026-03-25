# Class: DataFrameAnalyzer
import pandas as pd
import numpy as np

class DataFrameAnalyzer:

    def __init__(self, filepath):
        try:
            df = pd.read_csv(filepath)
            if df.empty:
                raise ValueError("DataFrame is empty.")
            self._df = df
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filepath} not found.")
        
    def info(self):
        print(f"Shape: {self._df.shape}")
        print(f"Dtypes:\n{self._df.dtypes}")
        print(f"Null counts:\n{self._df.isnull().sum()}")

    def fill_nulls(self, strategy="mean"):
        numeric_col = self._df.select_dtypes(include=np.number).columns

        for col in numeric_col:
            if strategy == "mean":
                self._df[col] = self._df[col].fillna(self._df[col].mean())
            elif strategy == "median":
                self._df[col] = self._df[col].fillna(self._df[col].median())
            elif strategy == "zero":
                self._df[col] = self._df[col].fillna(0)
            else:
                raise ValueError(f"Unknown strategy: {strategy}")
    
    def filter_by(self, column, value):
        return self._df[self._df[column] == value]
    
    def top_n(self, column, n=5):
        return self._df.sort_values(by=column, ascending=False).head(n)
    
    def add_grade_column(self, marks_col="marks"):
        def get_grade(mark):
            if mark >= 80: return "A"
            elif mark >= 60: return "B"
            elif mark >= 40: return "C"
            else: return "Fail"

        self._df["grade"] = self._df[marks_col].apply(get_grade)

    def summary_by(self, column):
        return self._df.groupby(column).mean(numeric_only=True)
    
    def save(self, filepath):
        self._df.to_csv(filepath, index=False)  

def main():
    FILE_PATH = "phase3_numpy_pandas/data/students.csv"
    analyzer = DataFrameAnalyzer(FILE_PATH)
    analyzer.info()
    analyzer.fill_nulls(strategy="median")
    print(analyzer.filter_by("city", "Lahore"))
    print(analyzer.top_n("marks", n=3))
    analyzer.add_grade_column()
    print(analyzer.summary_by("grade"))
    analyzer.save("phase3_numpy_pandas/data/students_analyzed.csv")

if __name__ == "__main__":
    main()