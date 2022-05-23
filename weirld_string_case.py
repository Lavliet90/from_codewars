'''
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all
even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be
upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present
if there are multiple words. Words will be separated by a single space(' ').
'''


def to_weird_case(string):
    weird_string = ''
    for word in string.split():
        weird_word = ''
        for letter in range(len(word)):
            if letter % 2 != 0:
                weird_word += word[letter].lower()
            else:
                weird_word += word[letter].upper()
        if word == string.split()[-1]:
            weird_string += weird_word
        else:
            weird_string += weird_word + ' '
    return weird_string
