# matrix = [
#     [7, 1, 3, 3, 2, 1],
#     [1, 3, 9, 8, 5, 6],
#     [4, 6, 7, 9, 1, 0],
# ]


def read_matrix():
    row_count, column_count = map(int, input().split(', '))
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()

total_sum = 0
for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        total_sum += row[c]
    # total_sum += sum(row)

print(total_sum)
print(matrix)