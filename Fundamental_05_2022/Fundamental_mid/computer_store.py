command = ''
total_price = 0
total_taxes = 0
total_without = 0
while True:
    command = input()
    if command == 'regular' or command == 'special':
        total_price = total_without + total_taxes
        break
    else:
        part_price = float(command)
        if part_price <= 0:
            print(f'Invalid price!')
        else:
            total_without += part_price
            total_taxes += part_price * 0.2

if total_price == 0:
    print(f'Invalid order!')
else:
    if command == 'special':
        total_price = total_price * 0.9
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price:.2f}$")

