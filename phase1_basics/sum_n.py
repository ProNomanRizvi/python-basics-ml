# Sum of Numbers 1 to n

num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number")
else:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(f"The sum of numbers from 1 to {num} is {sum}")
    