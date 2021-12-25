def my_func(a, b, c):
    params = [a, b, c]
    params.remove(min(params))
    print(sum(params))


my_func(10, 20, 30)

