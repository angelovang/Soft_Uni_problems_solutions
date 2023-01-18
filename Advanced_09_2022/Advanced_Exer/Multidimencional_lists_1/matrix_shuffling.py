rows, columns = map(int, input().split())

matrix = [input().split() for row in range(rows)]


def print_m(m,n,matrix_):
    for i in range(m):
        for j in range(n):
            print(matrix_[i][j], end=' ')
        print()


while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] == 'swap' and len(command) == 5:
        x = int(command[1])
        y = int(command[2])
        i = int(command[3])
        j = int(command[4])
        if -1 < x < rows or -1 < y < columns or -1 < i < rows or -1 < j < columns :
            temp = matrix[x][y]
            matrix[x][y] = matrix[i][j]
            matrix[i][j] = temp
            print_m(rows,columns,matrix)
        else:
            print(f'Invalid input!')
            continue
    else:
        print(f'Invalid input!')
        continue
