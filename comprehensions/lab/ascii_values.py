char_list = [el for el in input().split(', ')]
ascii_data = {el: ord(el) for el in char_list}
print(ascii_data)