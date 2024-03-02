vehicles = input().split(">>")
total_tax = 0


for vehicle in vehicles:
    vehicle_info = vehicle.split(" ")


    if len(vehicle_info) != 3 or not vehicle_info[1].isdigit() or not vehicle_info[2].isdigit():
        print("Invalid input format for vehicle:", vehicle)
        continue


    car_type, years, kilometers = vehicle_info
    years, kilometers = int(years), int(kilometers)


    if car_type == "family":
        tax = 50 - 5 * years + 12 * (kilometers // 3000)
    elif car_type == "heavyDuty":
        tax = 80 - 8 * years + 14 * (kilometers // 9000)
    elif car_type == "sports":
        tax = 100 - 9 * years + 18 * (kilometers // 2000)
    else:
        print("Invalid car type.")
        continue


    tax = max(tax, 0)
    total_tax += tax
    print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
