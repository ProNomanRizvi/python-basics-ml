def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count

def main():
    text = input("Enter a text: ")
    print(f"Vowel count: {count_vowels(text)}")

main()