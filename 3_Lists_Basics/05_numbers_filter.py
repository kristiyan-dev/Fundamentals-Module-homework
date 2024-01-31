number = int(input())
my_numbers = []
finish_list = []

for i in range(number):
    current_number = int(input())
    my_numbers.append(current_number)
command = input()
if command == 'even':
    for number in my_numbers:
        if number % 2 == 0:
            finish_list.append(number)
elif command == "odd":
    for number in my_numbers:
        if number % 2 != 0:
            finish_list.append(number)
elif command == "negative":
    for number in my_numbers:
        if number < 0:
            finish_list.append(number)
elif command == "positive":
    for number in my_numbers:
        if number >= 0:
            finish_list.append(number)
print(finish_list)
