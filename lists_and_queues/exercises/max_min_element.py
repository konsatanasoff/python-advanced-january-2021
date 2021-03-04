from collections import deque

n_queries = int(input())

stack = deque()

for _ in range(n_queries):
    data = input().split()

    if data[0] == '1':
        stack.appendleft(data[1])
    elif data[0] == '2' and stack:
        stack.popleft()
    elif data[0] == '3' and stack:
        max_el = max([int(el) for el in stack])
        print(max_el)
    elif data[0] == '4' and stack:
        min_el = min([int(el) for el in stack])
        print(min_el)

print(', '.join(stack))
