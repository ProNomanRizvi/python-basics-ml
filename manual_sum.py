def calculate_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

# -----
def main():
    nums = []
    while len(nums) < 5:
        num = int(input("Enter a number: "))
        if 0 <= num <= 100:
            nums.append(num)
        else:
            print("Invalid input")
            continue
    print(f"List: {nums}")
    print(f"Sum: {calculate_sum(nums)}")

main()