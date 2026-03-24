import numpy as np


def numpy_operations():
    marks = np.array([78, 55, 92, 43, 88, 61, 74, 39, 95, 67])

    # 1. Print mean, median, std deviation
    mean = np.mean(marks)
    median = np.median(marks)
    std_deviation = np.std(marks)
    print(f"Mean: {mean:.2f}, Median: {median}, Std Deviation: {std_deviation:.2f}")
    
    # 2. Print highest and lowest mark
    max_marks = np.max(marks)
    min_marks = np.min(marks)
    print(f"Highest mark: {max_marks}, Lowest mark: {min_marks}")

    # 3. Print index of the highest mark
    highest_mark_index = np.argmax(marks)
    print(f"Index of highest mark: {highest_mark_index}")

    # 4. Filter and print all marks above 70
    marks_above_70 = marks[marks > 70]
    print(f"Marks above 70: {marks_above_70}")

    # 5. Normalize the marks to 0-1 range using:
    #    (value - min) / (max - min)
    normalize = (marks - min_marks) / (max_marks - min_marks)
    print(f"Normalized marks: {normalize}")
    # 6. Print how many students passed (marks >= 40)and failed (marks < 40)
    passed_students = np.sum(marks >= 40)
    failed_students = np.sum(marks < 40)
    print(f"Number of students passed: {passed_students}")
    print(f"Number of students failed: {failed_students}")
    # Replace all marks below 40 with exactly 40
    # (floor — no one scores below 40)
    marks[marks < 40] = 40
    print(f"Marks after replacing below 40 with 40: {marks}")

    # 8. Print the sorted array (ascending)
    sorted_marks = np.sort(marks)
    print(f"Sorted marks: {sorted_marks}")

if __name__ == "__main__":
    numpy_operations()