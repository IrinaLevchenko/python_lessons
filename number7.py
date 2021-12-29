from math import factorial


def fact(n):
    for num in range(1, n + 1):
        yield factorial(num)


fact(4)
for el in fact(4):
    print(el)
