qty_water = int(input())
capacity_of_tank = 255

for i in range (qty_water):
    current_water = int(input())
    if current_water > capacity_of_tank:
        print("Insufficient capacity!")
        continue
    capacity_of_tank -= current_water
print(255 - capacity_of_tank)
