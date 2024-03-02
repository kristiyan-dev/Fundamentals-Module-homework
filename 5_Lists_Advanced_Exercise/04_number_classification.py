def categorize_numbers(numbers):
    numbers_list = list(map(int, numbers.split(", ")))

    positive_numbers = [num for num in numbers_list if num >= 0]
    negative_numbers = [num for num in numbers_list if num < 0]
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    odd_numbers = [num for num in numbers_list if num % 2 != 0]

    return positive_numbers, negative_numbers, even_numbers, odd_numbers


input_numbers = input()
positive, negative, even, odd = categorize_numbers(input_numbers)


print(f"Positive: {', '.join(map(str,positive))}")
print(f"Negative: {', '.join(map(str,negative))}")
print(f"Even: {', '.join(map(str,even))}")
print(f"Odd: {', '.join(map(str,odd))}")
