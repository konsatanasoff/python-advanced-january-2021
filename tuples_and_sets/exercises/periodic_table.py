def input_to_set(count):
    lines = set()
    for _ in range(count):
        elements = input()
        if " " in elements:
            for el in elements.split():
                lines.add(el)
        else:
            lines.add(elements)
    return lines


n = int(input())
elements = input_to_set(n)

print(*elements, sep='\n')