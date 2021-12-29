list = [300, 2, 35, 645, 254541, 551, 32, 5]
new_list = [el for el in list if int(el) > int(list[list.index(el) - 1])]
print(new_list)
