age = int(input("Enter Age: "))
salary = int(input("Enter Salary: "))

if age <= 0 or salary < 0:
    print("Invalid Input")
elif age > 25 and salary > 50000:
    print("Eligible: Meets both age and salary criteria")
else:
    print("Not Eligible: Does not meet required conditions")