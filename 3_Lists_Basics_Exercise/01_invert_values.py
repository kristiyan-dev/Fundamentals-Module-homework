list_number = input().split()
opposite_numbers = []

for number in list_number:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)

# print([-int(number) for number in input().split()]) # kys variant
