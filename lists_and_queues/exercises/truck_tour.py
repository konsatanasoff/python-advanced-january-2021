from collections import deque

n_lines = int(input())

stations = deque()

for _ in range(n_lines):
    stations.append(input())


for big_circle_iter in range(n_lines):
    is_valid = True
    sum_petrol = 0

    for small_circle_iter in range(n_lines):
        current_station = stations[small_circle_iter]

        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        sum_petrol += petrol - distance

        if sum_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break

    if is_valid:
        print(big_circle_iter)
        break
