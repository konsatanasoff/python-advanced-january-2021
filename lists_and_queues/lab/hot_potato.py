from collections import deque

players = input().split(' ')
step = int(input())
queue = deque(players)

while len(queue) > 1:
    queue.rotate(-step + 1)
    print(f'Removed {queue.popleft()}')

print(f'Last is {queue.popleft()}')