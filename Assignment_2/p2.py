# python program to count the frequency of each character in a string


def count_character_frequency(string):
    letter_frequency = {}
    for char in string:
        if char in letter_frequency:
            letter_frequency[char] = letter_frequency[char] + 1
        else:
            letter_frequency[char] = 1

    return letter_frequency


# Example usage and testing
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = count_character_frequency(input_string)
    print("Character frequencies:")
    for char, count in result.items():
        print(f"'{char}': {count}")
