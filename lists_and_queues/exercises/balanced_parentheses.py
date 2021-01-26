sequence = input()
is_balanced = True

opening = []

mirror = {'{': '}', '[': ']', '(': ')'}

for el in sequence:
    if el in '{[(':
        opening.append(el)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_el = opening.pop()
        if not mirror[current_opening_el] == el:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')