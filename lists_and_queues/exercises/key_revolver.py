from collections import deque

def bullet_lock_check():
    pass

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(el) for el in input().split()])
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())

total_money = intelligence_value
barrel = gun_barrel_size
reloaded = False

while True:
    if reloaded:
        barrel = gun_barrel_size
        reloaded = False

    if bullets.pop() <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    barrel -= 1
    total_money -= bullet_price

    if barrel == 0 and bullets:
        print("Reloading!")
        reloaded = True

    if not bullets or not locks:
        break

if len(bullets) < len(locks):
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${total_money}")
