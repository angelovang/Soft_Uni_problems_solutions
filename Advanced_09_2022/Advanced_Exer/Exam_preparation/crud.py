Size = 6
matrix = []

for rows in range(6):
    matrix.append(input().split())

start_position = list(map(int,(input().strip('()')).split(', ')))
last_position = []


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


while True:
    command = input().split(', ')

    if command[0] == 'Stop':
        break

    com , current_dir = command[0],command[1]
    last_position = start_position
#    print(last_position)

    if com == 'Create':
        value = command[2]
        last_position = change_position(last_position,current_dir)
        if matrix[last_position[0]][last_position[1]] == '.' :
            matrix[last_position[0]][last_position[1]] = value
        else:
            continue

    elif com == 'Update':
        value = command[2]
        last_position = change_position(last_position, current_dir)
        if matrix[last_position[0]][last_position[1]].isalnum() :
            matrix[last_position[0]][last_position[1]] = value
        else:
            continue

    elif com == 'Delete':
        last_position = change_position(last_position, current_dir)
        if matrix[last_position[0]][last_position[1]].isalnum():
            matrix[last_position[0]][last_position[1]] = '.'
        else:
            continue

    elif com == 'Read':
        last_position = change_position(last_position, current_dir)
        if matrix[last_position[0]][last_position[1]] != '.':
            print (matrix[last_position[0]][last_position[1]])
        else:
            continue
#    print(last_position)

for row in matrix:
    print(*row)
    