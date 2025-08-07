def most_freq_word(sentence):
    words = sentence.split()
    dict = {}
    for word in words:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1

    max_freq = max(dict.values())
    for word, freq in dict.items():
        if freq == max_freq:
            return word


if __name__ == "__main__":
    user_input = input("Enter a sentence:")
    print("Most frequent word:", most_freq_word(user_input))
