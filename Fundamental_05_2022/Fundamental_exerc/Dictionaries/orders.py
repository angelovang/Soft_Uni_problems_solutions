from collections import defaultdict

stock = {}

while True:
    in_data = input()
    if in_data == 'buy':
        break
    else:
        in_data = in_data.split()
        name , price , quantity = in_data[0], float(in_data[1]), int(in_data[2])
        if name not in stock:
            stock[name] = [price,quantity]
        else:
            stock[name][0] = price
            stock[name][1] += quantity

#print(stock)
for name in stock:
    print(f'{name} -> {(stock[name][0]*stock[name][1]):.2f}')

