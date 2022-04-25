'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until
a single-digit number is produced. The input will be a non-negative integer.
'''


def digital_root(n):
    def digi(n):
        num = 0
        while n > 0:
            num += n % 10
            n = n // 10
        return num

    while n > 9:
        n = digi(n)
    return n