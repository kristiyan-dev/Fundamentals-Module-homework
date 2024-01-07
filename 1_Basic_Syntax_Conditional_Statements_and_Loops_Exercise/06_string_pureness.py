number_string = int(input())

for current_string in range(number_string):
    pure_or_not_pure = input()
    if ',' in pure_or_not_pure or '.' in pure_or_not_pure or '_' in pure_or_not_pure:
        print(f'{pure_or_not_pure} is not pure!')
    else:
        print(f'{pure_or_not_pure} is pure.')
