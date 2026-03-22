def calculate_average():
    total = 0
    count = 0

    with open("data.txt", "r") as file:
        for line in file:
            try:
                value = int(line.strip())
                total += value
                count += 1
            except:
                continue

    if count == 0:
        return 0

    return total / count


def main():
    avg = calculate_average()
    print(f"Average: {avg:.2f}")


if __name__ == "__main__":
    main()