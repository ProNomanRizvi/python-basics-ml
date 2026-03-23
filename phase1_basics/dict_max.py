# Find Max Value

def find_max(data):
    values = list(data.values())
    max_value = values[0]

    for value in values:
        if value > max_value:
            max_value = value

    return max_value

data = {"a": 5, "b": 12, "c": 3}
max_value = find_max(data)
print(f"The maximum value in the dictionary is: {max_value}")