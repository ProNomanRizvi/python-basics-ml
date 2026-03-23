def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

def find_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

# ----------

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
    print(f"Max: {find_max(nums)}")
    print(f"Min: {find_min(nums)}")

main()  