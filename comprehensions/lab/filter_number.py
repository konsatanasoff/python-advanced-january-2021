start = int(input())
end = int(input())


def is_valid(x):
    return any(x % i == 0 for i in range(2, 11))


filtered_data = [x for x in range(start, end + 1) if is_valid(x)]
print(filtered_data)