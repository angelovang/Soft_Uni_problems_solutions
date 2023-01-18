size = 5
field = []
my_pos = []
total_targets = 0
targets = 0
target_list = []

step_moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),
}

for i in range(size):
    row = [x for x in input().split()]
    if 'A' in row :
        my_pos = [i,row.index('A')]
    if 'x' in row :
        total_targets += row.count('x')
    field.append(row)

num_of_commands = int(input())

for com in range(num_of_commands):
    command = input().split()

    if command[0] == 'shoot':
        r , c = my_pos
        dir = command[1]
        while targets < total_targets:
            r += step_moves[dir][0]
            c += step_moves[dir][1]
            if 0 <= r < size and 0 <= c < size:
                if field[r][c] == 'x' :
                    field[r][c] = '.'
                    targets += 1
                    target_list.append([r,c])
                    break
            else:
                break
        if targets == total_targets:
            print(f'Training completed! All {total_targets} targets hit.')
            break

    elif command[0] == 'move' :
        dir = command[1]
        step = int(command[2])
        r = my_pos[0] + step_moves[dir][0]*step
        c = my_pos[1] + step_moves[dir][1]*step
        if 0 <= r < size and 0 <= c < size and field[r][c] == '.':
            my_pos = r,c

if targets < total_targets:
    print(f'Training not completed! {total_targets - targets} targets left.')
print(*target_list, sep = '\n')

