my_boyfriends = []
count = 5
i = count
while i > 0:
    name = input('Введите имя своего парня:')
    my_boyfriends.append(name)
    i -= 1
my_boyfriends = list(enumerate(my_boyfriends))
print(my_boyfriends)

my_boyfriends[0], my_boyfriends[1] = my_boyfriends[1], my_boyfriends[0]
my_boyfriends[2], my_boyfriends[3] = my_boyfriends[3], my_boyfriends[2]
print(my_boyfriends)



