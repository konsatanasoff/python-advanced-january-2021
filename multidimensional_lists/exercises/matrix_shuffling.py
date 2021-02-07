def read_matrix():
    row_count, column_count = map(int, input().split())
    matrix = []
    for row_index in range(row_count):
        row = input().split()
        matrix.append(row)
    return matrix, row_count, column_count


def check_if_valid_index(index_row, index_col, rows, cols):
    if 0 <= index_row < rows and 0 <= index_col < cols:
        return True
    return False


def check_if_valid_command(command, coords, rows, cols):
    if len(coords) == 4 and command == "swap":
        for index in range(0, len(coords), 2):
            if check_if_valid_index(coords[index], coords[index + 1], rows, cols):
                return True
    return False


def print_matrix(matrix):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            print(f"{matrix[row_index][col_index]}", end=' ')
        print()


matrix, rows, cols = read_matrix()

data = input()

while not data == "END":
    split_data = data.split()
    command = split_data[0]
    coordinates = [int(el) for el in split_data[1:]]

    if check_if_valid_command(command, coordinates, rows, cols):
        current_row, current_col = coordinates[0], coordinates[1]
        row_swap, col_swap = coordinates[2], coordinates[3]
        temp = matrix[current_row][current_col]
        matrix[current_row][current_col] = matrix[row_swap][col_swap]
        matrix[row_swap][col_swap] = temp
        print_matrix(matrix)
    else:
        print("Invalid input!")
    data = input()