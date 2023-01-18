from collections import deque
orders = []
food = int(input())
orders = deque(int(num) for num in input().split())

if orders:
    print(max(orders))
while orders:
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        print('Orders left:',*orders,sep=' ')
        break
if not orders:
    print(f'Orders complete')
