def input_to_set(count):
    lines = set()
    for _ in range(count):
        lines.add(input())
    return lines


def element_filter(n_elements, m_elements):
    res = n_elements & m_elements
    return res


n = input().split()
n_elements = input_to_set(int(n[0]))
m_elements = input_to_set(int(n[1]))

print(*element_filter(n_elements, m_elements), sep='\n')

