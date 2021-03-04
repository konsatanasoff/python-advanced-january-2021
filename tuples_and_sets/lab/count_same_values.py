data = map(float, input().split())

value_count = {}

for el in data:
    if el not in value_count:
        value_count[el] = 0
    value_count[el] += 1

for (value, count) in value_count.items():
    print(f"{value} - {count} times")