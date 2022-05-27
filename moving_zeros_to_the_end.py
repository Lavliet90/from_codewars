'''
Write an algorithm that takes an array and moves all of the
zeros to the end, preserving the order of the other elements.
'''


def move_zeros(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] == 0 and array[i + 1] == 0:
                continue
            elif array[i] == 0 and array[i + 1] != 0:
                array[i], array[i + 1] = array[i + 1], array[i]
            else:
                continue

    return array


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
