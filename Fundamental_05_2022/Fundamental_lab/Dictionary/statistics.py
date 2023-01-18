product_in_stock = {}
total_q = 0
while True :
    command = input()
    if command == 'statistics':
        break
    else:
        product , quantity  = command.split(': ')
        if product in product_in_stock:
            product_in_stock[product] += int(quantity)
        else:
            product_in_stock[product] = int(quantity)
        total_q += int(quantity)

print('Products in stock:')
for prod, quan in product_in_stock.items():
    print(f'- {prod}: {quan}')
print(f'Total Products: {len(product_in_stock)}')
print(f'Total Quantity: {total_q}')
