def palindrome(string):
    cleaned = ""
    for char in string:
        if char.isalnum():
            cleaned = cleaned + char.lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    user_input = input("Enter a word or sentence:")
    if palindrome(user_input):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
