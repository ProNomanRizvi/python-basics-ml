def read_file():
    with open("data.txt", "r") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    read_file()