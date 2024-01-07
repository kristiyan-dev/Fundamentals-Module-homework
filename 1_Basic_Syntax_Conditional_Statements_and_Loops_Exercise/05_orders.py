number_of_orders = int(input())
total_order = 0
price_per_coffe = 0

for order in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    needed_capsul = int(input())
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if needed_capsul < 1 or needed_capsul > 2000:
        continue
    price_per_coffe = price_capsule * days * needed_capsul
    total_order += price_per_coffe
    print(f"The price for the coffee is: ${price_per_coffe:.2f}")
print(f"Total: ${total_order:.2f}")
