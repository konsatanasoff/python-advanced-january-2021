def read_matrix():
    row_count = int(input())
    matrix = []
    for row_index in range(row_count):
        row = [el for el in input()]
        matrix.append(row)
    return matrix, row_count


def is_valid(row, col, row_count):
    if 0 <= row < row_count and 0 <= col < row_count:
        return True
    return False


def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]

    for i in range(len(rows)):
        potential_row = row + rows[i]
        potential_col = col + cols[i]
        if is_valid(potential_row, potential_col, row_count):
            position = matrix[potential_row][potential_col]
            if position == "K":
                kills += 1
    return kills


matrix, row_count = read_matrix()

removed = 0
while True:
    max_kills = 0
    current_position = []

    for row_index in range(row_count):
        for col_index in range(row_count):
            if matrix[row_index][col_index] == "K":
                kills = calculate_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    current_position = [row_index, col_index]
    if current_position:

        matrix[current_position[0]][current_position[1]] = '0'
        removed += 1
    else:
        break
print(removed)
