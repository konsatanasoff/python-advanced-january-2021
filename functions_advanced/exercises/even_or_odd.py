def even_odd(*args):
    cmd = list(args)[-1]
    if cmd == "even":
        result = filter(lambda x: x % 2 == 0, list(args)[0:-1])
    else:
        result = filter(lambda x: x % 2 == 1, list(args)[0:-1])
    return list(result)


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))