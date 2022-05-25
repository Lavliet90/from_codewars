'''
Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns
the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing.
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
'''


def find_missing_letter(chars):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in range(len(letters)):
        if letters[letter] in chars:
            for point in range(letter, len(letters)):
                if letters[point] not in chars:
                    return (letters[point])
        else:
            continue


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))
