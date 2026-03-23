def clean_data(data):
    cleaned_data = []
    for num in data:
        if 0 <= num <= 100:
            cleaned_data.append(num)
    return cleaned_data

# ------
def main():
    data = []
    while len(data) < 5:
        num = int(input("Enter a number: "))
        data.append(num)
    print(f"Original Data: {data}")
    print(f"Cleaned Data: {clean_data(data)}")

main()