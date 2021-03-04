from collections import deque


def is_filled(bombs):
    if bombs[40] >= 3 and bombs[60] >= 3 and bombs[120] >= 3:
        return True
    return False


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = deque([int(x) for x in input().split(', ')])


bombs = {
    40: 0,
    60: 0,
    120: 0,
}

while bomb_effects and bomb_casings and not is_filled(bombs):
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    current_sum = current_effect + current_casing

    if current_sum in bombs:
        bombs[current_sum] += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

if is_filled(bombs):
    print("Bene! You have successfully filled the bomb pouch!")
if not is_filled(bombs):
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
if not bomb_casings:
    print("Bomb Casings: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))} ")
print(f"Cherry Bombs: {bombs[60]}")
print(f"Datura Bombs: {bombs[40]}")
print(f"Smoke Decoy Bombs: {bombs[120]}")

