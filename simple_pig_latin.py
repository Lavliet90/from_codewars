'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
'''


def pig_it(text):
    full = []
    for word in text.split(' '):
        if word.isalpha():
            right_list = []
            right_list.append([word[letter] for letter in range(1, len(word))])
            right_list[0].append(word[0])
            right_list[0].append('ay')
            right_str = "".join(right_list[0])
            full.append(right_str)
        else:
            full.append(word)
    print(" ".join(full))
    return " ".join(full)
