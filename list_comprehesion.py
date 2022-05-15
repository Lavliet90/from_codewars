'''
A seven-digit positive integer is entered. Using list comprehension, form a list lst containing
the digits of this number (the list must contain numbers, not strings). Display the result on the screen with the command:
'''
# x = input()
# lst = [int(z) for z in x]
# print(lst)


'''
A natural number N is introduced. Using list comprehension, form a two-dimensional list of size N x N, consisting of
from zeros, and along the main diagonal - ones. (The main diagonal is the elements running diagonally from the top left
corner of the matrix to its lower right corner). Output the result as a table of numbers as shown in the example below.
'''
# lengh_1 = int(input())
#
# [print([1 if i == j else 0 for i in range(lengh_1)]) for j in range(lengh_1)]

'''
The names of cities are entered in a line separated by a space. It is necessary to form a list using list comprehension,
containing names longer than five characters. Output the result in a line separated by a space.
'''

# print(*[x for x in input().split() if len(x) > 5])