from functools import reduce
list = [num for num in range(100, 1001) if num % 2 == 0]
print(list)
print(reduce(lambda num_1, num_2: num_1 * num_2, list))
