energy = 100
coins = 100
open = True
last_energy = 0

first_list = input().split('|')
# print(first_list)
event_list = []

for first in first_list:
    event_list.append(first.split('-'))

for event in event_list:
    if event[0] == 'rest':
        last_energy = energy
        energy += int(event[1])
        gained_energy = energy - last_energy
        if energy > 100:
            energy = 100
            gained_energy = 100 - last_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event[0] == 'order':
        if energy - 30 < 0:
            print(f'You had to rest!')
            if energy + 50 > 100:
                energy = 100
            else:
                energy += 50
        else:
            coins += int(event[1])
            energy -= 30
            print(f'You earned {int(event[1])} coins.')
    else:
        if int(event[1]) > coins :
            print(f'Closed! Cannot afford {event[0]}.')
            open = False
            break
        else:
            coins -= int(event[1])
            print(f'You bought {event[0]}.')

if open :
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')


