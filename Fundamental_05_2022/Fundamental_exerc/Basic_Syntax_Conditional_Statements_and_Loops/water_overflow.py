number_of_lines = int(input())
capacity = 255
liters_in_the_tank = 0

for line in range(number_of_lines):
    liters_water = int(input())
    if liters_water > (capacity - liters_in_the_tank):
        print(f'Insufficient capacity!')
        continue
    else:
        liters_in_the_tank += liters_water

print(liters_in_the_tank)

