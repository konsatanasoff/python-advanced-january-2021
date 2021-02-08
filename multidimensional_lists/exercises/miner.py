def check_remaining_coal(field_size):
    remaining_coals_count = 0
    for r in range(field_size):
        for c in range(field_size):
            if field[r][c] == "c":
                remaining_coals_count += 1

    return remaining_coals_count


def is_valid_move(move, field_size):
    return 0 <= move < field_size


def move_miner(field, position):
    row = position[0]
    col = position[1]
    coals_count = 0

    if field[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        quit()
    elif field[row][col] == "c":
        field[row][col] = "*"
        coals_count += 1
        if not check_remaining_coal(field_size):
            print(f"You collected all coals! ({row}, {col})")
            quit()

    return coals_count


field_size = int(input())
commands = input().split()
field = [input().split() for _ in range(field_size)]

current_position = [0, 0]
total_coal_count = 0

for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == "s":
            current_position = [row, col]
            break


for cmd in commands:
    row = current_position[0]
    col = current_position[1]

    if cmd == "left":
        move = col - 1
        if is_valid_move(move, field_size):
            current_position = [row, move]

    elif cmd == "right":
        move = col + 1
        if is_valid_move(move, field_size):
            current_position = [row, move]

    elif cmd == "up":
        move = row - 1
        if is_valid_move(move, field_size):
            current_position = [move, col]

    elif cmd == "down":
        move = row + 1
        if is_valid_move(move, field_size):
            current_position = [move, col]

    total_coal_count += move_miner(field, current_position)


print(f"{check_remaining_coal(field_size)} coals left. ({current_position[0]}, {current_position[1]})")