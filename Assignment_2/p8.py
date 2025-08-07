def replace_word(sentence, old_word, new_word):
    new_sentence = sentence.replace(old_word, new_word)
    return print(new_sentence)


if __name__ == "__main__":
    user_input = input("Enter a sentence:")
    old_word = input("Enter the word to be replaced:")
    new_word = input("Enter the new word:")
    replace_word(user_input, old_word, new_word)
