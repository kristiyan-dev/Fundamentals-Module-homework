def sort_name():
    names = input().split(', ')
    sorted_name = sorted(names, key=lambda  name: (-len(name), name))

    return sorted_name

result = sort_name()
print(result)