# def my_func(x, y):
#     if y < 0 and y is int(y):
#         print(x ** y)
#
#
# my_func(2, -1)


def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(my_func(2, -1))
