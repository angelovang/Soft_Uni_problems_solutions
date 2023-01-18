from collections import deque

rows, col = map(int, input().split())

txt = input()
txt_deq = deque()
matrix = []

for ch in txt:
    txt_deq.append(ch)

for i in range(rows):
    row = []
    if i % 2 == 0 :
        for j in range(col) :
            row.append(txt_deq[0])
            txt_deq.rotate(-1)
        matrix.append(row)
    else:
        for j in range(col) :
            row.append(txt_deq[0])
            txt_deq.rotate(-1)
        matrix.append(row[::-1])
#print(matrix)
for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end='')
    print()




