from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

queue = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{len(queue)} people remaining.')
        break
    elif command == PAID_COMMAND:
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)