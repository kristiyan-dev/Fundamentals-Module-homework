numbers = input().split()
new_list = []
for i in numbers:
    x = float(i)
    new_list.append(round(x))

# new_list = [round(float(num)) for num in numbers]


print(new_list)