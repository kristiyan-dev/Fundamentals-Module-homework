# def add_new(a, b):
#     return a + b
# # print(add_new(int(input()), int(input()),))
#
# number1 = int(input())
# numbers2 = int(input())
#
# print(add_new(number1, numbers2))

# def add_ten(a, b, c, d):
#     return a + b + c + d
#
#
# aa = int(input())
# bb = int(input())
# cc = int(input())
# dd = int(input())
# result = add_ten(aa, bb, cc, dd)
# print(result)

# def greet(name='Word'):
#     return f'Hello, {name}!'
# print(greet())
# print(greet('Mike'))

# def greet(name, message='Hello'):
#     return f'{message}, {name}'
# print(greet('Alice'))
# print(greet(message='Hi There', name='Ivan'))

# def add(x, y):
#     return  x + y
#
# add_lambda = lambda x, y: x + y
# print(add(5, 5))
# print(add_lambda(5, 10))

# nums = [1, 2, 3, 4, 5, 6]
# double_number = list(map(lambda x: x * 2, nums))
# print(double_number)

# def count_recursive(n):
#     if n == 1:
#         print(n)
#
#     else:
#         count_recursive(n - 1)
#         print(n)
#
# count_recursive(10)

# def calculate_stats(number):
#     total_sum = sum(number)
#     average = total_sum / len(number)
#     max_number = max(number)
#     min_number = min(number)
#
#     return total_sum, average, max_number, min_number
#
#
# data = [10, 20, 30, 40, 50]
# total, average, maximum, minimum = calculate_stats(data)
# print('Data:', data)
# print('Total:', total)
# print('Average', average)
# print('Maximum:', maximum)
# print('Minimum', minimum)