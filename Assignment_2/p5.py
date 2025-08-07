def word_frequency(text):
    temp = text.split()
    frequency = {}
    for word in temp:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency


if __name__ == "__main__":
    input_text = input("Enter a sentence:")
    result = word_frequency(input_text)
    print("Word frequencies:")
    for word, count in result.items():
        print(f"'{word}': {count}")
