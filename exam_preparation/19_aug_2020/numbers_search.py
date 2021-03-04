def numbers_searching(*args):
    numbers = [n for n in args]
    missing_num = 0
    repeated = []
    for i in range(min(numbers), max(numbers)):
        if i not in numbers:
            missing_num = i
    for num in numbers:
        if numbers.count(num) > 1:
            repeated.append(num)
    repeated = list(set(repeated))
    return [missing_num, sorted(repeated)]


# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))