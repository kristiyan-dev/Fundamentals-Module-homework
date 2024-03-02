def find_even_indices(numbers):
    numbers_list = list(map(int, numbers.split(", ")))
    numbers = [index for index, num in enumerate(numbers_list) if num % 2 == 0]
    return numbers

# Example usage:
input_numbers = input()
even_indices = find_even_indices(input_numbers)
print(even_indices)
