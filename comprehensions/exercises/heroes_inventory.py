heroes = {hero: {"inventory": [], "cost": 0} for hero in input().split(", ")}

command = input()

while not command == "End":
    hero, item, cost = command.split("-")
    cost = int(cost)

    if item not in heroes[hero]["inventory"]:
        heroes[hero]["inventory"] += [item]
        heroes[hero]["cost"] += int(cost)

    command = input()

[print(f"{hero} -> Items: {len(data['inventory'])}, Cost: {data['cost']}") for hero, data in heroes.items()]
