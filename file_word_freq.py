def read_file():
    with open("data.txt", "r") as file:
        text = file.read().lower()

        for char in ",.!?":
            text = text.replace(char, "")

        words = text.split()

    return words


def word_frequency(words):
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def main():
    words = read_file()
    result = word_frequency(words)

    for word, count in result.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()