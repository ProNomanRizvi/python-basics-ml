nums = [5, 2, 9, 1, 7]

max_num = nums[0]

for num in nums:
    if num > max_num: 
        max_num = num 

print(f"List: {nums}")
print(f"Max number: {max_num}")