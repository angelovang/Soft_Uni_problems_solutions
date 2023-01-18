days = int(input())
accom = input()
voting = input()

nights = days - 1
price = 0

if accom == 'apartment':
    price = nights * 25
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    else:
        price *= 0.5

elif accom == 'president apartment':
    price = nights * 35
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    else:
        price *= 0.8

else:
    price = nights * 18

if voting == 'positive':
    price *= 1.25
else:
    price *= 0.9

print (f'{price:.2f}')


