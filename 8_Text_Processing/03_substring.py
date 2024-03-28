# first_text = input()
# second_text = input()
#
# while True:
#     if first_text in second_text:
#         second_text = second_text.replace(first_text,"")
#     else:
#         break
#
# print(second_text)
#
first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace(first_string, "" )
print(second_string)