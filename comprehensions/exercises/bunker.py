item_categories = {item: [] for item in input().split(', ')}
n = int(input())

total_count = 0
total_quality = 0

for _ in range(n):
    line = input()
    quantity_qualities = line.split(' - ')[2].split(';')
    category, item_name = line.split(' - ')[0], line.split(' - ')[1]
    current_quantity = quantity_qualities[0].split(":")[1]
    current_quality = quantity_qualities[1].split(":")[1]

    total_count += int(current_quantity)
    total_quality += int(current_quality)

    item_categories[category].append(item_name)

avg_quality = total_quality / len(item_categories)

print(f"Count of items: {total_count}")
print(f"Average quality: {avg_quality:.2f}")
[print(f"{key} -> {', '.join(map(str, value))}") for key, value in item_categories.items()]
