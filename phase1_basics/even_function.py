def is_even(num):
    return num % 2 == 0


num = int(input("Enter a number: "))

print(f"Is {num} even? {is_even(num)}")