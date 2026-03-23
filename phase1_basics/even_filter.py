nums = [1, 2, 3, 4, 5, 6]

even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

print(f"List: {nums}")
print(f"Even numbers: {even_nums}")