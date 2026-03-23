def calculate_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

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

def calculate_average(nums):
    total = calculate_sum(nums)
    return total / len(nums)

# --------

def get_data():
    data = []

    while len(data) < 5:
        num = int(input("Enter a number: "))

        if 0 <= num <= 100:
            data.append(num)
        else:
            print("Invalid input")
            continue

    return data

def main():
    data = get_data()
    print("\nMini Data Analysis System")
    print(f"List: {data}")
    print(f"Sum: {calculate_sum(data)}")
    print(f"Max: {find_max(data)}")
    print(f"Min: {find_min(data)}")
    print(f"Average: {calculate_average(data)}")

main()