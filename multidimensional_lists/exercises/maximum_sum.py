def read_matrix():
    row_count, column_count = map(int, input().split())
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix, row_count, column_count


def sum_checker(rows, cols, matrix):
    max_sum = 0
    best_matrix = []
    for i in range(rows - 2):
        for j in range(cols - 2):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
            matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]

            current_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2], matrix[i + 1][j], matrix[i + 1][j + 1], \
            matrix[i + 1][j + 2], matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]

            if current_sum > max_sum:
                max_sum = current_sum
                best_matrix = current_matrix

    return max_sum, best_matrix


matrix, rows, columns = read_matrix()
max_sum, best_matrix = sum_checker(rows, columns, matrix)

print(f"Sum = {max_sum}")
for el in range(0,len(best_matrix) - 2, 3):
    # row = [best_matrix[el], best_matrix[el + 1], best_matrix[el + 2]]
    print(best_matrix[el], best_matrix[el + 1], best_matrix[el + 2])
