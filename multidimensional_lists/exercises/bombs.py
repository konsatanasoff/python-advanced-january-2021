def read_matrix():
    row_count = int(input())
    matrix = []
    for row_index in range(row_count):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix, row_count


def is_radius_valid(row, col, row_count):
    if 0 <= row < row_count and 0 <= col < row_count:
        return True
    return False


def find_current_bomb(index, coordinates):
    bomb_row, col_bomb = coordinates[index].split(',')
    bomb_row, col_bomb = int(bomb_row), int(col_bomb)
    return bomb_row, col_bomb


def calculate_blast_radius(dmg, matrix, row, col, row_count):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_radius_valid(r, c, row_count) and matrix[r][c] > 0:
                matrix[r][c] -= damage

    return matrix


def is_cell_alive(matrix, row_count):
    alive_cells = []

    for row in range(row_count):
        for col in range(row_count):
            cell = matrix[row][col]
            if cell > 0:
                alive_cells += [cell]

    return alive_cells


matrix, row_count = read_matrix()
coordinates = [el for el in input().split()]


for bomb in coordinates:
    row, col = list(map(int, bomb.split(",")))
    damage = matrix[row][col]
    if damage > 0:
        matrix = calculate_blast_radius(damage, matrix, row, col, row_count)

cells_alive = is_cell_alive(matrix, row_count)
total_sum = sum(cells_alive)

print(f"Alive cells: {len(cells_alive)}")
print(f"Sum: {sum(cells_alive)}")
[print(' '.join(map(str, row))) for row in matrix]


