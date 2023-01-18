size = 6
matrix = []
hit_buckets_column = []
scored_points = 0
prize = ''

for row in range(size):
    matrix.append(input().split())
#print(matrix)

for i in range(3):
    r , c = map(int,input().strip('()').split(', '))

    if r < 0 or r >= 6 or c < 0 or c >= 6 :
        continue
    if matrix[r][c] != 'B':
        continue
    if c in hit_buckets_column:
        continue

    if matrix[r][c] == 'B':
        sum = 0
        hit_buckets_column.append(c)
        for i in range(6):
            if matrix[i][c] != 'B':
                sum += int(matrix[i][c])

        scored_points += sum

if scored_points < 100 :
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")
else:
    if 100 <= scored_points < 200 :
        prize = 'Football'
    elif 200 <= scored_points < 300 :
        prize = 'Teddy Bear'
    elif 300 <= scored_points :
        prize = 'Lego Construction Set'

    print(f"Good job! You scored {scored_points} points, and you've won {prize}.")


