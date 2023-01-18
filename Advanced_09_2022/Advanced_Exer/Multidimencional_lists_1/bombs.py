size = int(input())

matrix = [[int(x) for x in input().split()] for row in range(size) ]
bomb_index = [tuple(int(j) for j in i.split(',')) for i in input().split()]
matrix_copy = matrix.copy()

bomb_damage_index = {
    'up_left' : (-1,-1),
    'up' : (-1,0),
    'up_right' : (-1,1),
    'left' : (0,-1),
    'right' : (0,1),
    'dwn_left' : (1,-1),
    'dwn' : (1,0),
    'dwn_right' : (1,1),
}

for index in bomb_index:
    bomb_power = matrix[index[0]][index[1]]
    matrix_copy[index[0]][index[1]] -=  bomb_power
    for key in bomb_damage_index:
        x = index[0] + bomb_damage_index[key][0]
        y = index[1] + bomb_damage_index[key][1]
        if 0 <= x < size and 0 <= y < size :
            if matrix_copy[x][y] > 0 :
                matrix_copy[x][y] -= bomb_power

alive_cells = 0
sum_of_cells = 0

for i in range(size):
    for j in range(size):
        if matrix_copy[i][j] > 0 :
            alive_cells += 1
            sum_of_cells += matrix_copy[i][j]

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_cells}')
for row in matrix_copy:
    print(*row)

