def recursive_power(num, pwr):
    if pwr == 1:
        return num
    return num * recursive_power(num, pwr - 1)

#
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))