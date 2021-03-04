with open("numbers.txt", "r") as file:
    res = 0
    for el in file.readlines():
        el.rstrip('n')
        res += int(el)
    print(res)
