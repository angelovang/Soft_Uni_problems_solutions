import sys
rows, columns = map(int, input().split())

matrix = [input().split() for row in range(rows)]
max_sum = -sys.maxsize - 1
start_index = [0, 0]


def calculation(x, y, matrix_):
    sum = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            sum += int(matrix_[i][j])
    return sum


def print_submatrix(x, y, matrix_):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            print(matrix_[i][j], end=' ')
        print()


for i in range(rows - 2):
    for j in range(columns - 2):
        current_sum = calculation(i, j, matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i, j

print(f'Sum = {max_sum}')
x, y = start_index
print_submatrix(x,y,matrix)

