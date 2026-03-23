def clean_file():
    cleaned = []

    with open("data.txt", "r") as file:
        for line in file:
            try:
                value = int(line.strip())

                if 0 <= value <= 100:
                    cleaned.append(value)

            except:
                continue

    with open("cleaned_data.txt", "w") as file:
        for num in cleaned:
            file.write(str(num) + "\n")


def main():
    clean_file()
    print("Cleaned data written to cleaned_data.txt")


if __name__ == "__main__":
    main()