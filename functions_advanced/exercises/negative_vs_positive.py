def num_checker(numbers):
    positives = []
    negatives = []
    for num in numbers:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)
    return positives, negatives


numbers = [int(n) for n in input().split()]
positives, negatives = num_checker(numbers)


print(sum(negatives))
print(sum(positives))
if sum(positives) > abs(sum(negatives)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
