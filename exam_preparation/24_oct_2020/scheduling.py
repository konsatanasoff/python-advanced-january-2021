numbers = [int(n) for n in input().split(', ')]
index = int(input())

cycles = 0
desired_task = numbers[index]

for num in sorted(numbers):
    if num <= desired_task:
        cycles += num

print(cycles)
