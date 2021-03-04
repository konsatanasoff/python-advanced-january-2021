KING_SYMBOL = "K"
QUEEN_SYMBOL = "Q"
EMPTY_SQUARE = "."


def find_king(board):
    for r_index in range(len(board)):
        if KING_SYMBOL in board[r_index]:
            c_index = board[r_index].index(KING_SYMBOL)
            return r_index, c_index


def in_range(val, max_value):
    return 0 <= val < max_value


def delta_search(board, king, deltas):
    row_count = len(board)
    col_count = len(board[0])
    row_index, col_index = king
    delta_row, delta_col = deltas

    while in_range(row_index, row_count) and in_range(col_index, col_count):
        if board[row_index][col_index] == QUEEN_SYMBOL:
            return [row_index, col_index]
        row_index += delta_row
        col_index += delta_col


def get_capture_queens(board, king):
    delta_moves = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),

    ]

    queens = [
        delta_search(board, king, move)
        for move in delta_moves
    ]
    return [q for q in queens if q]


def print_result(queens):
    if queens:
        for q in queens:
            print(q)
    else:
        print("The king is safe!")


board = [input().split() for _ in range(8)]


king = find_king(board)
queens = get_capture_queens(board, king)
print_result(queens)
