def operation_func(cmd, numbers):
    res = 0
    if cmd == "Odd":
        res = sum(filter(lambda x: x % 2 == 1, numbers))
    else:
        res = sum(filter(lambda x: x % 2 == 0, numbers))
    return res


command = input()
numbers = [int(n) for n in input().split()]
result = operation_func(command, numbers) * len(numbers)

print(result)