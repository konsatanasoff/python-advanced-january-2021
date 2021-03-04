from collections import deque


def pureness_calculation(numbers):
    pureness = 0
    for i, v in enumerate(numbers):
        pureness += i * v
    return pureness


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    k = min(k, len(numbers))
    rotations = 0
    best_pureness = pureness_calculation(numbers)

    for rotation in range(k + 1):
        current_pureness = pureness_calculation(numbers)
        if best_pureness < current_pureness:
            rotations = rotation
            best_pureness = current_pureness
        numbers.appendleft(numbers.pop())

    return f"Best pureness {best_pureness} after {rotations} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
