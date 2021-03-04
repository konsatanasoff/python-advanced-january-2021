from collections import deque

customers = deque(int(n) for n in input().split(', '))
taxis = deque([int(n) for n in input().split(', ')])

total_time = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()

    if taxi >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

