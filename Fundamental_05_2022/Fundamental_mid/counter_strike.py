energy = int(input())
comm_line = input()
won_battles = 0
not_energy = False

while comm_line != 'End of battle':
    current_distance = int(comm_line)
    if energy < current_distance:
        not_energy = True
        break
    else:
        energy -= current_distance
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles
    comm_line = input()

if not_energy:
    print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
else:
    print(f'Won battles: {won_battles}. Energy left: {energy}')
