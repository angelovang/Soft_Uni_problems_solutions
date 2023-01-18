presents = int(input())
size_field = int(input())

field = []
santa_pos = []
total_nice_kids = 0
happy_nice_kids = 0

steps = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),
}

for i in range(size_field):
    row = input().split()
    if 'S' in row :
        santa_pos = [i,row.index('S')]
    total_nice_kids += row.count('V')
    field.append(row)

while True:
    dir = input()
    if dir == 'Christmas morning' or presents <= 0 :
        break

    r = santa_pos[0] + steps[dir][0]
    c = santa_pos[1] + steps[dir][1]
    field[santa_pos[0]][santa_pos[1]] = '-'
    santa_pos = r, c

    if field[r][c] == 'V':
        presents -= 1
        happy_nice_kids += 1
        field[r][c] = '-'

    elif field[r][c] == 'X':
        field[r][c] = '-'

    elif field[r][c] == 'C':
        field[r][c] = '-'
        for key , val in steps.items():
            r = santa_pos[0] + val[0]
            c = santa_pos[1] + val[1]
            if field[r][c] == 'V' or field[r][c] == 'X':
                presents -= 1
                if field[r][c] == 'V':
                    happy_nice_kids += 1
                field[r][c] = '-'
                if presents == 0:
                    break
    if presents == 0:
        break

field[santa_pos[0]][santa_pos[1]] = 'S'
diff = total_nice_kids - happy_nice_kids

if presents == 0 and diff > 0 :
    print(f'Santa ran out of presents!')
for row in field:
    print(*row)
if diff == 0 :
    print(f'Good job, Santa! {happy_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {diff} nice kid/s.')

