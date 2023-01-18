from collections import  deque

kids_circle = deque(input().split())
toss = int(input())-1

while len(kids_circle) > 1:
    kids_circle.rotate(-toss)
    kid = kids_circle.popleft()
    print(f'Removed {kid}')
kid = kids_circle.popleft()
print(f'Last is {kid}')
