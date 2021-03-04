def is_valid(matrix, n, m, i):
    if 0 <= m <= n and n >= 0:
        wanted = matrix[n][m]
        return wanted
    return 0


def get_magic_triangle(n):
    matrix = []
    matrix.append([1])
    matrix.append([1, 1])

    for i in range(2, n):
        row = []
        for j in range(i + 1):
            i_1 = is_valid(matrix, i - 1, j, i)
            j_1 = is_valid(matrix, i - 1, j - 1, i)
            value_sum = i_1 + j_1
            row.append(value_sum)
        matrix.append(row)

    return matrix


# get_magic_triangle(5)