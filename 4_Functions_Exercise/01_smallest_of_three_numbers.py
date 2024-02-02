# def small_number(first, second, third):
#     if first < second and first < third:
#         return first
#     if second < first and second <third:
#         return  second
#     else:
#         return third
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# print(small_number(first_number, second_number, third_number))

def small_number(some_numbers:list): # "def small_number(some_numbers:list): -> int: prieto po konvenciq
    return min(some_numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())

small_element = small_number([first_number, second_number, third_number])
print(small_element)