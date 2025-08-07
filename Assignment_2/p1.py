# python program to count totoal number of words in a sentence
def count_words(sentence):
    words = sentence.split()
    return print(len(words))


sentence = "This is a python program"
count_words(sentence)
