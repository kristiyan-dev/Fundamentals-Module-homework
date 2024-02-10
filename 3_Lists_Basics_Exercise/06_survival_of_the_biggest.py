numbers = [int(x) for x in input().split()]
number_for_remove = int(input())
for i in range(number_for_remove):
    numbers.remove(min(numbers))
# new_list = map(str, numbers)

print(', '.join(map(str, numbers)))
