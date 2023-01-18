from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullet_stack = list(map(int,input().split()))
locks = deque(map(int,input().split()))
value_of_intelligence = int(input())
result = 0
revolver = gun_barrel
total_bullet = 0

while True:
    if not bullet_stack or not locks:
        break
    else:
        lock = locks.popleft()
        bullet = bullet_stack.pop()
        total_bullet += bullet
        revolver -= 1
        if revolver == 0:
            revolver = gun_barrel
            print(f'Reloading!')
        while bullet > lock :
            print(f'Ping!')
            if bullet_stack:
                bullet = bullet_stack.pop()
                total_bullet += bullet
                revolver -= 1
                if revolver == 0:
                    revolver = gun_barrel
                    print(f'Reloading!')
            else:
                break
        else:
            print(f'Bang!')






