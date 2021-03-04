clothes_box = [int(el) for el in input().split()]
rack_capacity = int(input())

rack_count = 1
current_capacity = rack_capacity

while len(clothes_box) > 0:
    current_cloth = clothes_box.pop()

    if current_cloth <= current_capacity:
        current_capacity -= current_cloth
    else:
        rack_count += 1
        current_capacity = rack_capacity
        current_capacity -= current_cloth

print(rack_count)