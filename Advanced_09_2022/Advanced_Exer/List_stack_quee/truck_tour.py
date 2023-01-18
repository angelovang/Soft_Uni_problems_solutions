from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pumps.append(input().split())

for i in range(n):
    tank = 0
    c_pumps = pumps.copy()

    while c_pumps :
        pump = c_pumps.popleft()
        amount = int(pump[0])
        distance = int(pump[1])
        tank += amount

        if tank >= distance:
            tank -= distance
        else:
            pumps.rotate(-1)
            break

    if not c_pumps:
        print(i)
        break


