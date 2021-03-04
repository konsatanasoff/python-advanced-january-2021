def read_matrix():
    row_count = int(input())
    matrix = []
    for row_index in range(row_count):
        row = list(input())
        matrix.append(row)
    return matrix


def player_location(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "P":
                return r, c


def is_valid_move(matrix,p_row, p_col, move_row, move_col):
    if 0 <= p_row + move_row < len(matrix) and 0 <= p_col + move_col < len(matrix):
        return True
    return False


def player_moves(string, matrix, commands, moves):
    for cmd in commands:
        player_row, player_col = player_location(matrix)
        current_player_location = matrix[player_row][player_col]
        matrix[player_row][player_col] = "-"
        current_move_row, current_move_col = moves[cmd]
        if is_valid_move(matrix, player_row, player_col, current_move_row, current_move_col) and cmd in moves:
            move_position = matrix[player_row + current_move_row][player_col + current_move_col]
            if not move_position == "-":
                string += move_position
            matrix[player_row + current_move_row][player_col + current_move_col] = "P"

        else:
            string = string[:-1]
            matrix[player_row][player_col] = "P"
    return matrix, string


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

string = input()
matrix = read_matrix()
m = int(input())
commands = []

for _ in range(m):
    cmd = input()
    commands.append(cmd)

result_matrix, result_string = player_moves(string, matrix, commands, moves)

print(result_string)
print(*[f"{''.join(el)}" for el in result_matrix], sep='\n')
