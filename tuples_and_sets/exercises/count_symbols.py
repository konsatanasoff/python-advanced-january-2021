# With dictionary

# def sym_counter(string):
#     data = {}
#     for el in string:
#         if el not in data:
#             data[el] = 1
#         else:
#             data[el] += 1
#     return data
#
#
# string = input()
# count_data = sym_counter(string)
# set_sorted_data = sorted(set(count_data))
#
# for chr in set_sorted_data:
#     count = count_data[chr]
#     print(f"{chr}: {count} time/s")


# with set

def sym_counter(string):
    data = []
    for el in string:
        data.append(el)
    return data


string = input()
count_data = sym_counter(string)
set_sorted_data = sorted(set(count_data))

for chr in set_sorted_data:
    count = count_data.count(chr)
    print(f"{chr}: {count} time/s")