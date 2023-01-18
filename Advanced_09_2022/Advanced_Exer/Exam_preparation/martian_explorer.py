Size = 6
field = []
rover_position = []
deposits = {'W': 0, 'M': 0, 'C': 0}
commands = []


def change_position(position, direction):
    if direction == 'up':
        position[0] -= 1
        if position[0] < 0:
            position[0] = Size-1
    elif direction == 'down':
        position[0] += 1
        if position[0] > Size-1:
            position[0] = 0
    elif direction == 'left':
        position[1] -= 1
        if position[1] < 0:
            position[1] = Size-1
    elif direction == 'right':
        position[1] += 1
        if position[1] > Size-1:
            position[1] = 0
    return (position)


for row in range(Size):
    field.append(input().split(' '))
    if 'E' in field[row]:
        rover_position = [row, field[row].index('E')]

commands = input().split(', ')

for com in commands:
    row, col = change_position(rover_position, com)

    if field[row][col] == 'R':
        print(f'Rover got broken at ({row}, {col})')
        break
    elif field[row][col] == 'W':
        deposits[field[row][col]] += 1
        print(f'Water deposit found at ({row}, {col})')

    elif field[row][col] == 'M':
        deposits[field[row][col]] += 1
        print(f'Metal deposit found at ({row}, {col})')

    elif field[row][col] == 'C':
        deposits[field[row][col]] += 1
        print(f'Concrete deposit found at ({row}, {col})')

for dep_len in deposits.values():
    if dep_len == 0 :
        print(f'Area not suitable to start the colony.')
        break
else:
    print(f'Area suitable to start the colony.')

