'''

from collections import deque

x = list(map(int, input().split()))
y = deque(map(int, input().split()))


while x and y:
    x1 = x.pop()
    y1 = y.popleft()

size = 6
matrix = []
for row in range(size):
    matrix.append(input().split())


if x :
    print(f"Text: {', '.join(map(str,x))}")
if y :
    print(f"Text: {', '.join(map(str,y))}")


def change_position(position,direction):
    if direction == 'up':
        position[0] -= 1
    elif direction == 'down':
        position[0] += 1
    elif direction == 'left':
        position[1] -= 1
    elif direction == 'right':
        position[1] += 1
    return(position)

def change_position_2(position, direction):
    if direction == 'up':
        position[0] -= 1
        if position[0] < 0:
            position[0] = size-1
    elif direction == 'down':
        position[0] += 1
        if position[0] > size-1:
            position[0] = 0
    elif direction == 'left':
        position[1] -= 1
        if position[1] < 0:
            position[1] = size-1
    elif direction == 'right':
        position[1] += 1
        if position[1] > size-1:
            position[1] = 0
    return (position)


field = []
for row in range(size):
    field.append(input().split(' '))
    if 'E' in field[row]:
        start_position = [row, field[row].index('E')]

 sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for y in sorted_cart:
        result += f"{y[0]}:\n"
        for el in sorted(y[1]):
            result += f' - {el}\n'
    return result

'''