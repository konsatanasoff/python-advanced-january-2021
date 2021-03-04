def num_type_check(numbers):
    data = {"Positive": [],
            "Negative": [],
            "Even": [],
            "Odd": [],
            }
    for number in numbers:
        if number >= 0:
            data["Positive"].append(number)
        if number < 0:
            data["Negative"].append(number)
        if number % 2 == 0:
            data["Even"].append(number)
        if number % 2 == 1:
            data["Odd"].append(number)
    return data


nums = [int(el) for el in input().split(', ')]
result = [f"{key}: {', '.join(map(str, value))}" for key, value in num_type_check(nums).items()]

[print(el) for el in result]



