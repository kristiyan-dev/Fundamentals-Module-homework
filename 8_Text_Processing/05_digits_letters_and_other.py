# elements = input()
# digits = []
# letters = []
# special_symbols = []
# for el in elements:
#     if el.isdigit():
#         digits.append(el)
#     elif el.isalpha():
#         letters.append(el)
#     elif not el.isalnum():
#         special_symbols.append(el)
#
# print(*digits, sep="")
# print(*letters, sep="")
# print(*special_symbols, sep="")

text = input()
numbers = ""
letters = ""
characters = ""
for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        characters += char
print(numbers)
print(letters)
print(characters)