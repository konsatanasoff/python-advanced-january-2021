from collections import deque


def list_manipulator(list, *args):
    result = deque(list)
    action = args[0]
    position = args[1]

    if action == "add":
        to_add = args[2:]
        if position == "beginning":
            [result.appendleft(el) for el in to_add[::-1]]
        else:
            [result.append(el) for el in to_add]
    else:
        to_remove = 1
        if not len(args) <= 2:
            to_remove = args[2]

        if position == "beginning":
            for _ in range(to_remove):
                result.popleft()
        else:
            for _ in range(to_remove):
                result.pop()

    return [el for el in result]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
