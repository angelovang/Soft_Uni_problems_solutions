size = int(input())

matrix = [input().split(', ') for row in range(size)]
sum_1 = 0
sum_2 = 0

print(f'Primary diagonal: ', end='')
for i in range(size):
    print(matrix[i][i], end=', ' if i < size-1 else '.')
    sum_1 += int(matrix[i][i])
print(f' Sum: {sum_1}')

print(f'Secondary diagonal: ', end='')
for i in range(size):
    print(matrix[i][(size - 1) - i], end=', ' if i < size-1 else '.')
    sum_2 += int(matrix[i][(size - 1) - i])
print(f' Sum: {sum_2}')
