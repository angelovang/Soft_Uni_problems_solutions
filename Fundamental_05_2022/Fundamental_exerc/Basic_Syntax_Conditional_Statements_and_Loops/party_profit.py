from math import floor
group_size = int(input())
days = int(input())

companions_count = group_size
coins = 0

for current_day in range(1, days + 1):
    coins += 50
    if current_day % 10 == 0:
        companions_count -= 2
    if current_day % 15 == 0:
        companions_count += 5
    if current_day % 3 == 0:
        coins -= 3 * companions_count
    if current_day % 5 == 0:
        coins += 20 * companions_count
        if current_day % 3 == 0:
            coins -= companions_count * 2
    coins -= companions_count * 2

coins_per_companion = floor(coins / companions_count)

print(f'{companions_count} companions received {coins_per_companion} coins each.')

