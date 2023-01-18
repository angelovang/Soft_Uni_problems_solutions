from collections import deque

bowls_ramen = list(map(int,input().split(', ')))
customers = deque(map(int,input().split(', ')))

while bowls_ramen and customers:
    ramen = bowls_ramen.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue

    elif ramen > customer:
        ramen -= customer
        bowls_ramen.append(ramen)

    elif customer > ramen:
        customer -= ramen
        customers.appendleft(customer)

if not customers:
    print(f'Great job! You served all the customers.')
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str,bowls_ramen))}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str,customers))}")
