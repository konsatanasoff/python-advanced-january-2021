def char_permutation(text, current_index=0):
    if current_index == len(text):
        print(''.join(text))

    for i in range(current_index, len(text)):
        text[current_index], text[i] = text[i], text[current_index]
        char_permutation(text, current_index + 1)
        text[current_index], text[i] = text[i], text[current_index]


text = list(input())
char_permutation(text)