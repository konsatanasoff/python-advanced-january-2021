numbers_list = [int(n) for n in input().split(", ")]
result = 1

for num in numbers_list:
    if num <= 5:
        result *= num
    elif 5 < num <= 10:
        result /= num

print(result)
