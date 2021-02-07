def read_matrix():
    row_count, column_count = map(int, input().split())
    matrix = []
    for row_index in range(row_count):
        row = input().split()
        matrix.append(row)
    return matrix, row_count, column_count


def check_equal_elements(row, col, matrix):
    current_el = matrix[row][col]
    next_el = matrix[row][col + 1]
    bottom_el = matrix[row + 1][col]
    bottom_el_right = matrix[row + 1][col + 1]

    if current_el == next_el and next_el == bottom_el and bottom_el == bottom_el_right:
        return True
    return False


matrix, rows, columns = read_matrix()
count = 0

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        if check_equal_elements(row_index, col_index, matrix):
            count += 1

print(count)