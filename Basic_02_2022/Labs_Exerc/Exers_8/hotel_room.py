month = input()
number = int(input())

price_apart = 0
price_studio = 0

if month == 'May' or month == 'October':
    price_studio = number * 50
    price_apart = number * 65
    if 7 < number <= 14 :
        price_studio *= 0.95
    elif number > 14 :
        price_studio *= 0.7


elif month == 'June' or month == 'September':
    price_studio = number * 75.20
    price_apart = number * 68.70
    if number > 14:
        price_studio *= 0.8

elif month == 'July' or month == 'August':
    price_studio = number * 76
    price_apart = number * 77

if number > 14 :
    price_apart *= 0.9

print(f'Apartment: {price_apart:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')
