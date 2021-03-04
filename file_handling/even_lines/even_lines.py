import re


def symbol_replacer(line):
    return re.sub(r"[\!\?\.,-]", "@", line)


with open("text.txt", "r") as file:
    data = file.readlines()
    for row in range(len(data)):
        if row % 2 == 0:
            replaced = symbol_replacer(data[row]).split()
            print(" ".join(replaced[::-1]))
