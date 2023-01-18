number_of_cities = int(input())

total_profit = 0

for i in range(1,number_of_cities+1):
    current_profit = 0
    name = input()
    income = float(input())
    expenses = float(input())
    current_profit += (income - expenses)
    if i % 3 == 0 and i % 5 != 0:
        current_profit -= 0.5 * expenses
    if i % 5 == 0 :
        current_profit = current_profit - income * 0.1
    print(f'In {name} Burger Bus earned {current_profit:.2f} leva.')
    total_profit += current_profit

print(F'Burger Bus total profit: {total_profit:.2f} leva.')


