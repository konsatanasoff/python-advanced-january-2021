def read_matrix():
    row_count, column_count = map(int, input().split(', '))
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def get_column_sum(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])

    all_sums = []

    for column_index in range(column_count):
        column_sum = 0
        for row_index in range(row_count):
            column_sum += matrix[row_index][column_index]
        all_sums.append(column_sum)
    return all_sums


def print_result(data):
    [print(x) for x in data]


matrix = read_matrix()
result = get_column_sum(matrix)
print_result(result)
