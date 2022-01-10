#  Узнайте у пользователя число n.
#  Найдите сумму чисел n + nn + nnn.
#  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# моё решение:
#user_number = input('Введите число: ')
#num1 = user_number + user_number
#num2 = user_number + user_number + user_number
#sum = int(user_number) + int(num1) + int(num2)
#print(sum)

# решение преподавателя
n = input('Введите число: ')
print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')
