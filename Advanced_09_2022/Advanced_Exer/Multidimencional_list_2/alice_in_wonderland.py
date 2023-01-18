size = int(input())
field = []
alice_pos = []
collected_bags = 0

for i in range(size):
    row = [x for x in input().split()]
    if 'A' in row :
        alice_pos = [i,row.index('A')]
    field.append(row)

step_moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),
}

r , c = alice_pos
field[r][c] = '*'

while collected_bags < 10:
    command = input()
    r += step_moves[command][0]
    c += step_moves[command][1]
    if 0 <= r < size and 0 <= c < size :

        if field[r][c] == 'R':
            field[r][c] = '*'
            break

        if field[r][c].isdigit():
            collected_bags += int(field[r][c])

        field[r][c] = '*'
    else:
        break
    field[r][c] = '*'

if collected_bags == 10:
    print(f'She did it! She went to the party.')
else:
    print(f"Alice didn't make it to the tea party.")

for row in field:
    print(*row)
