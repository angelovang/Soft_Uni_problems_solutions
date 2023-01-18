from collections import deque

bees = deque (int(bee) for bee in input().split())
nectar = list(int(nect) for nect in input().split())
command = deque(input().split())

total_honey = 0
# print(bees)
# print(nectar)
# print(command)

while bees and nectar and command:
    if nectar[-1] < bees[0]:
        nectar.pop()
        continue
    else:
        bee = bees.popleft()
        com = command.popleft()
        nect = nectar.pop()
        if com == "+":
            total_honey += abs(bee + nect)
        elif com == '-':
            total_honey += abs(bee - nect)
        elif com == '*':
            total_honey += abs(bee * nect)
        elif com == '/':
            if nect != 0:
                total_honey += abs(bee / nect)

print(f'Total honey made: {total_honey}')
if bees :
    print(f"Bees left: {', '.join(map(str,bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str,nectar))}")
