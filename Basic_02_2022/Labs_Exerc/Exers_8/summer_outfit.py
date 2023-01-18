degree = int(input())
time_of_day = input()

outfit = 'Shirt'
shoes = 'Moccasins'

if time_of_day == "Morning":
    if 10<= degree <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif degree >= 25 :
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        pass
elif time_of_day == "Afternoon":
    if 18 < degree <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degree >= 25 :
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    else:
        pass
print(f'It\'s {degree} degrees, get your {outfit} and {shoes}.')

