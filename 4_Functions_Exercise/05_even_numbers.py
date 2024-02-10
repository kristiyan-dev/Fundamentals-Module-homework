numbers = [int(num) for num in input().split()]


def num(x):
    if x % 2 == 0:
        return True


even = filter(num, numbers)
new_list = []
for x in even:
    new_list.append(x)
print(new_list)