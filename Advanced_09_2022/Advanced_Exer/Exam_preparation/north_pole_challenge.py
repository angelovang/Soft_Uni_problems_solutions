row, col = map(int, input().split(', '))
gifts = 0
my_pos = []
field = []
items = {
    'D': 0,
    'G': 0,
    'C': 0,
}

for r in range(row):
    field.append(input().split())
    for c in field[r]:
        if c == 'Y':
            my_pos = [r, field[r].index('Y')]
        elif c != '.':
            gifts += 1


def change_position(position, direction):
    if direction == 'up':
        position[0] -= 1
        if position[0] < 0:
            position[0] = row - 1
    elif direction == 'down':
        position[0] += 1
        if position[0] > row - 1:
            position[0] = 0
    elif direction == 'left':
        position[1] -= 1
        if position[1] < 0:
            position[1] = col - 1
    elif direction == 'right':
        position[1] += 1
        if position[1] > col - 1:
            position[1] = 0
    return (position)


command = input().split('-')

while command[0] != 'End' and gifts > 0:
    com = command[0]
    steps = int(command[1])
    field[my_pos[0]][my_pos[1]] = 'x'

    for step in range(steps):
        my_pos = change_position(my_pos, com)
        item = field[my_pos[0]][my_pos[1]]
#        print(item)
        if item != '.' and item != 'x':
            items[item] += 1
            gifts -= 1
            if gifts == 0:
                break
        field[my_pos[0]][my_pos[1]] = 'x'

    field[my_pos[0]][my_pos[1]] = 'Y'
    if gifts > 0:
        command = input().split('-')

if gifts == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f'- {items["D"]} Christmas decorations')
print(f'- {items["G"]} Gifts')
print(f'- {items["C"]} Cookies')
for r in range(row):
    print(*field[r])
