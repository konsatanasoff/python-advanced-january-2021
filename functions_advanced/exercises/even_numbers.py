num_list = [int(n) for n in input().split()]
result = filter(lambda x: x % 2 == 0, num_list)

print(list(result))