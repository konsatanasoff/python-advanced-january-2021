from collections import deque

total_food = int(input())
food_orders = deque([int(el) for el in input().split()])
food_left = []

print(max(food_orders))

for i in range(len(food_orders)):
    if total_food < food_orders[0]:
        break
    total_food -= food_orders.popleft()


if food_orders:
    print(f"Orders left: {' '.join([str(el) for el in food_orders])}")
else:
    print('Orders complete')

