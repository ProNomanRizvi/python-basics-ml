def clean_text(text):
    text = text.lower()
    words = text.split()
    return " ".join(words)

def main():
    text = input("Enter a text: ")
    print("Original text: ", text)
    print(f"Cleaned text: {clean_text(text)}")


main()