def average(marks):
    return sum(marks) / len(marks)

def highest_marks(marks):
    return max(marks)

def lowest_marks(marks):
    return min(marks)

# ----------
def get_marks():
    marks = []

    while len(marks) < 5:
        mark = int(input("Enter marks: "))

        if mark < 0 or mark > 100:
            print("Invalid marks")
            continue

        marks.append(mark)

    return marks

def main():
    marks = get_marks()
    print("\nStudent Marks System")
    print(f"Marks: {marks}")
    print(f"Average: {average(marks)}")
    print(f"Highest: {highest_marks(marks)}")
    print(f"Lowest: {lowest_marks(marks)}")

main()
