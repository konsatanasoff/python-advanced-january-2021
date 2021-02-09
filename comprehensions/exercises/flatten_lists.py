list_data = input().split('|')[::-1]

result = [num for group in list_data for num in group.split()]

print(' '.join(result))

