budget = float(input())
price_of_flour = float(input())

eggs_price = price_of_flour * 0.75
price_milk = (price_of_flour * 1.25) / 4
loaves_price = price_of_flour + eggs_price + price_milk
total_loves = 0
colors_eggs = 0

while loaves_price <= budget:
    total_loves += 1
    colors_eggs += 3
    budget -= loaves_price
    if total_loves % 3 == 0:
        colors_eggs -= total_loves - 2
print(f"You made {total_loves} loaves of Easter bread! Now you have {colors_eggs} eggs and {budget:.2f}BGN left.")
