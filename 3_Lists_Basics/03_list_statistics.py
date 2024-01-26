number = int(input())
positive_list = []
negative_list = []

for i in range(number):
    new_input = int(input())
    if new_input > 0:
        positive_list.append(new_input)
    elif new_input < 0:
        negative_list.append(new_input)

count_positive = len(positive_list)
sum_negative = sum(negative_list)
print(positive_list)
print(negative_list)

print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')
