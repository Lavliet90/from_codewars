

# a = [1, 4, 6, 3]
# k = iter(a)
#
# print(next(k))
# print(next(k))
# print(next(k))


# k = iter([a ** 2 for a in range(6)])
#
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
#
#
# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(3)
# print(next(s_iter1))
# print(next(s_iter1))
#

# print(next(s_iter1))
# print(next(s_iter1))
#
# from datetime import datetime
#
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         stat = datetime.now()
#         result = func(*args, **kwargs)
#         print(datetime.now() - stat)
#         return result
#
#     return wrapper
#
# @timeit
# def one(n):
#     l = []
#     for i in range(n):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# @timeit
# def two(n):
#     return [x for x in range(n) if x % 2 == 0]
#
#
#
# l1 = one
# l1(1000)
# l2 = two(10000)
#
# # print(l1)
# # print(l2)


a = []
b = a
a.append('fefef')
print(b)

c = 'fefef'
v = c
c = 'efe'
print(v)






def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))

    return inner


print(one())

print(dir(one()))
