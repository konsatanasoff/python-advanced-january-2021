def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = list(map(int, input().split(' ')))
        matrix.append(row)
    return matrix


def primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def secondary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][::-1][i]
    return diagonal_sum


matrix = read_matrix()
primary_sum = primary_diagonal_sum(matrix)
secondary_sum = secondary_diagonal_sum(matrix)

total_sum = primary_sum - secondary_sum

print(abs(total_sum))