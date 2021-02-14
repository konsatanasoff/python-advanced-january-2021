from collections import deque


def is_filled(fireworks):
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        return True


firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = deque([int(x) for x in input().split(', ')])


fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}


while firework_effects and explosive_power and not is_filled(fireworks):
    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()
    if not current_effect <= 0 and current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue
    if current_effect <= 0 and not current_power <= 0:
        explosive_power.append(current_power)
        continue
    else:
        current_sum = current_effect + current_power

    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        fireworks["Palm Fireworks"] += 1
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:
        fireworks["Willow Fireworks"] += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        firework_effects.append(current_effect - 1)
        explosive_power.append(current_power)
        if current_effect <= 0:
            firework_effects.pop()


if is_filled(fireworks):
    print("Congrats! You made the perfect firework show!")
if not is_filled(fireworks):
    print("Sorry. You can’t make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
[print(f"{f}: {count}") for f, count in fireworks.items()]


