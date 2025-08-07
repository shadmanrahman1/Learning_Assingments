def remove_cmn_eng(str):
    temp = str.split()
    cmn_eng = ["is", "the", "a", "an"]
    cleaned = []
    for word in temp:
        if word.lower() not in cmn_eng:
            cleaned.append(word)

    return cleaned


if __name__ == "__main__":
    user_input = input("Enter a sentence:")
    result = remove_cmn_eng(user_input)
    print(" ".join(result))
