'''
Class: StudentAnalyzer

__init__(self, marks_array)
- stores marks as numpy array
- validates: must be numpy array, no empty

Methods:
- summary() → print mean, median, std, min, max
- top_n(n) → return top N marks (sorted descending)
- normalize() → return normalized array (0-1), do not modify original
- grade_distribution() → return dict:
    {"A": count, "B": count, "C": count, "Fail": count}
    A: >=80, B: >=60, C: >=40, Fail: <40
- is_above_average(mark) → return True/False
'''
import numpy as np

class StudentAnalyzer:

    def __init__(self, marks_array):
        if not isinstance(marks_array, np.ndarray):
            raise ValueError("Marks must be a numpy array.")
        if marks_array.size == 0:
            raise ValueError("Marks array cannot be empty.")
        self.marks_array = marks_array      # store only after validation passes

    def summary(self):
        print(f"Mean : {np.mean(self.marks_array):.2f}")
        print(f"Median : {np.median(self.marks_array):.2f}")
        print(f"Standard Deviation : {np.std(self.marks_array):.2f}")
        print(f"Minimum Value : {np.min(self.marks_array):.2f}")
        print(f"Maximum Value : {np.max(self.marks_array):.2f}")
    
    def top_n(self, n):
        top_students = np.sort(self.marks_array)[::-1][:n]
        return top_students
    
    def normalize(self):
        return (self.marks_array - np.min(self.marks_array)) / \
            (np.max(self.marks_array) - np.min(self.marks_array))
    
    def grade_distribution(self):
        # A: >=80, B: >=60, C: >=40, Fail: <40

        above_80 = np.sum(self.marks_array >= 80)
        above_60 = np.sum((self.marks_array >= 60) & (self.marks_array < 80))
        above_40 = np.sum((self.marks_array >= 40) & (self.marks_array < 60))
        fail = np.sum(self.marks_array < 40)

        grade_dict = {
            "A": above_80,
            "B": above_60,
            "C": above_40,
            "Fail": fail
        }

        return grade_dict
    
    def is_above_average(self, mark):
        return mark > np.mean(self.marks_array)



def main():
    marks = np.array([50, 65, 25, 74, 96, 41])
    student = StudentAnalyzer(marks)
    print("Marks: ", student.marks_array)
    student.summary()
    print("Top Marks: ", student.top_n(3))
    print("Normalized Marks: ", student.normalize())
    print("Grade Distribution: ", student.grade_distribution())
    print("Is Above Average: ", student.is_above_average(70))


if __name__ == "__main__":
    main()
