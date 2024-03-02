import math

budget = float(input())
students = int(input())
package_of_flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

flour_needed = students * package_of_flour_price
flour_free = students // 5
eggs_needed = students * 10
aprons_needed = math.ceil(students * 1.20)
if students % 5 == 0:
    flour_needed = flour_needed - (flour_free * package_of_flour_price)

total_flour = flour_needed
total_eggs = eggs_needed * single_egg_price
total_apron = aprons_needed * single_apron_price

total_cost = total_flour + total_eggs + total_apron


if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")