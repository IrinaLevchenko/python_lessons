#  Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#  и возвращает сумму наибольших двух аргументов.

# def my_func(a, b, c):
#     params = [a, b, c]
#     try:
#         params.remove(min(params))
#         print(sum(params))
#     except TypeError:
#         return 'Enter only numbers!'
#
#
# my_func(10, 20, 30)

# решение от преподавателя:
my_func = lambda a, b, c: (a + b + c) - min(a, b, c)
print(f'Сумма наибольших двух чисел: {my_func(10, 20, 30)}')

