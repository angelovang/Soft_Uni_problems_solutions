rows , columns = map(int,input().split())

matrix = [input().split() for row in range(rows)]
total_squares = 0


for i in range(rows-1):
    for j in range(columns-1):
        if matrix[i][j] == matrix[i+1][j] and \
                matrix[i][j] == matrix[i][j+1] and \
                matrix[i][j] == matrix[i + 1][j+1]:
            total_squares += 1

print(total_squares)

