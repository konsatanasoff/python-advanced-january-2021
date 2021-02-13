from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
match_count = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    elif female <= 0:
        females.popleft()
        continue
    elif male % 25 == 0:
        males.pop()
        continue
    elif female % 25 == 0:
        females.popleft()
        continue
    elif male == female:
        females.popleft()
        males.pop()
        match_count += 1
    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {match_count}")
if not males:
    print(f"Males left: none")
else:
    print(f"Males left: {(', '.join(map(str, reversed(males))))}")

if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {(', '.join(map(str, females)))}")