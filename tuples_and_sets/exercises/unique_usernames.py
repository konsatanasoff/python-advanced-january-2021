def input_to_set(count):
    lines = set()
    for _ in range(count):
        lines.add(input())
    return lines


n_lines = int(input())
usernames = input_to_set(n_lines)

print(*usernames, sep='\n')
