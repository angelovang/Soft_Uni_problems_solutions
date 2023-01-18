dog_food_kg = int(input())
dog_food_gm = dog_food_kg * 1000

total_dog_food = 0
command = '0'

while command != 'Adopted':
    total_dog_food += int(command)
    command = input()

diff = dog_food_gm - total_dog_food
if diff >= 0 :
    print(f'Food is enough! Leftovers: {diff} grams.')
else :
    print(f'Food is not enough. You need {abs(diff)} grams more.')

