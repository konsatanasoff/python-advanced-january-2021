n_lines = int(input())

parking = set()

for _ in range(n_lines):
    direction, car_number = input().split(', ')

    if direction == 'IN' and car_number not in parking:
        parking.add(car_number)
    elif direction == "OUT" and car_number in parking:
        parking.remove(car_number)

if parking:
    print(*parking, sep='\n')
else:
    print('Parking Lot is Empty')
