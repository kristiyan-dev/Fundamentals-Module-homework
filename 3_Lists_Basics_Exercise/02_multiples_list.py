factor = int(input())
count = int(input())
new_list = []

for multiplier in range(1, count + 1):
    new_list.append(factor * multiplier)
print(new_list)
