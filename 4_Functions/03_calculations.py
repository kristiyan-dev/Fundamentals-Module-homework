def calculate(a, b, x):
    if x == "multiply":
        return a * b
    elif x == "divide":
        return a // b
    elif x == "add":
        return a + b
    elif x == "subtract":
        return a - b


input_operator = input()
first_number = int(input())
second_number = int(input())
print(calculate(first_number, second_number, input_operator))
