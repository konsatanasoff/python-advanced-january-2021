def read_matrix():
    row_count, column_count = map(int, input().split())
    matrix = []
    for row_index in range(row_count):
        row = []
        for col_index in range(column_count):
            data = chr(97 + row_index) + chr(97 + row_index + col_index) + chr(97 + row_index)
            row.append(data)
        matrix.append(row)
    return matrix


matrix = read_matrix()

[print(' '.join(el)) for el in matrix]