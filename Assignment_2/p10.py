def title_case(str):
    words = str.split()
    list = []
    for word in range(len(words)):
        words[word] = words[word].capitalize()  # Capitalize each word in the
        list.append(words[word])
    return " ".join(list)


if __name__ == "__main__":
    user_input = input("Enter a sentence:")
    print("Title case:", title_case(user_input))
