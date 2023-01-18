items_with_their_price = input().split('|')
budget = int(input())

items_list = []
prices_list = []
buy_items_list = []
sell_sum = 0
profit = 0

for element in items_with_their_price:
    temp_list = element.split('->')
    items_list.append(temp_list[0])
    prices_list.append(float(temp_list[1]))

for i in range(len(items_list)):
    buy_it = False
    if items_list[i] == 'Clothes' and prices_list[i] <= 50:
        buy_it = True
    elif items_list[i] == 'Shoes' and prices_list[i] <= 35:
        buy_it = True
    elif items_list[i] == 'Accessories' and prices_list[i] <= 20.50:
        buy_it = True
    else:
        continue
    if budget >= prices_list[i] and buy_it:
        budget -= prices_list[i]
        buy_items_list.append(1.4 * prices_list[i])
        sell_sum += prices_list[i] * 1.4
        profit += prices_list[i] * 0.4

for item in buy_items_list:
    print(f'{item:.2f}',end=' ')
print()
print(f'Profit: {profit:.2f}')

if (budget + sell_sum) >= 150 :
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
