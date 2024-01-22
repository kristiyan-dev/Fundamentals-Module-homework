animal = input().upper().split(', ')

if animal[len(animal) - 1] == 'sheep':
    count_sheep = animal.count('sheep')
    print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")
elif animal[len(animal) - 1] == 'wolf':
    print("Please go away and stop eating my sheep")
