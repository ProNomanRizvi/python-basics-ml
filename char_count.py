# Output:
# Total characters (excluding spaces)

def char_count(text):
    count = 0
    for char in text:
        if char != " ":
            count += 1
    return count

def main():
    text = input("Enter a text: ")
    print(f"Character count: {char_count(text)}")

main()