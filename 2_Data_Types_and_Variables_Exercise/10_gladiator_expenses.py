number_of_fight = int(input())
helmed_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0
broken_shield = 0

for current_fight in range(1, number_of_fight + 1):
    if current_fight % 2 == 0:
        total_price += helmed_price
    if current_fight % 3 == 0:
        total_price += sword_price
        if current_fight % 2 == 0:
            total_price += shield_price
            broken_shield += 1
            if broken_shield % 2 == 0:
                total_price += armor_price


print(f"Gladiator expenses: {total_price:.2f} aureus")