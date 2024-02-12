new_wagons = []
while True:
    number_of_people = int(input())
    number_of_wagons = [int(num) for num in input().split()]

    for i in range(len(number_of_wagons)):
        if 0 < i < 4:
            i += 1
            number_of_people -= 1
            new_wagons.append(i)
            if number_of_people <= 0:
                break
