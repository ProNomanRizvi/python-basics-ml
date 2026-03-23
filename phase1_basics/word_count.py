def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def main():
    text = input("Enter a text: ")
    print(f"Word count: {count_words(text)}")

main()