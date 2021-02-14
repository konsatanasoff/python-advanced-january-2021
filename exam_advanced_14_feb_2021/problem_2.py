from math import floor


def search_in_matrix(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


def is_inside_territory(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_new_position(command, current_position):
    new_row, new_col = current_position[0], current_position[1]
    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "right":
        new_col += 1
    elif command == "left":
        new_col -= 1
    return new_row, new_col


def is_wall(matrix, row, col):
    if matrix[row][col] == "X":
        return True
    return False


size = int(input())
field = [list(input().split()) for _ in range(size)]
player_position = search_in_matrix(field, size, "P")

total_coins = 0
path = []

while total_coins < 100:
    command = input()
    new_row, new_col = get_new_position(command, player_position)

    if is_inside_territory(new_row, new_col, size) and not is_wall(field, new_row, new_col):
        path.append([new_row, new_col])
        total_coins += int(field[new_row][new_col])
        player_position = new_row, new_col

    else:
        print(f"Game over! You've collected {floor(total_coins / 2)} coins.")
        break

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
print("Your path:")
[print(el) for el in path]