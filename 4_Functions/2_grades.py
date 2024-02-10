def grades(x):
    if 2.00 <= x <= 2.99:
        return 'Fail'
    elif 3.00 <= x <= 3.49:
        return 'Poor'
    elif 3.50 <= x <= 4.49:
        return 'Good'
    elif 4.50 <= x <= 5.49:
        return 'Very Good'
    elif 5.50 <= x <= 6.00:
        return 'Excellent'


current_grade = float(input())
print(grades(current_grade))
