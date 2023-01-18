flowers = input()
count_fl = int(input())
budget = int(input())

total_sum = 0

if flowers == 'Roses':
    if count_fl > 80 :
        total_sum = count_fl * 5 * 0.9
    else :
        total_sum = count_fl * 5

elif flowers == 'Dahlias':
    if count_fl > 90:
        total_sum = count_fl * 3.8 * 0.85
    else:
        total_sum = count_fl * 3.8

elif flowers == 'Tulips':
    if count_fl > 80:
        total_sum = count_fl * 2.8 * 0.85
    else:
        total_sum = count_fl * 2.8

elif flowers == 'Narcissus':
    if count_fl < 120:
        total_sum = count_fl * 3 * 1.15
    else:
        total_sum = count_fl * 3

elif flowers == 'Gladiolus':
    if count_fl < 80:
        total_sum = count_fl * 2.5 * 1.2
    else:
        total_sum = count_fl * 2.5

diff = budget - total_sum

if diff >= 0 :
    print (f'Hey, you have a great garden with {count_fl} {flowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(diff):.2f} leva more.')


