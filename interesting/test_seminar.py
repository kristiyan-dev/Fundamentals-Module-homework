# personal_information = ['Sofia', '22', ['Cagliari', 'Quartucciu'], 24]
#
# new_name, age, address, new_age = personal_information
# new_address = personal_information[2][0]
#
# print(new_address)
# print(new_name)
# print(age)
# print(' '.join(address))
# print(address[0])
# print(new_age)


# personal_information = ['Sofia', '22', ['Cagliari', 'Quartucciu'], 24]
#
# new_name, age, *other = personal_information
#
# print(new_name)
# print(age)
# print(other)

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sorted(new_list, key=lambda x: x % 2 == 0))
print(list(filter(lambda x: x % 2 == 0, new_list)))
