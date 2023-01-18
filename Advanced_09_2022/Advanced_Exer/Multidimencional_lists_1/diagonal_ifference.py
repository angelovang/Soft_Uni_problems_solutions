size = int(input())

matrix = [input().split() for row in range(size)]
sum_1 = 0
sum_2 = 0

#print (matrix)

for i in range(size):
    sum_1 += int(matrix[i][i])
    sum_2 += int(matrix[i][(size - 1) - i])

diff = abs(sum_1 - sum_2)
print(diff)

