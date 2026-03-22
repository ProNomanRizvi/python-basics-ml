# Character Frequency

def char_frequency(text):
    text = text.lower()
    freq = {}

    for char in text:
        if char == " ":
            continue

        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

chars = char_frequency("Hello World")

for char in chars:
    print(f"{char}: {chars[char]}")