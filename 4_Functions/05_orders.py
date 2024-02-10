def products(tipe, qty):
    if tipe == 'coffee':
        return qty * 1.50
    elif tipe == 'water':
        return qty * 1.00
    elif tipe == 'coke':
        return qty * 1.40
    elif tipe == 'snacks':
        return qty * 2.00


current_products = input()
current_qty = int(input())
print(f'{products(current_products, current_qty):.2f}')
