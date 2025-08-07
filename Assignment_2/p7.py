def count_unique_words(sentence):
    words = sentence.split()
    unique_words = set(words)
    return len(unique_words)


if __name__ == "__main__":
    user_input = input("Enter a sentence:")
    print("Number of unique words:", count_unique_words(user_input))
