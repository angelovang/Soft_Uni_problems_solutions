size = int(input())
field = []

for i in range(size):
    row = [x for x in input().split()]
    field.append(row)

step_moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),
}
max_eggs = 0
max_track = []
best_direction = ''

for i in range(size):
    for j in range(size):
        if field[i][j] == 'B':
            for dir in step_moves:
                eggs = 0
                direction = []
                r = i + step_moves[dir][0]
                c = j + step_moves[dir][1]
                while 0 <= r < size and 0 <= c < size :
                    if field[r][c] != 'X':
                        eggs += int(field[r][c])
                        direction.append([r,c])
                        r += step_moves[dir][0]
                        c += step_moves[dir][1]
                    else:
                        break
                if eggs >= max_eggs:
                    max_eggs = eggs
                    max_track = direction
                    best_direction = dir
        else:
            continue

print(best_direction)
for x in max_track:
    print(x)
print(max_eggs)

