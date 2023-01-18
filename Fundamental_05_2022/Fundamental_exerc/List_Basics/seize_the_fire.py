fires_with_their_cells = input().split('#')
total_water = int(input())

put_out_cells = []
effort = 0
total_fire = 0
cell_type = ''
cell_value = 0

for fires in fires_with_their_cells:
    valid = False
    cell_parameter = fires.split(' = ')
    cell_type = cell_parameter[0]
    cell_value = int(cell_parameter[1])
    if cell_type == 'High' and (81 <= cell_value <= 125):
        valid = True
    elif cell_type == 'Medium' and (51 <= cell_value <= 80):
        valid = True
    elif cell_type == 'Low' and (1 <= cell_value <= 50):
        valid = True
    else:
        continue
    if valid and total_water >= cell_value :
        total_water -= cell_value
        total_fire += cell_value
        effort += 0.25 * cell_value
        put_out_cells.append(cell_value)


print('Cells:')
for element in put_out_cells:
    print(f'- {element}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
