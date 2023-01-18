fruit = input()
size = input()
count_sets = int(input())

total_price = 0

if size == 'small':
    if fruit == 'Watermelon':
        total_price = count_sets * 56
    elif fruit == 'Mango':
        total_price = count_sets * 36.66
    elif fruit == 'Pineapple':
        total_price = count_sets * 42.10
    elif fruit == 'Raspberry':
        total_price = count_sets * 20
    total_price *= 2

elif size == 'big':
    if fruit == 'Watermelon':
        total_price = count_sets * 28.7
    elif fruit == 'Mango':
        total_price = count_sets * 19.6
    elif fruit == 'Pineapple':
        total_price = count_sets * 24.8
    elif fruit == 'Raspberry':
        total_price = count_sets * 15.2
    total_price *=5

if 400 <= total_price <=1000:
    total_price *= 0.85
elif total_price > 1000 :
    total_price *= 0.5

print(f'{total_price:.2f} lv.')

