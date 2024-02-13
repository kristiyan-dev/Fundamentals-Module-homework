def print_cupid_data(neighborhood, current_index):
    print(f"Cupid's last position was {current_index}.")

    if sum(neighborhood) == 0:
        print(f"Mission was successful.")
    else:
        failed_house = [house for house in neighborhood if house != 0]
        print(f"Cupid has failed {len(failed_house)} places.")


def cupid_main_logic(neighborhood):
    current_index = 0

    while True:
        command = input()
        if command == "Love!":
            break

        command_split = command.split()
        step = int(command_split[1])

        if current_index + step <= len(neighborhood) - 1:
            current_index += step
            if neighborhood[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")
            else:
                neighborhood[current_index] -= 2
                if neighborhood[current_index] == 0:
                    print(f"Place {current_index} has Valentine's day.")
        else:
            current_index = 0
            if neighborhood[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")
            else:
                neighborhood[current_index] -= 2
                if neighborhood[current_index] == 0:
                    print(f"Place {current_index} has Valentine's day.")

    return neighborhood, current_index


data = list(map(int, input().split('@')))
neighborhood_, last_index = cupid_main_logic(data)
print_cupid_data(neighborhood_, last_index)