numbers = int(input())

for current_number in range(1, numbers + 1):
    current_number_as_string = str(current_number)
    digits_sum = 0
    for digit in current_number_as_string:
        digits_sum += int(digit)
    is_special = False
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        is_special = True
    print(f'{current_number} -> {is_special}')

# numbers = int(input())
#
# for current_number in range(1, numbers + 1):
#     current_number_as_string = str(current_number)
#     digits_sum = 0
#     for digit in current_number_as_string:
#         digits_sum += int(digit)
#     if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
#         print(f'{current_number} -> True')
#     else:
#         print(f'{current_number} -> False')
