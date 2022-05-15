'''
Divide text into sentences. In general, he did it for a friend, tried to be as clear as possible, but the first option
did not fit, because. split() was required there
'''

text = 'fefef? efef f. efew wef! EFefe'
punk = ['.', '?', '!']
new_text = []
predlozenie = ''
for i in text:
    predlozenie += i
    if i in punk:
        new_text.append(predlozenie)
        predlozenie = ''

print(new_text)



text = 'fefef? efef f. efew wef! EFefe'

replacements = ('!', '?')
for znak in replacements:
    text = text.replace(znak, '.')
words = text.split('.')
print(words)
