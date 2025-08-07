def count_vowel_consonant(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    cons_count = 0

    for char in string:
        if char in vowels:
            vowel_count = vowel_count + 1

        else:
            cons_count = cons_count + 1

    return vowel_count, cons_count


if __name__ == "__main__":
    input = input("Enter a string: ")
    count_vowel_consonant(input)
    print("Number of vowels:", count_vowel_consonant(input)[0])
    print("Number of consonants:", count_vowel_consonant(input)[1])
