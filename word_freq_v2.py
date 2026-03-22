def word_frequency(text):
    words = text.lower()
    words = words.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = "Hello hello HELLO"
result = word_frequency(text)

for word in result:
    print(f"{word}: {result[word]}")