#  Для списка реализовать обмен значений соседних элементов, т.е.
#  Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().

my_boyfriends = []
count = int(input('Введите количество своих парней: '))
while count:
    name = input('Введите имя своего парня:')
    my_boyfriends.append(name)
    count -= 1
print(f'Список парней: {my_boyfriends}')

for i in range(1, len(my_boyfriends), 2):
    my_boyfriends[i - 1], my_boyfriends[i] = my_boyfriends[i], my_boyfriends[i - 1]
print(f'А лучше бы в таком порядке: {my_boyfriends}')



