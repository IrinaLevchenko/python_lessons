number = int(input('Введите целое положительное число: '))

maxdigit = 0  # самая большая цифра в числе
while number > 0:
    a = number % 10  # отделяем по цифре от числа. a - цифра
    if a > maxdigit:
        maxdigit = a
    number //= 10
print(maxdigit)
