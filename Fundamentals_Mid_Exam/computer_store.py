total_sum = 0
total_tax = 0
total_check = 0
while True:
    command = input()
    if command == 'special' or command == 'regular':
        if command == "special":
            total_tax = total_sum * 0.20
            total_check = (total_sum + total_tax) * 0.90
        elif command == "regular":
            total_tax = total_sum * 0.20
            total_check = total_sum + total_tax
        break
    command = float(command)
    if command < 0:
        print("Invalid price!")
        continue
    total_sum += command
if total_check > 0:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_sum:.2f}$\n"
          f"Taxes: {total_tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_check:.2f}$")
else:
    print("Invalid order!")
