day_count = int(input())
food = float(input())

t_food = 0
total_dog_food = 0
total_cat_food = 0
biscuits = 0

for i in range(day_count):
    dog_food = int(input())
    cat_food = int(input())
    if (i + 1) % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1
    t_food = t_food + dog_food + cat_food
    total_dog_food += dog_food
    total_cat_food += cat_food

biscuits = round(biscuits)
percent_dog = (total_dog_food * 100) / t_food
percent_cat = (total_cat_food * 100) / t_food
percent_total_food = (t_food * 100) / food

print(f'Total eaten biscuits: {biscuits}gr.')
print(f'{percent_total_food:.2f}% of the food has been eaten.')
print(f'{percent_dog:.2f}% eaten from the dog.')
print(f'{percent_cat:.2f}% eaten from the cat.')
