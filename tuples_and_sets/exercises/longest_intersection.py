def check_intersection(f_start, f_end, s_start, s_end):
    f_start, f_end, s_start, s_end = int(f_start), int(f_end), int(s_start), int(s_end)
    first_set = set()
    second_set = set()

    for i in range(f_start,f_end+1):
        first_set.add(i)
    for i in range(s_start,s_end+1):
        second_set.add(i)

    res = first_set & second_set

    return res


n = int(input())

result = []

for _ in range(n):
    first_inter, second_inter = input().split('-')
    first_start, first_end = first_inter.split(',')
    second_start, second_end = second_inter.split(',')

    result.append(check_intersection(first_start, first_end, second_start, second_end))

longest = ''
for el in result:
    if len(el) > len(longest):
        longest = el

print(f"Longest intersection is {list(longest)} with length {len(longest)}")