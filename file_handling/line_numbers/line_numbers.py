import re

letter_path = r"[a-z]"
symbol_path = r"['\!\?\.,-]"


def get_n(line, path):
    return len(re.findall(path, line, re.IGNORECASE))


with open("text.txt", "r") as file:
    data = file.readlines()
    count = 1

    for line in data:
        n_letters = get_n(line, letter_path)
        n_symbols = get_n(line, symbol_path)
        print(f"Line {count}: {line[:-1]} ({n_letters})({n_symbols})")
        count += 1
