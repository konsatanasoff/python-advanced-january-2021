def read_matrix():
    row_count, column_count = map(int, input().split())
    matrix = []
    for row_index in range(row_count):
        matrix.append(["" for el in range(column_count)])
    return matrix, row_count, column_count


matrix, rows, cols = read_matrix()
word = input()

word_index = 0

for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index][col_index] = word[word_index]
        word_index += 1
        if word_index == len(word):
            word_index = 0

for i in range(rows):
    if not i % 2 == 0:
        matrix[i].reverse()
    print(''.join(matrix[i]))
