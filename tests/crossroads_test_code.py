from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'

green_light = int(input())
free_window = int(input())

queue = deque()
cars_passed = 0
marker = False
car_hit = ''

command = input()

while not command == END_COMMAND:
    if not command == GREEN_COMMAND:
        queue.append(command)
    else:
        car_index = 0
        while car_index < green_light:
            if queue:
                current_car = queue.popleft()
                if green_light - car_index < len(current_car):
                    queue.appendleft(current_car[green_light - car_index:])
                    marker = True
                    car_hit = current_car
                    break
                else:
                    cars_passed += 1
                    car_index += len(current_car)
            else:
                break
        car_index = 0
        if marker:
            current_car = queue.popleft()
            if free_window < len(current_car):
                print('A crash happened!')
                print(f'{car_hit} was hit at {current_car[free_window - car_index]}.')
                exit()
            else:
                marker = False
                cars_passed += 1
                break

    command = input()

print('Everyone is safe.')
print(f'{cars_passed} total cars passed the crossroads.')