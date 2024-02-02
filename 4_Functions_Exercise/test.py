def small_number(some_numbers: list):
    """Find small number in 3 input"""
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())

small_element = small_number([first_number, second_number, third_number])
print(small_element)
print(small_number.__doc__)