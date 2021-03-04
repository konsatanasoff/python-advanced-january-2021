def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = list(map(int, input().split(' ')))
        matrix.append(row)
    return matrix


def get_primary_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


print(get_primary_sum(read_matrix()))