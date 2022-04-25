'''
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
'''


def tower_builder(n_floors):
    piramida = []
    for i in range(1, n_floors + 1):
        text = ''
        text += (' ' * int(n_floors - i)) + ('*' * (1 + ((i - 1) * 2))) + (' ' * int(n_floors - i))
        piramida.append(text)
    return piramida


print(tower_builder(6))