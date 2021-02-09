def read_matrix():
    row_count = int(input())
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def calculate_mod(matrix, action, r_pos, col_pos, val):

    if action == "Add":
        matrix[r_pos][col_pos] += val
    else:
        matrix[r_pos][col_pos] -= val
    return matrix


def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


matrix = read_matrix()

command = input()

while not command == "END":
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)

    if is_valid(matrix, row, col):
        matrix = calculate_mod(matrix, action, row, col, value)
    else:
        print("Invalid coordinates")

    command = input()

[print(' '.join(map(str,row))) for row in matrix]