number_of_line = int(input())
word = input()
first_list = []
second_list = []


for current_line in range(number_of_line):
    current_word = input()
    first_list.append(current_word)
    if word in first_list:
        second_list.append(current_word)

print(first_list)
print(second_list)