budget = int(input())
season = input()
fishers = int(input())

total = 0

if fishers <= 6:
    if season == 'Spring':
        total = 3000 * 0.9
    elif season == 'Winter':
        total = 2600 * 0.9
    else:
        total = 4200 * 0.9

elif 7 <= fishers <= 11:
    if season == 'Spring':
        total = 3000 * 0.85
    elif season == 'Winter':
        total = 2600 * 0.85
    else:
        total = 4200 * 0.85
elif fishers >= 12:
    if season == 'Spring':
        total = 3000 * 0.75
    elif season == 'Winter':
        total = 2600 * 0.75
    else:
        total = 4200 * 0.75

if season != 'Autumn' and fishers %2 == 0:
    total *= 0.95

diff = budget - total
if diff >= 0:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(diff):.2f} leva.')


