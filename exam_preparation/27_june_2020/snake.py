def search_in_matrix(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


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


def is_inside_territory(row, col, size):
    return 0 <= row < size and 0 <= col < size


def print_result(food_quantity, matrix):
    print(f"Food eaten: {food_quantity}")
    [print("".join(row)) for row in matrix]


size = int(input())
field = [list(input()) for _ in range(size)]
snake_position = search_in_matrix(field, size, "S")
eaten_food = 0


while eaten_food < 10:
    command = input()
    new_row, new_col = get_new_position(command, snake_position)

    if not is_inside_territory(new_row, new_col, size):
        field[snake_position[0]][snake_position[1]] = "."
        print("Game over!")
        break

    elif field[new_row][new_col] == "*":
        eaten_food += 1

    elif field[new_row][new_col] == "B":
        field[new_row][new_col] = "."
        new_row, new_col = search_in_matrix(field, size, "B")

    field[new_row][new_col] = "S"
    field[snake_position[0]][snake_position[1]] = "."
    snake_position = search_in_matrix(field, size, "S")

else:
    print("You won! You fed the snake.")

print_result(eaten_food, field)