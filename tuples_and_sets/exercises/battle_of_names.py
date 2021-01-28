n = int(input())

even_nums = set()
odd_nums = set()

for iter in range(1, n + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // iter

    if current_sum % 2 == 0:
        even_nums.add(current_sum)
    else:
        odd_nums.add(current_sum)

sum_even = sum(even_nums)
sum_odd = sum(odd_nums)

if sum_even == sum_odd:
    mod_set = [str(el) for el in even_nums.union(odd_nums)]
    print(f"{', '.join(mod_set)}")

elif sum_odd > sum_even:
    mod_set = [str(el) for el in odd_nums.difference(even_nums)]
    print(f"{', '.join(mod_set)}")
else:
    mod_set = [str(el) for el in even_nums.symmetric_difference(odd_nums)]
    print(f"{', '.join(mod_set)}")