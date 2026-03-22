def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    print(get_grade(marks))
    