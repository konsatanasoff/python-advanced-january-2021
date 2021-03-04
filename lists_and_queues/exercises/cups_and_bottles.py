from collections import deque

cup_queue = deque([int(el) for el in input().split()])
water_bottles = deque([int(el) for el in input().split()])

wasted_water = 0

while True:
    current_bottle = water_bottles.pop()
    current_cup = cup_queue.popleft()
    diff = current_bottle - current_cup
    if diff < 0:
        cup_queue.appendleft(abs(diff))

    if current_bottle > current_cup:
        wasted_water += diff

    if not water_bottles or not cup_queue:
        break

if water_bottles:
    print(f"Bottles: {' '.join(map(str, water_bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cup_queue))}")

print(f"Wasted litters of water: {wasted_water}")