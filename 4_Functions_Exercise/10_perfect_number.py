# def is_perfect(numbers):
#     divisions_sum = sum(i for i in range(1, numbers) if numbers % i == 0)
#
#     if divisions_sum == numbers:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# numbers = int(input())
# print(is_perfect(numbers))


numbers = int(input())
numbers_sum = 0
for i in range(1, numbers):
    if numbers % i == 0:
        if numbers_sum == numbers:
            break
        numbers_sum += i
if numbers_sum % numbers == 0:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
