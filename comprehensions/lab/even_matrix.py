def read_matrix():
    row_count = int(input())
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()
matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(matrix)