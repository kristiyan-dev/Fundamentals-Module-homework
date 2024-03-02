items = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()

left_sum = sum(items[:entry_point])
right_sum = sum(items[entry_point + 1:])

if type_of_items == "cheap":
    left_sum = sum(filter(lambda x: x < items[entry_point], items[:entry_point]))
    right_sum = sum(filter(lambda x: x < items[entry_point], items[entry_point + 1:]))
elif type_of_items == "expensive":
    left_sum = sum(filter(lambda x: x >= items[entry_point], items[:entry_point]))
    right_sum = sum(filter(lambda x: x >= items[entry_point], items[entry_point + 1:]))

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")