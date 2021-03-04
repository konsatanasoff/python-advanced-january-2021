def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


def primary_diagonal_sum(matrix):
    diagonal_sum = 0
    diag_items = []
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
        diag_items.append(matrix[i][i])
    return diagonal_sum, diag_items


def secondary_diagonal_sum(matrix):
    diagonal_sum = 0
    diag_items = []
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][::-1][i]
        diag_items.append(matrix[i][::-1][i])
    return diagonal_sum, diag_items


matrix = read_matrix()
primary_sum, primary_items = primary_diagonal_sum(matrix)
secondary_sum, secondary_items = secondary_diagonal_sum(matrix)

print(f"First diagonal: {', '.join(map(str, primary_items))}. Sum: {primary_sum}")
print(f"Second diagonal: {', '.join(map(str, secondary_items))}. Sum: {secondary_sum}")