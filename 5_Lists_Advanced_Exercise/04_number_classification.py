def categorize_numbers(numbers):
    numbers_list = list(map(int, numbers.split(", ")))

    positive_numbers = [num for num in numbers_list if num >= 0]
    negative_numbers = [num for num in numbers_list if num < 0]
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    odd_numbers = [num for num in numbers_list if num % 2 != 0]

    return positive_numbers, negative_numbers, even_numbers, odd_numbers


input_numbers = input()
positive, negative, even, odd = categorize_numbers(input_numbers)


print(f"Positive:", *positive)
print(f"Negative:", *negative)
print(f"Even:", *even)
print(f"Odd:", *odd)
