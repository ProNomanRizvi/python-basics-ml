def calculate_sum():
    total = 0

    with open("data.txt", "r") as file:
        for line in file:
            try:
                value = int(line.strip())
                total += value
            except:
                continue

    return total


def main():
    total = calculate_sum()
    print(f"Total sum: {total}")


if __name__ == "__main__":
    main()