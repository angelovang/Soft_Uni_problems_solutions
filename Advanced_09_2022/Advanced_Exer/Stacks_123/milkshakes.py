from collections import deque

chocolates = [int(choc) for choc in input().split(', ')]
milk = deque(int(mil) for mil in input().split(', '))

made_shakes = 0

while made_shakes < 5 and chocolates and milk:
    choc = chocolates[-1]
    mil = milk[0]

    if choc <= 0 or mil <= 0 :
        if choc <= 0 :
            chocolates.pop()

        if mil <= 0 :
            milk.popleft()
        continue

    if choc == mil :
#        if chocolates:
        chocolates.pop()
#        if milk :
        milk.popleft()
        made_shakes += 1

    else:
        milk.append(milk.popleft())
        chocolates[-1] = chocolates[-1] - 5

if made_shakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolates:
    print(f'Chocolate:', ', '.join(map(str, chocolates)))
else:
    print(f'Chocolate: empty')
if milk:
    print(f'Milk:', ', '.join(map(str, milk)))
else:
    print(f'Milk: empty')
