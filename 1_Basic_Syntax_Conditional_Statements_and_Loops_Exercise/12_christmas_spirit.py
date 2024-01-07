qty = int(input())
remaining_days = int(input())
total_cost = 0
total_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        qty += 2
    if current_day % 2 == 0:
        total_cost += qty * ornament_set
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += qty * (tree_skirt + tree_garland)
        total_spirit += 10 + 3
    if current_day % 5 == 0:
        total_cost += qty * tree_lights
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights
if remaining_days % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
