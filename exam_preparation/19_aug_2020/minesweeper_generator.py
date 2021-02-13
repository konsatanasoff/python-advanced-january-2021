def is_valid_position(size, r, c):
    return 0 <= r < size and 0 <= c < size


def count_bombs_around(size, row, cell, matrix):
    current_count = 0
    for r in range(row - 1, row + 2):
        for c in range(cell - 1, cell + 2):
            if is_valid_position(size, r, c) and matrix[r][c] == "*":
                current_count += 1
    return str(current_count)


def calculate_number_cells(matrix):
    for row in range(len(matrix)):
        for cell in range(len(matrix)):
            if matrix[row][cell] is None:
                matrix[row][cell] = count_bombs_around(size, row, cell, matrix)
    return matrix


size = int(input())
bomb_count = int(input())
mine_field = [[None for _ in range(size)] for _ in range(size)]

for _ in range(bomb_count):
    bomb_row, bomb_col = input().split(', ')
    bomb_row, bomb_col = [int(bomb_row.strip("(")), int(bomb_col.strip(")"))]
    mine_field[bomb_row][bomb_col] = "*"

mine_field = calculate_number_cells(mine_field)
[print(" ".join(row)) for row in mine_field]