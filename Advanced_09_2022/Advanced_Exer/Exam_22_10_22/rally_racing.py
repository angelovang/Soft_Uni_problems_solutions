def change_position(position, direction):
    if direction == 'up':
        position[0] -= 1
    elif direction == 'down':
        position[0] += 1
    elif direction == 'left':
        position[1] -= 1
    elif direction == 'right':
        position[1] += 1
    return position


size = int(input())
racing_number = input()

distance = 0
car_pos = [0, 0]
t = []
finish = False

matrix = []
for row in range(size):
    matrix.append(input().split())
    if 'T' in matrix[row]:
        t.append([row, matrix[row].index('T')])


dir_ = input()
while dir_ != 'End' and not finish:

    car_pos = change_position(car_pos, dir_)
    r, c = car_pos
    if matrix[r][c] == '.':
        distance += 10

    elif matrix[r][c] == 'T':
        matrix[r][c] = '.'
        distance += 30
        if r == t[0][0] and c == t[0][1]:
            r , c = t[1]

        else:
            r , c = t[0]
        car_pos = [r, c]
        matrix[r][c] = '.'

    elif matrix[r][c] == 'F':
        distance += 10
        finish = True

    dir_ = input()

if finish:
    print(f'Racing car {racing_number} finished the stage!')
else:
    print(f'Racing car {racing_number} DNF.')
print(f'Distance covered {distance} km.')
matrix[car_pos[0]][car_pos[1]] = 'C'

for row in matrix:
    print(''.join(row))
