budget = float(input())
season = input()

total = 0
destination = 'Europe'
accommodation = 'Hotel'

if budget <= 100 :
    destination = 'Bulgaria'
    if season == 'summer':
        total = budget * 0.3
        accommodation = 'Camp'
    elif season == 'winter':
        total = budget * 0.7
elif budget <= 1000 :
    destination = 'Balkans'
    if season == 'summer':
        total = budget * 0.4
        accommodation = 'Camp'
    elif season == 'winter':
        total = budget * 0.8
else:
    destination = 'Europe'
    total = budget * 0.9


print(f'Somewhere in {destination}')
print(f'{accommodation} - {total:.2f}')


