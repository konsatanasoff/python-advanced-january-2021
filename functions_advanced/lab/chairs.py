def combination_count(names, n, combinations=[]):
    if len(combinations) == n:
        print(', '.join(combinations))
        return

    for i in range(len(names)):
        name = names[i]
        combinations.append(name)
        combination_count(names[i + 1:], n, combinations)
        combinations.pop()


names = input().split(', ')
n = int(input())

combination_count(names, n)


