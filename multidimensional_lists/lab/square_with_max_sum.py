def read_matrix():
    row_count, column_count = map(int, input().split(', '))
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


def get_sum_submatrix(matrix, row_index, column_index, size):
    total_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            total_sum += matrix[r][c]
    return total_sum


def get_best_submatrix_sum(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_submatrix(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index

    return best_row_index, best_column_index


def print_result(coordinates, size):
    row_index, col_index = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_submatrix(matrix,row_index, col_index, size))


matrix = read_matrix()
SUBMATRIX_SIZE = 2

coordinates = get_best_submatrix_sum(matrix, SUBMATRIX_SIZE)
print_result(coordinates, SUBMATRIX_SIZE)
