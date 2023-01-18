size = int(input())
matrix = []
matrix = [[int(x) for x in input().split()] for row in range(size)]

while True:
    command = input().split()
    if 'END' in command :
        break
    else:
        com , row , col , value = command
        row = int(row)
        col = int(col)
        value = int(value)
        if 0 <= row < size and 0 <= col < size:
            if com == 'Add':
                matrix[row][col] += value
            elif com == 'Subtract':
                matrix[row][col] -= value
        else:
            print(f'Invalid coordinates')

for element in matrix:
    print(*element)
