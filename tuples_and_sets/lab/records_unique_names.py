def data_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


n_lines = int(input())
data = data_to_list(n_lines)

print(*set(data), sep='\n')
