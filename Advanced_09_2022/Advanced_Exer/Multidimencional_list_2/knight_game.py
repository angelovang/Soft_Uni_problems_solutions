size = int(input())
table = []

for i in range(size):
    row = [x for x in input()]
    table.append(row)

knight_moves = {
    'up_left':(-2,-1),
    'up_right':(-2,1),
    'dn_left':(2,-1),
    'dn_right':(2,1),
    'left_up':(-1,-2),
    'left_dn':(1,-2),
    'right_up':(-1,2),
    'right_dn':(1,2),
}

attacks = True
removed_knight = 0

while attacks :
    max_attack = 0
    max_index = []

    for i in range(size):
        for j in range(size):

            if table[i][j] == 'K':
                attack = 0

                for direction in knight_moves:
                    r = i + knight_moves[direction][0]
                    c = j + knight_moves[direction][1]

                    if 0 <= r < size and 0 <= c < size :
                        if table[r][c] == 'K':
                            attack += 1

                if attack > max_attack:
                    max_attack = attack
                    max_index = [i,j]

    if max_attack != 0:
        x , y = max_index
        table[x][y] = '0'
        removed_knight += 1
    else:
        attacks = False

print(removed_knight)
