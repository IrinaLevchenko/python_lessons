n = input('Введите целое положительное число: ')
n = int(n)

maxdigit = 0

while n > 0:
    a = n % 10
    if a > maxdigit:
        maxdigit = a
    n = n // 10

print(maxdigit)
