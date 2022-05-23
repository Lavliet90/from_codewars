'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
'''


def to_camel_case(text):
    conwert_word = (text.replace('_', '-').split('-'))[0]
    for word in text.replace('_', '-').split('-')[1:]:
        conwert_word += word.capitalize()
    return conwert_word
