def find_expression(nums, current_sum=0, expr=""):
    if nums:
        result_plus = find_expression(nums[1:], current_sum + nums[0], f"{expr}+{nums[0]}")
        result_minus = find_expression(nums[1:], current_sum - nums[0], f"{expr}-{nums[0]}")
        return result_plus + result_minus
    return [(expr, current_sum)]


numbers = [int(n) for n in input().split(', ')]
result = find_expression(numbers)

print(*[f"{el[0]}={el[1]}" for el in result], sep='\n')
