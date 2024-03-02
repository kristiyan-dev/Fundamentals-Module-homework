def check_employee_happiness(happiness_values, improvement_factor):
    happiness_list = list(map(int, happiness_values.split()))
    improved_happiness = [happiness * improvement_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(1 for happiness in improved_happiness if happiness >= average_happiness)
    total_count = len(improved_happiness)

    if happy_count >= total_count / 2:
        print(f"Score: {happy_count}/{total_count}. Employees are happy!")
    else:
        print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


employee_happiness = input()
improvement_factor = float(input())

check_employee_happiness(employee_happiness, improvement_factor)
