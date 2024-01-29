number_of_snowball = int(input())
top_snowball = 0
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0
for current_snowball in range(number_of_snowball):
    weight_snowball = int(input())
    needed_time = int(input())
    quality_of_snowball = int(input())
    top_snowball = (weight_snowball / needed_time) ** quality_of_snowball
    if top_snowball >= best_snowball:
        best_snowball = top_snowball
        best_weight = weight_snowball
        best_time = needed_time
        best_quality = quality_of_snowball

print(f'{best_weight} : {best_time} = {best_snowball:.0f} ({best_quality})')
